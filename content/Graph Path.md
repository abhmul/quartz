---
title: "Graph Path"
---

# Definition 1
Let $G = (V, E)$ be a [[Directed Graph]]. A [[Graph Path]] of length $n \in \mathbb{N}$ from [[Graph Vertex|vertex]] $u \in V$ to $v \in V$ is a [[Tuple]] $(e_{1}, e_{2}, \dots, e_{n}) \in E^{n}$ so that 
1. $e_{1} = (u, x)$ for some $x \in V$
2. $e_{2} = (y, v)$ for some $y \in V$
3. $e_{i} = (x, y)$ and $e_{i+1} = (y, z)$ for some $x,y,z \in V$ for all $i \in [n]$

## Remarks
1. The [[Empty Tuple]] $()$ is a [[Graph Path]] from $v \in V$ to itself for all $v \in V$. It has length $0$.
2. Suppose $P$ is a [[Graph Path]] of length $n \in \mathbb{N}$ from $u \in V$ to $v \in V$. We let $V(P)$ signify the [[Tuple]] $(e_{1,1} = u, e_{2,1}, \dots, e_{n,1}, v) \subset V^{n+1}$.
# Definition 2
Let $G$ be an [[Undirected Graph]]. Then a [[Graph Path]] of length $n \in \mathbb{N}$ from from [[Graph Vertex|vertex]] $u \in V$ to $v \in V$ is a [[Graph Path]] of length $n \in \mathbb{N}$ on the [[Represent an Undirected Graph as a Directed Graph|Directed Graph representation]] of $G$.

# Other Outlinks
- [[Natural Numbers]]
- [[Graph Edge]]