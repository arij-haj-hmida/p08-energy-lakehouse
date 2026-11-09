-- Test minimal Iceberg avec Hive 4.0.0 (commandes executees le 09/11/2026).
-- Lancement : docker exec -it hive4-test beeline -u "jdbc:hive2://localhost:10000/"
SET hive.vectorized.execution.enabled=false;
CREATE TABLE t_test (id INT, kwh DOUBLE) STORED BY ICEBERG;
INSERT INTO t_test VALUES (1, 12.5), (2, 7.3);
SELECT * FROM t_test;
SELECT * FROM default.t_test.snapshots;
INSERT INTO t_test VALUES (3, 5.1);
SELECT * FROM default.t_test.snapshots;
SELECT * FROM default.t_test.history;
-- Lecture d'un ancien etat : remplacer par un snapshot_id reel de la table snapshots.
-- SELECT * FROM t_test FOR SYSTEM_VERSION AS OF 8850418074684856975;