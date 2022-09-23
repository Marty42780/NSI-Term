# Commandes SQL

Vous trouverez ci-dessous une liste des commandes SQL usuelles.


## Commantaires en SQL

| Commande   |       Usages |
| :--------- | -----------: |
| `-- text`  |  Commentaire |


## Gérer des bases de données et des tables

| Commande                              |                                        Usages |
| :------------------------------------ | --------------------------------------------: |
| `CREATE DATABASE db_name`             |                     Créer une base de données |
| `DROP DATABASE db_name`               |                 Supprimer une base de données |
| `CREATE TABLE table_name`             |       Créer une table dans la base de données |
| `ALTER TABLE table_name instruction`  |                            Modifier une table |
| `TRUNCATE TABLE table_name`           |      Supprimer toutes les données d'une table |
| `DROP TABLE table_name`               |  Supprimer une table dans une base de données |


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

| Commande                                  |                                             Usages |
| :---------------------------------------- | -------------------------------------------------: |
| `table1 JOIN table2 USING (common_key)`   |         Joindre deux tables avec une clé étrangère |
| `WHERE condition`                         |                   Filtre des données sans fonction |
| `GROUP BY column [WITH ROLLUP]`           |  Regroupe les données [ajoute une ligne de totaux] |
| `HAVING function(column) operator value`  |              Filtre des données avec une fonctions |
| `ORDER BY column ASC / DESC`              |        Ordonne des données (croissant/décroissant) |
| `LIMIT count`                             |                      Limite le nombre de résultats |


## Comparer des valeurs

| Commande                         |                                        Usages  |
| :------------------------------- | ---------------------------------------------: |
| `<`                              |               Comparer par infériorité stricte |
| `>`                              |               Comparer par supériorité stricte |
| `<=`                             |                 Comparer par infériorité large |
| `>=`                             |                 Comparer par supériorité large |
| `<>`                             |                       Comparer par non-égalité |
| `=`                              |                           Comparer par égalité |
| `LIKE`                           |   Comparer par une chaîne de caractères modèle |
| `AND`                            |  Vérifier que plusieurs conditions sont vraies |
| `OR`                             |   Vérifier qu'au moins une condition est vraie |
| `BETWEEN 'value1' AND 'value2'`  |  Vérifier qu'une valeur est dans un intervalle |
| `IS [NOT] NULL`                  |          Vérifier qu'une valeur est [non] NULL |


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