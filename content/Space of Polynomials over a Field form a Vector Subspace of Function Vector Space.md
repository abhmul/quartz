---
title: "Space of Polynomials over a Field form a Vector Subspace of Function Vector Space"
---


# Statement
Let $F$ be a [[Field]] and denote $$P[F] = \{x \mapsto \sum\limits_{k=0}^{n} c_{k}x^{k} : n \in \mathbb{Z}_{\geq 0}; c_{0}, \dots, c_{n}  \in F \}$$ the [[Set]] of all [[Polynomial]]s over $F$. Then $P[F]$ forms a [[Vector Subspace]] of the space $F^{F}$.

## Proof
We know from [[Functions to a Field form a Vector Space]] that $F^{F}$ forms a [[Vector Space]]. By [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]], it suffices to check we are closed under scaling and addition.

Suppose $c \in F$ and $p, r \in P[F]$. Then there exist $n, m \in \mathbb{Z}_{\geq 0}$ so that $$\begin{align*}
&p = c_{0} + c_{1} x + \cdots + c_{n} x^{n}\\
&r = d_{0} + d_{1} x + \cdots + d_{m} x^{m}\\
\end{align*}$$
[[Without Loss of Generality]] we can take $n \geq m$ and then rewrite $$r = d_{0} + d_{1} x + \cdots + d_{m} x^{m} + d_{m+1} x^{m+1} + \cdots d_{n} x^{n},$$ taking $d_{m+1}, \dots, d_{n} = 0$. Then we get that $$\begin{align*}
cp + r &= \sum\limits_{k=0}^{n}c c_{k}x^{k} + \sum\limits_{k=0}^{n} d_{k}x^{k}\\
&=\sum\limits_{k=0}^{n}(c c_{k} + d_{k})x^{k} \in P[F]
\end{align*}$$

$\blacksquare$

## Remarks
1. This also establishes that [[Polynomial]]s over a [[Field]] form a [[Vector Space]].