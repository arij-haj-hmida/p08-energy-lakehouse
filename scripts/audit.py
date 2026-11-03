import pandas as pd, glob

for f in sorted(glob.glob("data/raw/meters/*.csv")):
    df = pd.read_csv(f, dtype=str, skipinitialspace=True)
    df.columns = [c.strip() for c in df.columns]
    id_col, grp_col, time_col, kwh_col = df.columns[:4]
    print("\n==", f, df.shape, list(df.columns))

    print("En-têtes répétés :", (df[id_col] == id_col).sum())
    d = df[df[id_col] != id_col].copy()

    raw = d[kwh_col]
    num = pd.to_numeric(raw.str.strip(), errors="coerce")
    print("Non numériques :", num.isna().sum(), raw[num.isna()].unique()[:5])
    print("Négatives :", (num < 0).sum(), "| Zéros :", (num == 0).sum(),
          "| Max kWh/30min :", num.max())

    t = pd.to_datetime(d[time_col], errors="coerce")
    print("Dates illisibles :", t.isna().sum(), "| plage :", t.min(), "->", t.max())
    print("Exemple brut :", d[time_col].iloc[0])
    print("Lignes en 2013 :", (t.dt.year == 2013).sum())
    print("Minutes hors 0/30 :", (~t.dt.minute.isin([0, 30])).sum())

    print("Doublons (foyer, heure) :", d.duplicated([id_col, time_col], keep=False).sum())
    print("Doublons exacts :", d.duplicated(keep=False).sum())

    print(d[grp_col].value_counts())
    print("Foyers :", d[id_col].nunique())
    cov = d.assign(t=t).groupby(id_col)["t"].agg(["min", "max", "count"])
    print(cov.describe())

x = pd.read_excel("data/raw/tariffs/tariffs.xlsx", sheet_name=None)
for name, sheet in x.items():
    print("\n== Tariffs / feuille :", name, sheet.shape)
    print(sheet.head(10))
    print(sheet.dtypes)