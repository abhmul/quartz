---

title: "Martingale"

---
# Definition 1
Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a [[Probability Space]]. Let $X: \Omega \to \mathbb{R}^{T}$ be an [[Adapted Process]] wrt [[Filtration]] $\mathcal{F}_{*} := (\mathcal{B}_{t})_{t \in T}$  on $\Omega$. $X$ is a [[Martingale]] if it satisfies the following properties:
1. $X_{t} \in L^{1}(\Omega)$ $\forall t \in T$,
2. $\mathbb{E}(X_{t} | \mathcal{B}_{r}) = X_{r}$ [[Almost Surely]] for any $r \leq t$.

## Properties
1. [[Expectations of a Martingale are Constant]]

## Remarks
1. Defining property (2) is [[Conditioning on known information is Idempotent|already true]] when $r = t$, so really what matters is when $r < t$.

# Definition 2
[[A Martingale is a Supermartingale and a Submartingale]]

## Remark
1. This definition is equivalent to the first because property (2) of [[Supermartingale]]s and [[Submartingale]]s together implies property (2) of [[Martingale]]s.

# Definition 3
Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a [[Probability Space]]. Let $X: \Omega \to \mathbb{R}^{\mathbb{N}}$ be an [[Adapted Process]] wrt [[Filtration]] $\mathcal{F}_{*} := (\mathcal{B}_{n})_{n \in \mathbb{N}}$  on $\Omega$. $X$ is a [[Martingale]] if it satisfies the following properties:
1. $X_{n} \in L^{1}(\Omega)$ $\forall n \in \mathbb{N}$,
2. $\mathbb{E}(X_{n+1} | \mathcal{B}_{n}) = X_{n}$ [[Almost Surely]] for any $n \in \mathbb{N}$.

## Remarks
1. It is not hard to see that definition (3) is equivalent definition (1) in the case where $T = \mathbb{N}$. First note that $(3)$ is just a special case of $(1)$. We can establish that $(3) \Rightarrow (1)$ by [[Induction]]. First observe that for $n = 1$, the only $m \in \mathbb{N}$ s.t. $m \leq n$ is $m = 1$. Therefore, $\forall m \leq n$, we have that $\mathbb{E}(X_{n} | \mathcal{B}_{m}) = \mathbb{E}(X_{1} | \mathcal{B}_{1}) = X_{1}$ since [[Conditioning on known information is Idempotent]]. For the inductive step, suppose this claim holds for $n \in \mathbb{N}$. Consider $m \leq n+1$. Then we have that $$\mathbb{E}(X_{n+1} | \mathcal{B}_{m}) = \mathbb{E}(\mathbb{E}(X_{n+1} | \mathcal{B}_{n}) | \mathcal{B}_{m}) = \mathbb{E}(X_{n} | \mathcal{B}_{m}) = X_{m}$$ by induction. Note that the first equality holds because of [[Smoothing]]. $\blacksquare$