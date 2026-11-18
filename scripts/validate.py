"""Check models.json before it is committed. Exits non-zero on any problem.

Usage: python3 scripts/validate.py [path/to/models.json]
"""
import json, re, sys

CATS = ["coding", "writing", "reasoning", "speed", "value",
        "agents", "longdocs", "media", "selfhost"]
REQUIRED_MODEL = ["name", "maker", "price", "ctx", "access", "blurb", "s", "ev"]
REQUIRED_SOURCE = ["name", "url", "what", "used", "when", "caveat"]

def main(path):
    errors = []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(data.get("lastChecked", ""))):
        errors.append("lastChecked must be YYYY-MM-DD")

    sources = data.get("sources", {})
    for key, src in sources.items():
        for field in REQUIRED_SOURCE:
            if not str(src.get(field, "")).strip():
                errors.append(f"source {key}: missing {field}")
        if not str(src.get("url", "")).startswith("https://"):
            errors.append(f"source {key}: url must start with https://")

    models = data.get("models", [])
    if len(models) < 5:
        errors.append(f"only {len(models)} models; refusing to publish a near-empty catalogue")
    names = set()
    for m in models:
        label = m.get("name", "<unnamed>")
        for field in REQUIRED_MODEL:
            if field not in m or m[field] in ("", None, []):
                errors.append(f"{label}: missing {field}")
        if label in names:
            errors.append(f"{label}: duplicate model name")
        names.add(label)
        scores = m.get("s", {})
        for c in CATS:
            v = scores.get(c)
            if not isinstance(v, int) or not 0 <= v <= 10:
                errors.append(f"{label}: score {c} must be a whole number 0-10, got {v!r}")
        extra = set(scores) - set(CATS)
        if extra:
            errors.append(f"{label}: unknown score keys {sorted(extra)}")
        for e in m.get("ev", []):
            if not str(e.get("text", "")).strip():
                errors.append(f"{label}: evidence line with no text")
            src = e.get("source")
            if src is not None and src not in sources:
                errors.append(f"{label}: evidence cites unknown source {src!r}")

    basis_cats = {b.get("category") for b in data.get("basis", [])}
    if basis_cats != set(CATS):
        errors.append(f"basis must cover exactly these categories: {CATS}")
    for b in data.get("basis", []):
        if b.get("trust") not in (1, 2, 3, 4):
            errors.append(f"basis {b.get('category')}: trust must be 1-4")

    if errors:
        print("models.json has problems:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print(f"OK: {len(models)} models, {len(sources)} sources, checked {data['lastChecked']}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "models.json")
