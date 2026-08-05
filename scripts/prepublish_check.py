#!/usr/bin/env python3
"""
Simple local pre-publication scanner.

This is a convenience check, not a guarantee that a repository is safe.
Always manually inspect `git diff --cached` before pushing.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys


SKIP_DIRS = {
    ".git",
    "venv",
    ".venv",
    "__pycache__",
    "node_modules",
    "data",
}

SKIP_FILES = {
    "prepublish_check.py",
}

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".json", ".yml", ".yaml", ".ini",
    ".env", ".example", ".service", ".sh", ".toml", ".cfg",
}

PATTERNS = [
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("Bearer token", re.compile(r"Authorization\s*[:=]\s*Bearer\s+[A-Za-z0-9._~+/=-]{12,}", re.I)),
    ("Private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("Telegram bot token", re.compile(r"\b\d{6,12}:[A-Za-z0-9_-]{25,}\b")),
    ("Generic secret assignment", re.compile(
        r"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\b"
        r"\s*[:=]\s*[\"']?(?!YOUR_|CHANGE_ME|replace-|example|<)[A-Za-z0-9._~+/=-]{12,}"
    )),
]

DANGEROUS_FILENAMES = {
    ".env",
    "database.sqlite",
    "id_rsa",
    "id_ed25519",
}


def likely_text_file(path: Path) -> bool:
    if path.name in DANGEROUS_FILENAMES:
        return True
    if path.suffix.lower() in TEXT_SUFFIXES:
        return True
    if path.name.endswith(".example"):
        return True
    return False


def scan(root: Path) -> int:
    findings = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        if any(part in SKIP_DIRS for part in path.parts):
            continue

        if path.name in SKIP_FILES:
            continue

        rel = path.relative_to(root)

        if path.name in DANGEROUS_FILENAMES:
            findings.append((str(rel), 0, f"dangerous filename: {path.name}"))

        if not likely_text_file(path):
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append((str(rel), lineno, label))

    if findings:
        print("Potential sensitive content found:\n")
        for filename, lineno, label in findings:
            location = f"{filename}:{lineno}" if lineno else filename
            print(f"  - {location}: {label}")
        print("\nReview every finding before publishing.")
        return 1

    print("No obvious secrets found by this basic scanner.")
    print("Still run: git diff --cached")
    print("Manual review is required before publishing.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"Path does not exist: {root}", file=sys.stderr)
        return 2

    return scan(root)


if __name__ == "__main__":
    raise SystemExit(main())
