# Audit des données (lot v1-2files)
Scripts : scripts/audit.py, scripts/audit2.py. Sorties : docs/audit_output.txt, docs/audit2_output.txt.

## Synthèse
| Mesure | _150 (ToU) | _84 (Std) |
|---|---|---|
| Lignes de mesure | 1 000 000 | 1 000 000 |
| Foyers | 34 | 43 |
| Plage de dates | 2012-05-03 au 2014-02-28 | 2012-10-04 au 2014-02-28 |
| Lignes en 2013 | 575 937 | 714 963 |
| Valeurs Null | 34 | 42 |
| Négatives / zéros | 0 / 2 651 | 0 / 17 114 |
| Maximum (kWh/30 min) | 4,25 | 5,49 |
| Dates illisibles | 0 | 0 |
| Lignes en doublon | 1 386 | 1 394 |
| Doublons contradictoires | 0 | 0 |

## Observations
- Colonnes : LCLid, stdorToU, DateTime, KWH/hh (per half hour). Un espace précède chaque valeur kWh. Aucun en-tête répété dans ces deux fichiers.
- Les lignes Null sont toutes à minute hors 0/30 (34/34 et 42/42), datées du 2012-12-18 vers 15:22 (8 lignes affichées par fichier).
- Doublons : copies exactes à 00:00:00, environ une fois par mois.
- Changement d'heure : 48 horodatages uniques par foyer les 2013-03-31 et 2013-10-27 (49 lignes le 10-27 : doublon identique de minuit, vérifié pour MAC002534).
- Foyers dont la série est coupée : MAC002690 (fin 2013-07-16, dernier du fichier _150), MAC003499 et MAC003557 (bords de _84, non vérifié). Séries terminées avant la fin : MAC002634, MAC003554, MAC003507.
- Les deux groupes ne couvrent pas les mêmes foyers ni les mêmes dates de début.

## Tariffs.xlsx
- Feuille Sheet1 : 17 520 lignes, du 2013-01-01 00:00 au 2013-12-31 23:30, pas de 30 min, sans trou.
- Libellés : Normal 15 072, Low 1 660, High 788 (77 jours). Aucun prix dans le fichier.
- Prix (fiche officielle, consultée le 03/11/2026) : High 67,20, Normal 11,76, Low 3,99 p/kWh ; tarif plat 14,228 p/kWh.

## Limites
- Le sens de l'horodatage (début ou fin de créneau) et le fuseau ne sont pas documentés dans les fichiers.
- Deux fichiers seulement : le lot n'est pas représentatif de l'ensemble des foyers.
