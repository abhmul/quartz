---
title: "Sequence Limits are unique in Hausdorff Spaces"
---

# Statement
Suppose $(X, \tau)$ is a [[Hausdorff]]. Let $(x_n) \subset X$. Then if $x_{n} \to x \in X$ and $x_{n} \to y \in Y$, $x=y$.

## Proof 1
Suppose not. Then there exists a sequence $(x_n) \subset X$ so that $x_{n} \to x$ and $x_{n} \to y$ and $x \neq y$. Since $X$ is a [[Hausdorff]], there exists $U, V \subset X$ [[Open]] so that $x \in U$, $y \in V$, and $U \cap V = \emptyset$. Since $x_{n} \to x$, there exists $N \in \mathbb{N}$ so that $\forall n \geq N$, we have that $x_{n} \in U$. Likewise, since $x_{n} \to y$, there exists $M \in \mathbb{N}$ so that $\forall m \geq M$, we have that $x_{m} \in V$. Then $$U \cap V \supset \{x_n\}_{n=\max(M, N)}^{\infty}$$

[[Proof by Contradiction|Contradicting]] the [[Mutually Disjoint]]ness of $U$ and $V$. $\blacksquare$

## Proof 2
[[Net Limits are unique in Hausdorff Spaces]] and [[A Sequence is a Net]]. $\square$