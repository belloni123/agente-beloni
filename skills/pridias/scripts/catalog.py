"""Inventory local skill metadata; never execute skill code or contact services."""
import argparse
import json
import os
from pathlib import Path
import re


def scalar(text):
    text = text.strip()
    if text.startswith('"'):
        return json.loads(text)
    if text.startswith("'") and text.endswith("'"):
        return text[1:-1].replace("''", "'")
    return text


def fields(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("Missing YAML frontmatter")
    rows = match.group(1).splitlines()
    result = {}
    for index, row in enumerate(rows):
        field = re.match(r"^(name|description):[ \t]*(.*)$", row)
        if not field:
            continue
        key, value = field.groups()
        continuation = []
        for following in rows[index + 1:]:
            if following and not following[0].isspace():
                break
            continuation.append(following.strip())
        if re.fullmatch(r"[>|][-+]?[1-9]?", value):
            value = " ".join(continuation)
        elif continuation:
            value = value + " " + " ".join(continuation)
        result[key] = scalar(value).strip()
    if not result.get("name") or not result.get("description"):
        raise ValueError("Missing name or description")
    return result


def catalog(roots):
    result, warnings, seen = [], [], set()
    for root in roots:
        root = Path(root).expanduser()
        if not root.is_dir():
            continue
        paths = list(root.glob("*/SKILL.md")) + list(root.glob(".system/*/SKILL.md"))
        for path in sorted(paths):
            try:
                identity = str(path.resolve())
                if identity in seen:
                    continue
                seen.add(identity)
                if path.stat().st_size > 131072:
                    raise ValueError("Entrypoint exceeds 128 KiB")
                item = fields(path.read_text(encoding="utf-8"))
                policy = path.parent / "agents/openai.yaml"
                explicit = False
                if policy.is_file():
                    if policy.stat().st_size > 32768:
                        raise ValueError("Invocation metadata exceeds 32 KiB")
                    explicit = bool(re.search(r"^\s+allow_implicit_invocation:\s*false\s*(?:#.*)?$",
                                              policy.read_text(encoding="utf-8"), re.M))
                result.append({**item, "source": str(path), "runtime_recognized": "unverified",
                               "runtime_ready": "unverified", "requires_explicit_invocation": explicit})
            except (OSError, UnicodeError, ValueError, TypeError) as error:
                warnings.append({"source": str(path), "reason": str(error)})
    return {"skills": result, "warnings": warnings,
            "limits": "Local metadata only. Use session/provider catalogs for plugins, activation and runtime availability."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", action="append", help="Skill root; repeat as needed; replaces defaults")
    args = parser.parse_args()
    roots = args.root or [str(Path(os.environ.get("CODEX_HOME") or "~/.codex").expanduser() / "skills"),
                           "~/.agents/skills"]
    print(json.dumps(catalog(roots), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
