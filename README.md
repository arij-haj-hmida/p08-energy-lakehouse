# P08 - Analyse de la consommation énergétique (London Smart Meters)
Projet Big Data, Mastère 1 IA & DS, ISIMa, 2026/2027. Équipe : Arij, Nour, Nourhenne.

## 1. Contexte et objectifs
Chaîne HDFS, deux jobs Hadoop MapReduce Java (MR1, MR2) et Lakehouse Apache Iceberg à partir des relevés demi-horaires de compteurs intelligents de Londres. Architecture : docs/architecture.md.

## 2. Prérequis et versions
| Composant | Version | Vérification |
|---|---|---|
| Python | 3.14.0 (PC Arij), 3.13.16 (PC Nour) | py --version |
| pandas, numpy, openpyxl | 2.3.3, 2.3.4, 3.1.5 (requirements.txt) | utilisés pour l'audit |
| Docker Desktop | 4.34.2, moteur 27.2.0, Compose 2.29.2 | docker version |
| Hadoop (cluster) | apache/hadoop:3.4.1 (provisoire) | hadoop version dans le conteneur |
| Java | OpenJDK 1.8 dans les images Hive et Hadoop | java -version dans le conteneur |
| Maven | a renseigner | semaine 3 |
| Hive | apache/hive:4.0.0, Hadoop 3.3.6 embarqué | docs/iceberg_test.md |
| Iceberg | hive-iceberg-handler-4.0.0, test réussi | docs/iceberg_test.md |

## 3. Acquisition des données
- Source : SmartMeter Energy Consumption Data in London Households, UK Power Networks, London Datastore.
- URL : https://data.london.gov.uk/dataset/smartmeter-energy-consumption-data-in-london-households-vqm0d
- Licence : Creative Commons Attribution 4.0 (https://creativecommons.org/licenses/by/4.0/).
- Ressources : Partitioned LCL Data.zip (168 CSV) et Tariffs.xlsx, téléchargés le 03/11/2026.
- Lot figé : dataset_version v1-2files, fichiers LCL-June2015v2_84.csv (Std) et LCL-June2015v2_150.csv (ToU).
- Empreintes SHA-256 : docs/checksums.txt. Fiche complète : docs/DATASET_CARD.md.
- Les données ne sont pas dans le dépôt (dossier data/ ignoré par Git).

## 4. Installation
À compléter en semaine 2 : procédure Docker Compose depuis une machine vierge.

## 5. Exécution
À compléter : chargement HDFS, MR1, MR2, publication Iceberg.

## 6. Reprise après échec
À compléter : suppression du dossier de sortie, relance, vérification.

## 7. Tests
À compléter : tests Java (mvn test), jeux de test artificiels.

## 8. Structure du dépôt
| Dossier | Contenu |
|---|---|
| mr1/, mr2/ | Jobs MapReduce Java |
| scripts/ | Audit, scan, ingestion |
| tests/ | Tests |
| sql/ | Requêtes et DDL Iceberg |
| docs/ | Fiche dataset, audit, conventions, architecture |
| config/ | Paramètres (prix, seuils) |
| data_samples/ | Petits jeux de test artificiels |
| data/ | Données locales, ignorées par Git |

## 9. Licence et attribution
Données : UK Power Networks, publiées par le London Datastore sous licence CC BY 4.0.
