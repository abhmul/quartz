---

title: "Dimension of a Vector Space upper bounds Linearly Independent Set sizee"

---
# Statement
Let $V$ be a [[Vector Space]] with [[Dimension of a Vector Space|dimension]] $\dim V = n$ for some $n \in \bar{\mathbb{N}}$. Then if $S \subset V$ s.t. $|S| > n$, $S$ is [[Linearly Dependent]].

## Proof
Suppose $\dim V = n$ for $n \in \mathbb{N}$. Then there exists a [[Vector Space Basis]] $\mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in V$. Since a [[Vector Space Basis]] is a [[Spanning Set|spanning set]], because [[Spanning Set Size bound Linearly Independent Set Size]], any [[Linearly Independent]] [[Set]] must have [[Set Cardinality|size]] less than or equal to $n$. But $|S| > n$, so it cannot be [[Linearly Independent]]. Therefore $S$ is [[Linearly Dependent]]. $\checkmark$

This is vacuously true for $\dim V = \infty$ since there does not exist $S \subset V$ such that $|S| > \infty$ 
(every [[Set]] is either [[Infinite Set|infinite]] or [[Finite Set|finite]]). $\checkmark$ $\blacksquare$

# Other Outlinks
- [[Set Cardinality]]
- 