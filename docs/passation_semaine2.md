# Passation de la semaine 2 (brouillon, point d'étape 1)
Rédigée par Nour le 09/11/2026. Semaine terminée : non.

## État
| Tâche | État | Preuve |
|---|---|---|
| Ouverture du projet sur le PC de Nour | fait | lot conforme, audit identique |
| 2.1 Docker | fait | Docker 27.2.0, Compose 2.29.2, hello-world |
| 2.2 Versions | provisoire | apache/hive:4.0.0, apache/hadoop:3.4.1 |
| 2.4 Test Iceberg | fait | docs/iceberg_test.md |
| 2.3 Cluster Hadoop et WordCount | à faire | |
| 2.5 Zones HDFS et chargement | à faire | |
| 2.7 Normalisation | à faire | |
| 2.8 Tableau des pertes | à faire | |
| 2.9 README | en cours | tableau des versions |
| 2.10 Passation vers la semaine 3 | à faire | ce fichier |

## Versions vérifiées
| Image | Hadoop | Java |
|---|---|---|
| apache/hive:4.0.0 | 3.3.6 | OpenJDK 1.8.0_342 |
| apache/hadoop:3.4.1 | 3.4.1 | OpenJDK 1.8.0_212 |

## Pièges rencontrés
- Un texte copié depuis WhatsApp contient un préfixe avec l'heure et un numéro : il fait échouer la commande. Copier depuis la conversation avec Claude.
- Git n'est pas dans le PATH de cmd sur ce PC : ajouter son dossier cmd au PATH de la fenêtre.
- La commande python n'existe pas sur ce PC, il faut utiliser py.
- Docker a répondu Internal Server Error : quitter Docker Desktop, lancer wsl --shutdown, relancer Docker Desktop.
- Les tables de métadonnées Iceberg se lisent avec le nom de base : default.table.snapshots.
- Le texte collé dans le Bloc-notes peut perdre les barres de code et gagner des antislashs : toujours relire avec type avant de faire un commit.

## Points ouverts
- Comparer l'empreinte de data/processed/tariffs_2013.tsv avec celle d'Arij.
- Compatibilité du client Hadoop 3.3.6 de Hive avec un HDFS 3.4.1.
- Emplacement des tables Iceberg : volume Docker ou HDFS.
- Raison de la commande SET hive.vectorized.execution.enabled=false dans le test Iceberg.
- L'image takwabag/spark-hadoop:hv-2.7.2 (Hadoop 2.7.2) semble être celle du TP1 : trop ancienne pour le projet.
