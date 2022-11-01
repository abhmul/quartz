---
title: "Graph Deficiency"
---

# Definition
Let $G$ be an [[Undirected Graph]] and let $\mathcal{M} = \{M \subset E(G) : M \text{ is a Matching}\}$. Then the [[Graph Deficiency]] of $G$, denoted $\text{def}(G)$, is $$\text{def}(G) = \min \{|\{v \in V : v \text{ is exposed by }M\}| \leq |V(G)| : M \in \mathcal{M}\}$$
## Remarks
1. For [[Infinite Set]]s, $\text{def}(G)$ is [[Well-Defined]] because [[Cardinals form a Well-Ordering]].
2. If our $V(G)$ is a [[Finite Set]] (as is the case in most relevant cases), then $\text{def}(G) = |V(G)| - \nu(G)$.

# Other Outlinks
- [[Matching]]
- [[Graph Edge]]
- [[Matching Exposed]]