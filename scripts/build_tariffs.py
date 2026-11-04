import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "raw" / "tariffs" / "tariffs.xlsx"
CFG = ROOT / "config" / "tariffs.properties"
OUT = ROOT / "data" / "processed" / "tariffs_2013.tsv"


def read_prices(path):
    prices = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            prices[key.strip()] = float(value)
    return prices


prices = read_prices(CFG)
df = pd.read_excel(SRC, sheet_name="Sheet1")
df = df.rename(columns={"TariffDateTime": "tariff_time", "Tariff": "label"})
df["label"] = df["label"].astype(str).str.strip()

errors = []
if len(df) != 17520:
    errors.append("nombre de lignes inattendu : " + str(len(df)))
if df["tariff_time"].isna().any():
    errors.append("horodatage manquant")
if df["tariff_time"].duplicated().any():
    errors.append("horodatages dupliques")
steps = df["tariff_time"].sort_values().diff().dropna().value_counts()
if len(steps) != 1 or steps.index[0] != pd.Timedelta(minutes=30):
    errors.append("pas irregulier : " + str(steps.to_dict()))
unknown = set(df["label"]) - {"High", "Normal", "Low"}
if unknown:
    errors.append("libelles inconnus : " + str(unknown))
if errors:
    sys.exit("ERREUR : " + " ; ".join(errors))

df["price_p_per_kwh"] = df["label"].map(lambda x: prices["tou." + x])
df["tariff_time"] = df["tariff_time"].dt.strftime("%Y-%m-%d %H:%M:%S")
OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, sep="\t", index=False, lineterminator="\n")
print("OK :", len(df), "creneaux ecrits dans", OUT)
print(df["label"].value_counts().to_string())