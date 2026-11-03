import pandas as pd, glob

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)
pd.set_option("display.max_rows", 100)

DAYS = ["2012-10-28", "2013-03-31", "2013-10-27"]

for f in sorted(glob.glob("data/raw/meters/*.csv")):
    df = pd.read_csv(f, dtype=str, skipinitialspace=True)
    df.columns = ["id", "grp", "ts", "kwh"]
    df["val"] = pd.to_numeric(df["kwh"].str.strip(), errors="coerce")
    df["t"] = pd.to_datetime(df["ts"], errors="coerce")
    print("\n==========", f)

    nul = df[df["val"].isna()]
    odd = df[~df["t"].dt.minute.isin([0, 30])]
    print("\n-- Lignes Null :", len(nul), "| foyers :", nul["id"].nunique())
    print(nul[["id", "ts", "kwh"]].head(8).to_string())
    print("Minute hors 0/30 :", len(odd), "| dont Null :", odd.index.isin(nul.index).sum())
    print(odd[["id", "ts", "kwh"]].head(8).to_string())

    dup = df[df.duplicated(["id", "ts"], keep=False)]
    conf = dup.groupby(["id", "ts"])["kwh"].nunique()
    print("\n-- Doublons :", len(dup), "| foyers :", dup["id"].nunique(),
          "| groupes contradictoires :", (conf > 1).sum())
    print(dup["t"].dt.strftime("%Y-%m-%d").value_counts().head(10).to_string())
    print(dup.head(6)[["id", "ts", "kwh"]].to_string())

    cov = df.groupby("id", sort=False)["t"].agg(["min", "max", "count"])
    print("\n-- Couverture par foyer (ordre du fichier) :")
    print(cov.to_string())

    print("\n-- Jours de changement d'heure :")
    day_str = df["t"].dt.strftime("%Y-%m-%d")
    for day in DAYS:
        sub = df[day_str == day]
        if sub.empty:
            print(day, ": aucune ligne")
            continue
        raw = sub.groupby("id").size().value_counts().to_dict()
        uniq = sub.groupby("id")["ts"].nunique().value_counts().to_dict()
        print(day, "| lignes/foyer :", raw, "| horodatages uniques/foyer :", uniq)

t = pd.read_excel("data/raw/tariffs/tariffs.xlsx", sheet_name="Sheet1")
print("\n========== Tariffs")
print(t.shape, t["TariffDateTime"].min(), "->", t["TariffDateTime"].max())
print(t["Tariff"].value_counts(dropna=False).to_string())
print("Horodatages uniques :", t["TariffDateTime"].nunique())
print("Ecarts :", t["TariffDateTime"].sort_values().diff().dropna().value_counts().to_dict())
sub = t[t["TariffDateTime"].dt.strftime("%Y-%m-%d").isin(["2013-03-31", "2013-10-27"])]
print(sub.groupby(sub["TariffDateTime"].dt.strftime("%Y-%m-%d")).size().to_string())
h = t[t["Tariff"] == "High"]
print("Jours avec High :", h["TariffDateTime"].dt.date.nunique())
print("Heures High :", h["TariffDateTime"].dt.strftime("%H:%M").value_counts().sort_index().to_dict())