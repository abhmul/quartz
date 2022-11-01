---
title: "A Convex Cone is a Convex Set"
---

# Statement
Let $V$ be a [[Vector Space]] on $\mathbb{R}$ and let $S \subset V$ be a [[Convex Cone]]. Then $S$ is a [[Convex Set]].

## Proof
Suppose $\mathbf{u}, \mathbf{v} \in S$ and $a \in [0, 1]$. If $a = 0$ or $a = 1$ we have that $a \mathbf{u} + (1-a) \mathbf{v} \in \{u, v\} \subset S$. Otherwise $a \in (0,1)$ so $a > 0$ and $1-a > 0$. Because $S$ is a [[Convex Cone]], we have that $a \mathbf{u} + (1-a) \mathbf{v} \in S$. Thus $S$ is a [[Convex Set]]. $\blacksquare$