# Passation de la semaine 1 vers la semaine 2
Rédigée par Arij le 03/11/2026. Responsable de la semaine 2 : Nour.

## État
| Élément | État | Où |
|---|---|---|
| Dépôt et structure | fait | racine |
| Lot de données figé (v1-2files) | fait | docs/DATASET_CARD.md, docs/checksums.txt |
| Audit des données | fait | docs/audit.md |
| Conventions de normalisation | fait | docs/conventions.md |
| Architecture et diagramme | fait | docs/architecture.md |
| Tarifs 2013 convertis | fait | scripts/build_tariffs.py, config/tariffs.properties |
| Vérification du lot | fait | scripts/verify_setup.py |
| Cluster, HDFS, normalisation, test Iceberg | à faire | semaine 2 |

## Faits à connaître sur les données
- Lot : LCL-June2015v2_84.csv (Std, 43 foyers) et LCL-June2015v2_150.csv (ToU, 34 foyers), 1 000 000 de lignes chacun.
- Colonnes : LCLid, stdorToU, DateTime, KWH/hh (per half hour). Un espace précède chaque valeur kWh. La date a 7 décimales.
- Les valeurs Null sont toutes à un horodatage hors grille (34 sur 34 et 42 sur 42) ; les 8 lignes affichées par fichier datent du 2012-12-18 vers 15:22 : quarantaine.
- Les doublons sont des copies exactes à 00:00:00, environ une fois par mois : garder une copie.
- Il y a toujours 48 créneaux par jour, y compris aux changements d'heure.
- Les prix sont dans config/tariffs.properties. Le fichier data/processed/tariffs_2013.tsv se régénère avec scripts/build_tariffs.py.

## Versions
- Python 3.14.0, pandas 2.3.3, numpy 2.3.4, openpyxl 3.1.5.
- Hadoop, Hive et JDK : à choisir à la tâche 2.2.
- Vérifié dans les documentations : Hive 4 gère Iceberg nativement (STORED BY ICEBERG). Hive a une image officielle apache/hive. Hadoop 3.3 et plus fonctionne avec Java 8 et 11. Hadoop 3.5 et plus demande Java 17 côté serveur. Les tags réellement publiés sont à lire sur Docker Hub avant de figer.
- Le TP1 utilisait Hadoop 2.7.2 : ne pas réutiliser cette image. Reprendre seulement le modèle (un master et deux workers sur un réseau Docker dédié).

## Pièges rencontrés
- Sous cmd, certaines commandes ne sont pas reconnues (certutil, chcp) : utiliser le chemin complet dans le dossier System32 de Windows.
- Le Bloc-notes de Windows 11 ajoute des antislashs et des codes d'espace aux textes collés : nettoyer le fichier avant de l'envoyer.
- Git ignore data/, *.csv, *.zip et *.xlsx : renommer en .txt les sorties à versionner.
- La commande notepad rend la main tout de suite : fermer le Bloc-notes avant de lancer la commande suivante.
- Le PC d'Arij a 3,8 Go de RAM : le TP1 y a fait tourner un cluster Hadoop seul à la limite (WSL à 3,6 Go, 512 Mo par tâche, un reducer). Hive avec Tez n'y est pas testé : le cluster du projet tourne chez Nour.

## Tâches de la semaine 2 (Nour)
1. Vérifier Docker.
2. Choisir et figer les versions Hadoop et Hive.
3. Écrire le docker-compose.yml du cluster et lancer un WordCount.
4. Test minimal Iceberg avec Hive 4 : table jouet, insertion, lecture, snapshots.
5. Créer les zones HDFS et écrire scripts/load_hdfs.sh.
6. Job de normalisation avec compteurs et quarantaine.
7. Tableau des pertes dans docs/quality_report.md.
8. Compléter les sections Installation, Exécution et Reprise du README.
9. Écrire la passation vers la semaine 3.

## Points ouverts
- Réponse de Dr Gader sur le tarif plat Std de 14,228 p/kWh (toute la période ou seulement 2013).
- Choix entre Hive 4 et Spark SQL, après le test Iceberg.
