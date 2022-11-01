---

title: "Dimension of a Vector Space lower bounds Spanning Set size"

---
# Statement
Let $V$ be a [[Vector Space]] with [[Dimension of a Vector Space|dimension]] $\dim V = n$ for some $n \in \bar{\mathbb{N}}$. Then if $S \subset V$ s.t. $|S| < n$, $\text{span} S \subsetneq V$.

## Proof
First suppose $V$ is a [[Finite-Dimensional Vector Space]] with $\dim V = n$ for some $n \in \mathbb{N}$. Since $\dim V = n$, there exists a [[Vector Space Basis]] $\mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in V$. Suppose $\text{span} S = V$. Then, because [[Spanning Set Size bound Linearly Independent Set Size]], any [[Linearly Independent]] [[Set]] must have [[Set Cardinality|size]] less than $n$. But since $\mathbf{a}_{1}, \dots, \mathbf{a}_{n}$ is  a [[Vector Space Basis]], it is [[Linearly Independent]] $\unicode{x21af}$. Therefore $\text{span} S \subsetneq V$. $\checkmark$

Now suppose $V$ is an [[Infinite-Dimensional Vector Space]]. Then if $S \subset V$ is s.t. $\text{span} S = V$, then we must have that $|S| = \infty$. Otherwise, because [[A Vector Space is Finite-Dimensional iff it has a Finite Spanning Set]], $V$ would be [[Finite-Dimensional Vector Space|finite-dimensional]], a [[Proof by Contradiction|contradiction]]. $\blacksquare$
# Other Outlinks
- [[Subspace Span]]
- [[Finite Set]]
- [[Extended Natural Numbers]]
- [[Infinite Set]]