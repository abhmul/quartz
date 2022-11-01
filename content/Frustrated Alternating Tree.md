---
title: "Frustrated Alternating Tree"
---

# Definition
Suppose $G$ is an [[Undirected Graph]], $M$ is a [[Matching]] on $G$, and $(T, r)$ is an $M$-[[Matching Alternating Tree|alternating tree]]. We say $T$ is a [[Frustrated Alternating Tree]] if $\forall e \in E(G)$ s.t. $e \cap B(T) \neq \emptyset$, we have that $e \cap A(T) \neq \emptyset$. That is, each [[Graph Edge]] with a [[Graph Vertex|endpoint]] in $B(T)$ has its other endpoint in $A(T)$.

## Results
- [[If a Graph has a Frustrated Tree then it has no Perfect Matching]]