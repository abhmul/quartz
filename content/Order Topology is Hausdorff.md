---

title: "Order Topology is Hausdorff"

---
# Statement
Let $(X, \leq)$ be a [[Total Ordering]] with the [[Order Topology]]. Then $X$ is [[Hausdorff]].

## Proof
We break into cases on $X$.

1. $|X| = 1$: Then $X$ is vacuously [[Hausdorff]]. $\checkmark$
2. $|X| > 1$. Let $x,y \in X$ so that $x < y$. 
	1. Suppose there exists $a \in (x,y)$. Then $x \in ( \leftarrow, a)$, $y \in (a, \rightarrow)$ and $( \leftarrow, a) \cap (a, \rightarrow) = \emptyset$. $\checkmark$
	2. Suppose $(x,y) = \emptyset$. Then $x \in ( \leftarrow, y)$, $y \in (x, \rightarrow)$ and $( \leftarrow, y) \cap (x, \rightarrow) = (x,y) = \emptyset$.
	Thus $X$ is [[Hausdorff]]. $\checkmark$

$\blacksquare$