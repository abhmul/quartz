---
title: "Induced Subgraph"
---

# Definition
Let $G = (V, E)$ be a [[Directed Graph]] or [[Undirected Graph]]. Let $A \subset V$. Then the [[Induced Subgraph|Subgraph induced by]] $A$, denoted $G[A]$, is $$G[A] = (A, E(A)),$$ where $E(A) = \{e \in E : e \text{ has both endpoints in }A\}$. That is, if
- $G$ is an [[Undirected Graph]], $E(A) = \{e \in E: e \cap A = e}$
- $G$ is a [[Directed Graph]], $E(A) = \{(u, v) \in E : \{u, v\} \cap A = \{u, v\}\}$