import hashlib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"^([0-9a-f]{64})\s+(\S+)")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


ok = True
text = (ROOT / "docs" / "checksums.txt").read_text(encoding="utf-8-sig")
for line in text.splitlines():
    m = PATTERN.match(line)
    if not m:
        continue
    expected, rel = m.groups()
    path = ROOT / rel
    if not path.exists():
        optional = "spare" in rel or rel.endswith(".zip")
        print("FACULTATIF MANQUANT" if optional else "MANQUANT", rel)
        ok = ok and optional
        continue
    status = "OK" if sha256(path) == expected else "DIFFERENT"
    print(status, rel)
    ok = ok and status == "OK"

print("Lot conforme." if ok else "Lot NON conforme : corrigez avant de continuer.")
sys.exit(0 if ok else 1)