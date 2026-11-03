\# Fiche dataset : SmartMeter Energy Consumption Data in London Households



\## Source

\- Fournisseur : UK Power Networks (auteur et mainteneur), publié via le London Datastore

\- URL : https://data.london.gov.uk/dataset/smartmeter-energy-consumption-data-in-london-households-vqm0d

\- Contact : innovation@ukpowernetworks.co.uk

\- Date de consultation et de téléchargement : 03/11/2026

\- Période : novembre 2011 à février 2014, relevés toutes les 30 minutes

\- Licence : Creative Commons Attribution (attribution à UK Power Networks)



\## Ressources téléchargées

| Ressource | Nom d'origine | Taille |

|---|---|---|

| Archive découpée (168 CSV) | Partitioned LCL Data.zip | 758,86 Mo |

| Tarifs 2013 | Tariffs.xlsx | 239,63 ko |



Les CSV sont dans le dossier « Small LCL Data/ » du ZIP et se nomment LCL-June2015v2\_N.csv (N de 0 à 167).

Colonnes observées : LCLid, stdorToU, DateTime, KWH/hh (per half hour). Chaque fichier compte 1 000 001 lignes (en-tête inclus).



\## Lot retenu (figé)

\- dataset\_version : v1-2files

\- Fichiers : LCL-June2015v2\_84.csv (Std, 714 963 lignes en 2013) et LCL-June2015v2\_150.csv (ToU, 575 937 lignes en 2013)

\- Règle de sélection : scan de l'archive (docs/tou\_scan.txt). Les fichiers \_0 à \_133 ne contiennent aucune ligne ToU, \_134 est mixte, \_135 à \_167 sont ToU. Un fichier Std et un fichier ToU ont été retenus pour permettre la comparaison descriptive.

\- Limite : une série de foyer peut être coupée à la frontière entre deux fichiers (ex. MAC002690 s'arrête au 2013-07-16 dans \_150).

\- Réserve : \_0 (Std), hors lot, stocké dans data/raw/spare, pour l'élargissement de volume en S6.



\## Empreintes SHA-256

Voir docs/checksums.txt



\## Tarifs annoncés (à vérifier dans Tariffs.xlsx lors de l'audit)

\- dToU : High 67,20 p/kWh, Normal 11,76 p/kWh, Low 3,99 p/kWh

\- Std (tarif plat) : 14,228 p/kWh

\- Les tarifs dynamiques ne valent que pour les périodes et foyers documentés (2013).



\## Limites

\- Données historiques, pas de temps réel.

\- Les groupes Std et ToU ne sont pas interchangeables : le fichier Std et le fichier ToU contiennent des foyers différents, donc les comparaisons sont descriptives, sans effet causal.

