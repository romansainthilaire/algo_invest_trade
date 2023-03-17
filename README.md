# AlgoInvest&Trade

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Ce projet a été réalisé dans le cadre de la formation OpenClassrooms *Développeur d'application - Python*.

→ Résolution d'un problème algorithmique.

## Présentation du projet

L'objectif est de maximiser le profit d'un client qui souhaite acheter des actions.

Les règles sont les suivantes :
- Chaque action ne peut être achetée qu'une seule fois.
- Il est impossible d'acheter une fraction d'action.
- Le client peut dépenser au maximum 500 euros.

Deux algorithmes peuvent être utilisés :
- *bruteforce.py* : teste toutes les combinaisons d'achats possibles et affiche la combinaison optimale.
- *optimized.py* : détermine et affiche la combinaison d'achats jugée optimale.

Attention : le script *bruteforce.py* ne fonctionne qu'avec un nombre d'actions limité (≤ 20).

## Fichiers csv
- Les actions doivent être stockées dans un fichier csv.
- L'emplacement du fichier csv doit être le même que celui du script exécuté.
- Le fichier csv doit inclure 3 colonnes : nom de l'action, prix en euros et rendement en %.
- Le nom du fichier csv doit être spécifié dans le code.
