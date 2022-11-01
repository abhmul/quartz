---
title: "Solution set of Linear Equations is an Affine Set"
---

# Statement
Let $V, W$ be a [[Vector Space]]s over $\mathbb{R}$, let $T \in \mathcal{L}(V, W)$, and let $b \in W$ define the [[Linear Equation System]]
$$T(x) = b.$$. Let $S = \{x \in V : T(x) = b\}$ be its [[Solution Set]]. Then $S$ is an [[Affine Set]].

## Proof
Let $\lambda \in \mathbb{R}$. Suppose $x_{1}, x_{2} \in S$. Then

$$\begin{align*}
T(\lambda x_{1} + (1 - \lambda) x_{2}) &= \lambda T(x_{1}) + (1 - \lambda)T(x_{2})\\
&=\lambda b + (1 - \lambda) b\\
&=b
\end{align*}$$
so $\lambda x_{1} + (1 - \lambda) x_{2} \in S$ and $S$ is an [[Affine Set]]. $\blacksquare$

[[TODO]] - Converse is true for $\mathbb{R}^{n}$ according to [[Boyd - Convex Optimization]] (Sect 2.1 pg 22, Example 2.1). Is this true in general?

# Other Outlinks
- [[Real Numbers]]
- [[Linear Operator]]
- [[Linear Equation]]