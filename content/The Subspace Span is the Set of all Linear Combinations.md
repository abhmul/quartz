---

title: "The Subspace Span is the Set of all Linear Combinations"

---
# Statement
Let $V$ be a [[Vector Space]] on [[Field]] $F$. Let $S \subset V$. Then
$$\{c_{1} \mathbf{x}_{1} + \cdots + c_{n} \mathbf{x}_{n} \in V : n  \in \mathbb{Z}_{\geq 0}; \mathbf{x}_{1}, \dots, \mathbf{x}_{n} \in S; c_{1}, \dots, c_{n} \in F\} = \text{span} S$$

## Proof
Let $W = \{c_{1} \mathbf{x}_{1} + \cdots + c_{n} \mathbf{x}_{n} \in V : n  \in \mathbb{Z}_{\geq 0}; \mathbf{x}_{1}, \dots, \mathbf{x}_{n} \in S; c_{1}, \dots, c_{n} \in F\}$.

First recall that the [[Subspace Span]] is a [[Vector Subspace]]. For any $n \in \mathbb{N}$, $\mathbf{x}_{1}, \dots, \mathbf{x}_{n} \in S$, $c_{1}, \dots, c_{n} \in F$, we have that $\mathbf{x}_{1}, \dots, \mathbf{x}_{n} \in \text{span}S$ since $S \subset \text{span}S$. Since [[A Subset of a Vector Space is a Subspace iff it contains all its Linear Combinations]], we see that $c_{1} \mathbf{x}_{1} + \cdots + c_{n} \mathbf{x}_{n} \in \text{span} S$ and $W \subset \text{span} S$. $\checkmark$

On the other hand, we will show that $W$ is a [[Vector Subspace]], in which case $W \supset S$ ($1 * \mathbf{x}$ is a [[Linear Combination]] for $\mathbf{x} \in S$). Thus, by definition of [[Subspace Span]], $\text{span} S \subset W$. Together with above, we get $\text{span} S = W$. To that end, let $\mathbf{u}, \mathbf{v} \in W$ and let $a \in F$. Then there exist $n, m \in \mathbb{Z}_{\geq 0}$, $\mathbf{x}_{1}, \dots, \mathbf{x}_{n}, \mathbf{y}_{1}, \dots, \mathbf{y}_{m} \in S; c_{1}, \dots, c_{n}, d_{1}, \dots, d_{m} \in F$ so that
$$\begin{align*}
a \mathbf{u} + \mathbf{v} &= a \sum\limits_{i=1}^{n} c_{i} \mathbf{x}_{i} + \sum\limits_{j=1}^{m} d_{j} \mathbf{y}_{j}\\
&=ac_{1}\mathbf{x}_{1} + \dots + ac_{n}\mathbf{x}_{n} + d_{1} \mathbf{y}_{1} + \dots + d_{m} \mathbf{y}_{m}\\
&\in W.
\end{align*}$$
[[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]], so $W$ is a [[Vector Subspace]], completing the proof. $\checkmark$ $\blacksquare$

## Remarks
1. This works as a general alternate definition to [[Subspace Span]].