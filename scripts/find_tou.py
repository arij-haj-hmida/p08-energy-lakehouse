import zipfile

ZIP = "data/raw/partitioned.zip"
TOU = b",ToU,"

with zipfile.ZipFile(ZIP) as z:
    names = sorted(
        (n for n in z.namelist() if n.endswith(".csv")),
        key=lambda n: int(n.rsplit("_", 1)[1].split(".")[0]),
    )
    print("fichier;lignes_ToU")
    for n in names:
        count, tail = 0, b""
        with z.open(n) as f:
            while True:
                chunk = f.read(1 << 20)
                if not chunk:
                    break
                data = tail + chunk
                count += data.count(TOU)
                tail = data[-(len(TOU) - 1):]
        print(f"{n.split('/')[-1]};{count}", flush=True)