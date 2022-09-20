# Commandes SQL

SQLite nous a permis de gérer des bases de données en SQL.

## Commantaires en SQL

| Commande   |       Usages |
| :--------- | -----------: |
| `-- text`  |  Commentaire |

## Gérer la base de données

| Commande                    |                  Usages |
| :-------------------------- | ----------------------: |
| `CREATE DATABASE db_name`   |  Créer une base de données |
| `DROP DATABASE db_name`     |  Supprimer une base de données |
| `CREATE TABLE table_name`   |  Créer une table dans la base de données |
| `TRUNCATE TABLE table_name` |  Supprimer toutes les données d'une table |

## Gérer des données

| Commande                                              |                  Usages |
| :---------------------------------------------------- | ----------------------: |
| `SELECT [DISTINCT] data [AS alias] FROM table`        |  Affiche ou Selectionne |
| `INSERT INTO table VALUES ('value1', 'value2', ...)`  |        Insère des ligne |
| `UPDATE table SET column = 'value'`                   |       Change des valeur |
| `DELETE FROM table`                                   |       Efface des valeur |

## Données sélectionnables

| Commande       |                Usages   |
| :------------- | ----------------------: |
| `*`            |      Toutes les données |
| `column`       |  Les valeurs d'un champ |
| `COUNT (data)` |    Le nombre de valeurs |
| `MIN (data)`   |   Le minimum de valeurs |
| `MAX (data)`   |  Le maximum des valeurs |
| `AVG (data)`   |  La moyenne des valeurs |
| `SUM (data)`   |    La somme des valeurs |

## Spécifications principales

| Commande                                |                                      Usages |
| :-------------------------------------- | ------------------------------------------: |
| `table1 JOIN table2 USING (common_key)` |                         Joindre deux tables |
| `WHERE condition`                       |                          Filtre des données |
| `ORDER BY column ASC / DESC`            |  Filtre des données (croissant/décroissant) |

## Comparer des valeurs

| Commande   |                                        Usages  |
| :--------- | ---------------------------------------------: |
| `<`        |               Comparer par infériorité stricte |
| `>`        |               Comparer par supériorité stricte |
| `<=`       |                 Comparer par infériorité large |
| `>=`       |                 Comparer par supériorité large |
| `=`        |                           Comparer par égalité |
| `LIKE`     |   Comparer par une chaîne de caractères modèle |
| `AND`      |  Vérifier que plusieurs conditions sont vraies |
| `OR`       |   Vérifier qu'au moins une condition est vraie |
