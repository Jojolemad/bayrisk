# Titre

Type : vidéo  |  Source : [Lien](https://www.youtube.com/watch?v=dZoHsVO4F3k)

Le : 22/11/2026

## Résumé court

Explication pratique de l'algo de sampling de Gibbs,

méthode en simplifié ++ pour faire les calculs dans l'algo

Puis application sur un exemple simple.


## Détails
**Grandes lignes de l'Algorithme**
- Fix the values of observed variables 
- Set the values of all non-observed variables randomly
- Perform a random walk through the space of complete variable assignments. On each move:
    1. Pick a variable X 
    2. Calculate Pr(X=true | all other variables) 
    3. Set X to true with that probability
- Repeat many times. Frequency with which any variable X is true is it's posterior probability.


**Pour les calculs:**

How to calculate Pr(x=true | all other variables) ? \
Recall: a variable is independent of all others given it's Markov Blanket
- parents
- children
- other parents of children    

So problem becomes calculating Pr(X=true | MB(X)) 
- We solve this sub-problem exactly 
- Fortunately, it is easy to solve
$P(X) =\alpha P(X | Parents(X )) \; \Pi_{Y \in \: children(X)} \; P(Y | Parents(Y ))$
--> ie formule de Bayes


