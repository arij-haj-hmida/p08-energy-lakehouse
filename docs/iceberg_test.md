# Test minimal Apache Iceberg avec Hive 4.0.0
Réalisé par Nour le 09/11/2026 (tâche 2.4). Docker Desktop 4.34.2, moteur 27.2.0.

## Résultat
Test réussi : une table Iceberg a été créée, remplie, lue, et ses snapshots ont été interrogés en SQL avec Hive 4.0.0. La lecture d'un ancien snapshot fonctionne.

## Environnement
| Élément | Valeur | Vérification |
|---|---|---|
| Image | apache/hive:4.0.0 | docker pull, 2,77 Go |
| Hadoop embarqué | 3.3.6 | fichier hadoop-common-3.3.6.jar dans /opt/hadoop |
| Java embarqué | OpenJDK 1.8.0_342 | java -version dans l'image |
| Support Iceberg | hive-iceberg-handler-4.0.0.jar | présent dans /opt/hive/lib |
| Service | HiveServer2, métastore embarqué (Derby d'après la documentation) | variable SERVICE_NAME=hiveserver2 |

## Commandes
```
docker run -d --name hive4-test -p 10000:10000 -p 10002:10002 -e SERVICE_NAME=hiveserver2 apache/hive:4.0.0
docker exec -it hive4-test beeline -u "jdbc:hive2://localhost:10000/"
docker rm -f hive4-test
```
Les requêtes SQL sont dans sql/00_iceberg_smoke_test.sql.

## Observations
- La création de la table avec STORED BY ICEBERG a pris 3,2 secondes.
- Les INSERT s'exécutent avec Tez : 2 lignes (662 octets), puis 1 ligne (total 3 lignes, 2 fichiers, 1312 octets).
- La table default.t_test.snapshots montre un premier snapshot (opération append, parent NULL, 2 enregistrements), puis un second dont le parent est le premier (3 enregistrements au total).
- Les fichiers de métadonnées sont sous file:/opt/hive/data/warehouse/t_test/metadata/.
- La lecture FOR SYSTEM_VERSION AS OF avec le premier snapshot (8850418074684856975) renvoie 2 lignes, avec le second (8436382604393357982) 3 lignes.

## Erreurs rencontrées
| Requête | Message | Correction |
|---|---|---|
| SELECT * FROM t_test.snapshots | Table not found 'snapshots' | Préfixer par la base : default.t_test.snapshots |
| FOR SYSTEM_VERSION AS OF suivi d'un texte entre chevrons | ParseException | Mettre le numéro réel du snapshot |

## Limites et points ouverts
- Les fichiers sont dans le système de fichiers du conteneur et pas dans HDFS. Le conteneur a été supprimé : la table n'existe plus. Pour le projet, il faut un volume Docker ou HDFS.
- La commande SET hive.vectorized.execution.enabled=false a été exécutée avant le test. La raison n'a pas été notée : refaire le test sans cette ligne pour savoir si elle est nécessaire.
- Les messages de Tez mentionnent un cluster YARN alors qu'aucun cluster n'était démarré : à clarifier.
- La lecture de données HDFS par une table externe, puis INSERT SELECT vers Iceberg, n'a pas été testée.
- Hive embarque un client Hadoop 3.3.6, alors que le cluster prévu est en 3.4.1 : compatibilité à vérifier.

## Décision proposée
Retenir Hive 4.0.0 comme moteur SQL Iceberg, sous réserve des points ouverts. Spark SQL reste le plan de secours.
