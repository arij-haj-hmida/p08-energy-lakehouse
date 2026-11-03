\# Checklist des exigences P08



Équipe : Arij (données/HDFS, coordination), Nour (MR1, Iceberg), Nourhenne (MR2, dashboard)



\## Fonctionnelles

| Réf | Exigence | Responsable | Statut | Preuve |

|---|---|---|---|---|

| F01 | Télécharger et figer les ressources officielles | Arij | à faire | |

| F02 | Normaliser les relevés CSV | Arij | à faire | |

| F03 | Organiser les zones HDFS | Arij | à faire | |

| F04 | Exécuter MR1 Java | Nour | à faire | |

| F05 | Exécuter MR2 Java | Nourhenne | à faire | |

| F06 | Contrôler la qualité | Arij | à faire | |

| F07 | Publier une vraie couche Iceberg | Nour | à faire | |

| F08 | Produire les profils horaires | Nourhenne | à faire | |

| F09 | Analyser pics et tarifs | Nourhenne | à faire | |

| F10 | Justifier l'architecture | Arij | à faire | |

| F11 | Mesurer les performances | Nour | à faire | |

| F12 | Démontrer la chaîne complète | Arij | à faire | |



\## Non fonctionnelles

| Réf | Exigence | Responsable | Statut | Preuve |

|---|---|---|---|---|

| NF01 | Exactitude | Nour (MR1) / Nourhenne (MR2) | à faire | |

| NF02 | Performance (2 volumes) | Nour | à faire | |

| NF03 | Robustesse | Arij | à faire | |

| NF04 | Reproductibilité | Arij | à faire | |

| NF05 | Traçabilité | Arij | à faire | |

| NF06 | Confidentialité | Arij | à faire | |

| NF07 | Maintenabilité | Nourhenne | à faire | |

| NF08 | Disponibilité | Arij | à faire | |

| NF09 | Lakehouse (snapshots) | Nour | à faire | |



\## Tests

| Réf | Scénario | Responsable | Statut | Preuve |

|---|---|---|---|---|

| T01 | Parsing | Arij | à faire | |

| T02 | MR1 : journée de 48 mesures | Nour | à faire | |

| T03 | Doublons | Nour | à faire | |

| T04 | Lacune | Nour | à faire | |

| T05 | MR2 : deux jours, prix connu | Nourhenne | à faire | |

| T06 | Hors tarif | Nourhenne | à faire | |

| T07 | Iceberg | Nour | à faire | |

| T08 | Reproductibilité | Arij | à faire | |

| T09 | Volumétrie | Nour | à faire | |

| T10 | Visualisation | Nourhenne | à faire | |

