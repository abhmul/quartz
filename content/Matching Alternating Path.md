---
title: "Matching Alternating Path"
---

# Definition
Suppose $G$ is an [[Undirected Graph]] and $M \subset E(G)$ is a [[Matching]] on $G$. A [[Graph Path]] $P$ on $G$ from [[Graph Vertex|vertex]] $u \in V(G)$ to $v \in V(G)$ of length $n \in \mathbb{N}$ is an $M$-[[Matching Alternating Path|alternating path]] if its [[Graph Edge|edges]] are alternately in $P$. That is, $P$ is such that
1. $\forall i \in [n-1]$, if $e_{i} \in M$ then $e_{i+1} \not\in M$,
2. $\forall i \in [n-1]$, if $e_{i} \not\in M$ then $e_{i+1} \in M$.