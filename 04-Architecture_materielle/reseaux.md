## Reseaux et protocoles de routages, Partie 2

# Architecture matérielle

![Reading Time: 2 min](https://img.shields.io/badge/%E2%8C%9A%20Read%20Time-2%20min-red)
![Language: French](https://img.shields.io/badge/Language-French-blue)
![Topic: Network](https://img.shields.io/badge/Topic-Network-blueviolet)

## I. Routage

**Routeur** = relie plusieurs réseaux locaux, il possède une table de routage qui dit où envoyer les paquets de données (en fonction de l’adresse IP de destination).

Il existe 2 méthodes permettant de renseigner la table de routage d’un routeur :  
- le routage statique : "à la main", cette solution est seulement envisageable pour des très petits réseaux de réseaux.
- le routage dynamique : "automatique", on utilise des protocoles qui vont permettre de "découvrir" les différentes routes automatiquement pour remplir la table de routage.

Note : on peut représenter un réseau de réseaux par un graphe ([voir le cours sur les graphes](../03-Donnees_structurees-1/arbre-graphe-dijkstra.md)). Routeurs = sommets, liaisons = arête. Les algorithmes utilisés par les protocoles de routages sont donc des algorithmes issus de la théorie de graphes.

Les 2 protocoles au programme sont les protocoles RIP (Routing Information Protocol) et OSPF (Open Shortest Path First) : 
- protocole RIP : s'appuie sur l'algorithme de Bellman-Ford (algorithme qui permet de calculer les plus courts chemins dans un graphe). Le protocole RIP utilise le nombre de sauts comme métrique. Ce protocole est aujourd'hui très rarement utilisé dans les grandes infrastructures.  
- protocole OSPF : s'appuie sur l'algorithme de Dijkstra. Le protocole OSPF utilise le “coût” comme métrique (la notion de coût est directement liée au débit des liaisons entre les routeurs).

Note : il faut être capable d’identifier la route empruntée par un paquet suivant le protocole de routage utilisé (RIP ou OSPF).
