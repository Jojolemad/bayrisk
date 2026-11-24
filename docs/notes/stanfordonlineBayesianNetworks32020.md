# Bayesian Networks 3 - Maximum Likelihood

Type : vidéo  |  Source : [lien](https://www.youtube.com/watch?v=Fa-rr6AXMwg&list=PLoROMvodv4rO1NB9TD4iUZ3qghGEGtqNX&index=15)
Le : 24/11/2026

## Résumé court
Présentation apprentissage par la méthode Maximum Likelihood.
- supervised learning
- laplace smoothing
- unsupervisied learning



## Détails

- **Objective**: turn dataset $D$ to parameters (CPT)

- **parameter sharing**: The local conditional distributions of different variables use the same parameters.

General case algorithm:

```
Input: training examples Drain of full assignments
Output: parameters 0 = {pq : d € D}

Count:
    For each x € D_train: 
        For each variable x_i:
            Increment count_di(x_parents(i), x_i)
Normalize:
    For each d and local assignment x_parents(i):
        Set p_d(x_i | x_Parents(i)) = count_d (x_parents(i) , x_i)
```

- **Laplace smoothing**:

    For each distribution d and partial assignment (X_Parents(i),x_i), add $\lambda$ to count(x_Parents(i),x_i).
    
    Then normalize to get probability estimates.

    Larger $\lambda$ = more smoothing => probabilities closer to
uniform.

- **maximum marginal likelihood :** when there is missing data
    
    expectation maximisation algorithm :
    ```
    Intuition: generalization of the K-means algorithm
    Variables: H is hidden, E = e is observed
    Algorithm: 

    Initialize \theta (random, close to uniform)
    E-step:
     - Compute q(h) = P(H = h| E = e; \theta) for each h
        (using any inference algorthm --> gibbs sampling)
     - Create weighted points: (h, e) with weight q(h) 
    
    M-step:
     -  Compute maximum likelihood (just count and normalize) to get \theta
    Repeat until convergence.
    ```
