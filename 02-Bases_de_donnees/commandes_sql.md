# Commandes SQL

Vous trouverez ci-dessous une liste des commandes SQL usuelles.


## Commantaires en SQL

| Commande   |       Usages |
| :--------- | -----------: |
| `-- text`  |  Commentaire |


## Gérer des bases de données et des tables

| Commande                              |                                        Usages |
| :------------------------------------ | --------------------------------------------: |
| `CREATE DATABASE db_name`             |                      Crée une base de données |
| `DROP DATABASE db_name`               |                  Supprime une base de données |
| `CREATE TABLE table_name`             |        Crée une table dans la base de données |
| `ALTER TABLE table_name instruction`  |                             Modifie une table |
| `TRUNCATE TABLE table_name`           |       Supprime toutes les données d'une table |
| `DROP TABLE table_name`               |   Supprime une table dans une base de données |


## Gérer des données

| Commande                                              |                  Usages |
| :---------------------------------------------------- | ----------------------: |
| `SELECT [DISTINCT] data [AS alias] FROM table`        |  Affiche ou Sélectionne |
| `INSERT INTO table VALUES ('value1', 'value2', ...)`  |       Insère des lignes |
| `UPDATE table SET column = 'value'`                   |      Change des valeurs |
| `DELETE FROM table`                                   |      Efface des valeurs |


## Joindre des requêtes

| Commande          |                                  Usages |  Figuré  |
| :---------------- | --------------------------------------: | :------: |
| `UNION [ALL]`     |    Union de 2 ensembles [avec doublons] | Figuré 1 |
| `INTERSECT`       |             Intersection de 2 ensembles | Figuré 2 |
| `EXCEPT / MINUS`  |  Sélection d’un ensemble avec exception | Figuré 3 |


## Données sélectionnables

| Commande       |                  Usages |
| :------------- | ----------------------: |
| `*`            |      Toutes les données |
| `column`       |  Les valeurs d'un champ |
| `COUNT (data)` |   Le nombre des valeurs |
| `MIN (data)`   |   Le minimum de valeurs |
| `MAX (data)`   |  Le maximum des valeurs |
| `AVG (data)`   |  La moyenne des valeurs |
| `SUM (data)`   |    La somme des valeurs |


## Spécifications principales

| Commande                                  |                                                    Usages |
| :---------------------------------------- | --------------------------------------------------------: |
| `table1 JOIN table2 USING (column)`       |                  Joint deux tables avec une clé étrangère |
| `WHERE condition`                         |                          Filtre des données sans fonction |
| `GROUP BY column [WITH ROLLUP]`           |         Regroupe les données [ajoute une ligne de totaux] |
| `HAVING function(column) operator value`  |                     Filtre des données avec une fonctions |
| `ORDER BY column ASC / DESC`              |               Ordonne des données (croissant/décroissant) |
| `LIMIT count [OFFSET start]`              |  Limite le nombre de résultats [décalés de start valeurs] |

![Document illustratif des différentes jointures possibles](./resources/SQL_Joins.svg)
*Figuré : Les différentes jointures*

## Comparer des valeurs

| Commande                         |                                            Usages |
| :------------------------------- | ------------------------------------------------: |
| `<`                              |                   Compare par infériorité stricte |
| `>`                              |                   Compare par supériorité stricte |
| `<=`                             |                     Compare par infériorité large |
| `>=`                             |                     Compare par supériorité large |
| `<>`                             |                           Compare par non-égalité |
| `=`                              |                               Compare par égalité |
| `BETWEEN 'value1' AND 'value2'`  |      Vérifie qu'une valeur est dans un intervalle |
| `LIKE`                           |       Compare par une chaîne de caractères modèle |
| `AND`                            |      Vérifie que plusieurs conditions sont vraies |
| `OR`                             |       Vérifie qu'au moins une condition est vraie |
| `IN ('value1', 'value2', ...)`   |   Vérifie qu'une valeur est dans un set de donnée |
| `IS [NOT] NULL`                  |              Vérifie qu'une valeur est [non] NULL |


## Caractères génériques (utilisés avec `LIKE`)

| Commande  |                                   Usages |
| :-------- | ---------------------------------------: |
| `%`       |  Zéro, un ou plusieurs caractères jokers |
| `_`       |      Un seul caractère joker obligatoire |


## Les conditions

```sql
CASE column
    WHEN 1 THEN 'un'
    WHEN 2 THEN 'deux'
    WHEN 3 THEN 'trois'
    ELSE 'autre' 
END
``` 
*Figure : Conditions SI, SINON*
