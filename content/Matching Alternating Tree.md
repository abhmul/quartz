---
title: "Matching Alternating Tree"
---

# Definition
Suppose $G$ is an [[Undirected Graph]] and $M$ is a [[Matching]] on $G$. Suppose $(T, r)$ is a [[Rooted Tree]] [[Subgraph]] of $G$. Then $(T, r)$ is an $M$-[[Matching Alternating Tree]] if
1. $r$ is [[Matching Exposed|exposed]] by $M$,
2. $\forall v \in T$, the [[Graph Path|Path]] from $v$ to $r$ on $T$ is an $M$-[[Matching Alternating Path|alternating path]].

## Remarks
1. We have two special [[Set]]s $A(T)$ and $B(T)$ associated with an $M$-[[Matching Alternating Tree|alternating tree]] defined as follows
	1. $A(T) = \{v \in T : d(r, v) \text{ is odd}\}$
	2. $B(T) = \{v \in T : d(r, v) \text{ is even}\}$
2. $|B(T)| = |A(T)| + 1$ since every $v \in T \setminus \{r\}$ is $M$-[[Matching Covered]], so we can pair up all [[Graph Vertex|vertices]] in $B(T)$ except $r$ with one in $A(T)$.

# Sources
- [[Cook - Combinatorial Optimization]] - Ch 5, Section 5.2, pg 135

# Other Outlinks
- [[Odd Integer]]
- [[Even Integer]]