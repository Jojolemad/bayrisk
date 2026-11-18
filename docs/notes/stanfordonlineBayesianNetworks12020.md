# Bayesian Networks 1 - Inference

Type : video |  Source : https://www.youtube.com/watch?v=U23yuPEACG0
Le : 18/11/2026

## Résumé

- Factor graphs + probabilities = baysian networks
- Baysian networks permettent de donner du sens aux factors

- Probabilities : 
    - Joint distribution: toutes les probas pour chaque cas différents P(S=s,R=r)
    - Marginal distribution: probas pour un sous cas (P(S=s))
    - Conditional distribution: (P(S | R=1 )) probas de S normalisée 
- Probabilisic inference: 
    - **Condition** on evidence
    - Interested in **query**
    - Some variables can be **marginalized out**
- Bayesian networks permettent de specify une joint distribution de manière efficace (sinon pour n variable il faut 2^n values pour completement spécifier la table)

- **Baysian Network**: Let $X = (X_1,...,X_n)$ be random varaibles. A **Bayesian network** is a directed acyclic graph (DAG) that specifies a joint distribution over $X$ as a product of local distributions, one for each node : $P(X_1=x_1,...,X_n=x_n) = \Pi \hspace{0.1cm} p(x_i|x_{parents(i)})$
    - **all factors satisfy $\sum p(x_i|x_{parents(i)}) = 1$ pour tous les x_parents**  --> pratique pour simplification dans la calcules
    - marginalization
    - local conditional distributions
    - **Inference**: given an evidence and a query, the goal is to compute the probability of the query variable conditionned on the evidence that you see
