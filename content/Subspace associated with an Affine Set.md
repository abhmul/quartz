---
title: "Subspace associated with an Affine Set"
---

# Statement
Let $V$ be a [[Vector Space]] over $\mathbb{R}$ and let $S \subset V$ be an [[Affine Set]]. Suppose $u \in S$. Then $$W = S - u = \{v - u : v \in S\}$$ is a [[Vector Subspace]] of $V$. Furthermore, $W$ does not depend on the choice of $u$.

## Proof
First we verify that $W$ is [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition|closed under scaling and addition]]. Let $x, y \in W$ and let $a \in \mathbb{R}$. Then there exist $v, w \in S$ so that $v = x + u$ and $w = y + u$. Then $$\begin{align*}
ax + y + u &= a(x + u) + (y + u) - au \in S\\
\end{align*}$$ since $a + 1 - a = 1$ and $x + u, y + u, u \in S$. Thus, by definition of $W$, $ax + y \in W$ and $W$ is a [[Vector Subspace]]. $\checkmark$

Now suppose $s \in S$ as well and that $U = S - s$. Suppose $p \in U$. Then $(p + s) - u \in W$. But $s - u \in W$ as well, thus $W \ni (p + s - u) - (s - u) = p$ and $U \subset W$. Repeating the argument with $U$ and $W$ swapped gets us that $U = W$. $\checkmark$ $\blacksquare$