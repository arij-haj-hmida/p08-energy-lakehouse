# Conventions de normalisation

## 1. Schéma normalisé
| Colonne | Source | Remarque |
|---|---|---|
| household_id | LCLid | pseudonymisé, aucune réidentification (NF06) |
| tariff_group | stdorToU | Std ou ToU |
| event_time | DateTime | tel que publié, sans correction |
| local_date | dérivé | partie date de event_time |
| half_hour_slot | dérivé | heure x 2 + (minute >= 30), de 0 à 47 |
| energy_kwh | KWH/hh | kWh par 30 min (espaces supprimés) |
| source_file | nom du CSV | traçabilité |
| quality_flag | calculé | ok, doublon, hors_grille, null, conflit |
| dataset_version | paramètre | v1-2files |
| run_id | paramètre | présent dans toutes les sorties |

## 2. Règles de robustesse
| Cas | Règle | Compteur |
|---|---|---|
| Valeur Null ou non numérique | Quarantaine, jamais convertie en 0 | NULL_VALUE |
| Horodatage hors grille (minute différente de 0/30 ou secondes non nulles) | Quarantaine | OFF_GRID |
| Date illisible | Quarantaine | BAD_DATE |
| Valeur négative ou supérieure au seuil (paramètre, 10 kWh/30 min proposé) | Quarantaine | OUT_OF_RANGE |
| Doublon identique (foyer, horodatage, valeur) | Une seule copie conservée | DUP_IDENTICAL |
| Doublon contradictoire | Rejet des deux lignes, quarantaine | CONFLICT |
| Zéro mesuré | Valeur valide | |
| Créneau sans relevé valide | Compté dans n_missing_slots, jamais 0 | |

Le seuil de 10 kWh/30 min dépasse le maximum observé (5,49) : à ajuster. Aucun conflit dans le lot : le test T03 utilisera un cas artificiel.

## 3. Temps et changement d'heure
- Les horodatages sont pris tels que publiés. Il y a toujours 48 créneaux par jour, y compris les 2013-03-31 et 2013-10-27 (constat de l'audit).
- Le sens de l'horodatage (début ou fin de créneau) et le fuseau ne sont pas documentés : limite à signaler dans le rapport.

## 4. Foyers à série partielle
Les foyers dont la série est coupée ou terminée tôt sont conservés et signalés. La complétude est mesurée par MR1 (n_valid_slots, n_missing_slots).

## 5. Tarifs
- Jointure exacte entre event_time et TariffDateTime. Calendrier : 2013-01-01 00:00 au 2013-12-31 23:30.
- ToU : prix selon le libellé. High 67,20, Normal 11,76, Low 3,99 p/kWh.
- Std : 14,228 p/kWh, appliqué uniquement aux horodatages couverts par le calendrier 2013. Hors de cette période, coût null (à confirmer avec l'enseignante).
- Coût (£) = kWh x prix (p/kWh) / 100. Pas de prix : coût null, jamais inventé.
- Les prix sont dans config/ (paramètres hors code, NF07).

## 6. Traçabilité et confidentialité
dataset_version, run_id et source_file figurent dans toutes les sorties. Seuls les identifiants techniques LCLid sont utilisés.
