#!/usr/bin/env python3
"""Validate a package produced by learning-path-generator."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LEARNER_DIRS = ("projects", "journal")
REQUIRED_EXACT = ("01_资料使用顺序.md", "02_学习环境与工具.md", "03_学习计划与阶段验收.md")
UNWANTED_SUFFIXES = {
    ".exe", ".msi", ".dll", ".so", ".dylib", ".o", ".obj", ".pdb",
    ".ilk", ".class", ".pyc", ".zip", ".7z", ".rar", ".tar", ".gz",
}
UNWANTED_DIRS = {"build", "dist", "__pycache__", ".pytest_cache", "node_modules"}
PLACEHOLDER_RE = re.compile(r"\[(?:主题|学习者背景|最终可验证能力|相对路径|待填写|TODO)[^\]]*\]", re.I)
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PERSONAL_PATH_PATTERNS = (
    re.compile(r"[A-Za-z]:\\Users\\(?!Public(?:\\|$))[^\\\s]+", re.I),
    re.compile(r"/home/[^/\s]+"),
    re.compile(r"/Users/[^/\s]+"),
)


class Results:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="Path to the generated learning package")
    parser.add_argument(
        "--max-file-mb",
        type=float,
        default=10.0,
        help="Warn when a file is larger than this size (default: 10 MB)",
    )
    return parser.parse_args()


def all_entries(directory: Path) -> list[Path]:
    return list(directory.iterdir()) if directory.is_dir() else []


def check_structure(root: Path, results: Results) -> None:
    overview = list(root.glob("00_先看我_*学习总图.md"))
    if len(overview) != 1:
        results.error("Expected exactly one 00_先看我_*学习总图.md file")

    for name in REQUIRED_EXACT:
        if not (root / name).is_file():
            results.error(f"Missing required root document: {name}")

    references = root / "references"
    if not references.is_dir():
        results.error("Missing references/ directory")
    elif not (references / "00_完整学习路线.md").is_file():
        results.error("Missing references/00_完整学习路线.md")

    books = root / "books"
    if not books.is_dir():
        results.warn("Missing books/ directory; acceptable only if no long resources are useful")

    for name in LEARNER_DIRS:
        directory = root / name
        if not directory.is_dir():
            results.error(f"Missing learner-owned directory: {name}/")
            continue
        entries = all_entries(directory)
        if entries:
            rendered = ", ".join(str(item.relative_to(root)) for item in entries[:5])
            results.error(f"{name}/ must be completely empty; found: {rendered}")


def check_unwanted_files(root: Path, results: Results, max_bytes: int) -> None:
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if path.is_dir() and path.name.lower() in UNWANTED_DIRS:
            results.warn(f"Generated/build directory should usually be removed: {relative}")
        if not path.is_file():
            continue
        if path.suffix.lower() in UNWANTED_SUFFIXES:
            results.warn(f"Binary/archive file requires explicit justification: {relative}")
        try:
            if path.stat().st_size > max_bytes:
                results.warn(f"Large file requires explicit justification: {relative}")
        except OSError as exc:
            results.warn(f"Could not inspect {relative}: {exc}")


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip().strip("<>")
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0])


def check_markdown(root: Path, results: Results) -> None:
    numbered: dict[tuple[Path, str], list[Path]] = {}
    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        match = re.match(r"^(\d{2})_", path.name)
        if match:
            numbered.setdefault((path.parent, match.group(1)), []).append(path)

        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            results.error(f"Cannot read Markdown as UTF-8: {relative}: {exc}")
            continue

        if PLACEHOLDER_RE.search(text):
            results.error(f"Unresolved template placeholder in {relative}")

        for pattern in PERSONAL_PATH_PATTERNS:
            if pattern.search(text):
                results.warn(f"Possible absolute personal path in {relative}")
                break

        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = normalize_link_target(raw_target)
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue
            linked = (path.parent / target).resolve()
            try:
                linked.relative_to(root.resolve())
            except ValueError:
                results.warn(f"Relative link leaves package in {relative}: {raw_target}")
                continue
            if not linked.exists():
                results.error(f"Broken relative link in {relative}: {raw_target}")

    for (directory, prefix), files in numbered.items():
        if len(files) > 1:
            names = ", ".join(path.name for path in files)
            results.warn(f"Duplicate numeric prefix {prefix} in {directory.relative_to(root)}: {names}")


def main() -> int:
    args = parse_args()
    root = args.package.expanduser().resolve()
    results = Results()

    if not root.is_dir():
        print(f"ERROR: package directory does not exist: {root}", file=sys.stderr)
        return 2

    check_structure(root, results)
    check_unwanted_files(root, results, int(args.max_file_mb * 1024 * 1024))
    check_markdown(root, results)

    for message in results.errors:
        print(f"ERROR: {message}")
    for message in results.warnings:
        print(f"WARNING: {message}")

    print(
        f"Validation complete: {len(results.errors)} error(s), "
        f"{len(results.warnings)} warning(s)."
    )
    return 1 if results.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
