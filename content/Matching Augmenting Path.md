---
title: "Matching Augmenting Path"
---

# Definition
Suppose $G$ is an [[Undirected Graph]] and $M \subset E(G)$ is a [[Matching]] on $G$. Suppose $P$ is an $M$-[[Matching Alternating Path|Alternating Path]] on $G$ of length $n \in \mathbb{N}$ from $u \in V(G)$ to $v \in V(G)$. Then $P$ is an $M$-[[Matching Augmenting Path|augmenting path]] if $u$ and $v$ are both $M$-[[Matching Exposed|exposed]].

## Remarks
1. [[Augmenting Network Flow Paths for Bipartite Matching Flow Formulation are Matching Augmenting Paths]]
2. If $P = (e_{1}, \dots, e_{n})$ is an $M$-[[Matching Augmenting Path|augmenting path]], then $e_{1}, e_{n} \not\in M$. If $e_{1}$ was, then $u$ would be [[Matching Covered|covered]] by $M$. If $e_{n}$ was, then $v$ would be [[Matching Covered|covered]] by $M$. Thus $n$ is [[Odd Integer|odd]] and only $e_{2i} \in M$ for $i \in [\frac{n-1}{2}]$.

# Other Outlinks
- [[Natural Numbers]]
- [[Graph Edge]]
- [[Graph Vertex]]