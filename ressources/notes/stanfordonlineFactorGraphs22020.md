# Factor Graphs 2 - Conditional Independence

Type : vido  |  Source : https://www.youtube.com/watch?v=o0mKSvbMunA&list=PLoROMvodv4rO1NB9TD4iUZ3qghGEGtqNX&index=12

Le : 17/11/2026

## Résumé
Idée principale abordée : indépendance et indépendance conditionnelle.
Deux variables sont **indépendantes** lorsqu'elles n'ont aucune influence directe ou indirecte l'une sur l'autre dans le graphe.


Conditionnllement indépendantes :
$A \perp B \mid C$
Si tous les chemins entre deux variables passent par une variable sur laquelle on conditionne, alors les deux variables deviennent indépendantes conditionnellement à cette variable.

Ca permet de simplifier les choses car on a besoin de moins de données au total.

Quelques méthodes pour permettre de simplifier les choses sont les suivantes : 
 - Conditioning :On fixe une variable à une valeur donnée.
 - Variable Elimination :on cherche la meilleure valeur possible d'une variable pour chaque configuration de ses voisines.
    - si on souhaite éliminer X_2 : $
g(X_1)=\max_{X_2}
f(X_1,X_2)$

