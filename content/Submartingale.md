---

title: "Submartingale"

---
# Definition 1
Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a [[Probability Space]]. Let $X: \Omega \to \mathbb{R}^{T}$ be an [[Adapted Process]] wrt [[Filtration]] $\mathcal{F}_{*} := (\mathcal{B}_{t})_{t \in T}$  on $\Omega$. $X$ is a [[Supermartingale]] if it satisfies the following properties:
1. $X_{t} \in L^{1}(\Omega)$ $\forall t \in T$
2. $\mathbb{E}(X_{t} | \mathcal{B}_{r}) \geq X_{r}$ [[Almost Surely]] for any $r \leq t$.

## Properties
1. [[An Adapted Process is a Supermartingale iff its negative is a Submartingale]]
2. [[Expectations of a Submartingale are Non-Decreasing]]

# Definition 2
Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a [[Probability Space]]. Let $X: \Omega \to \mathbb{R}^{\mathbb{N}}$ be an [[Adapted Process]] wrt [[Filtration]] $\mathcal{F}_{*} := (\mathcal{B}_{n})_{n \in \mathbb{N}}$  on $\Omega$. $X$ is a [[Submartingale]] if it satisfies the following properties:
1. $X_{n} \in L^{1}(\Omega)$ $\forall n \in \mathbb{N}$,
2. $\mathbb{E}(X_{n+1} | \mathcal{B}_{n}) \geq X_{n}$ [[Almost Surely]] for any $n \in \mathbb{N}$.

## Remarks
1. Like in [[Martingale]], Definition (2) and (1) are equivalent. The proof is very similar, except we also require [[Conditional Expectation is Non-Decreasing]].