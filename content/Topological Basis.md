---
title: "Topological Basis"
---

# Definition
Let $X, \tau$ be a [[Topological Space]]. Then $\mathcal{B} \subset \tau$ is a [[Topological Basis]] for $X$ if 
$$\tau = \{\bigcup\limits_{B \in \mathcal{C}} B : \mathcal{C} \subset \mathcal{B}\}$$

## Remarks
1. Even if $\emptyset \not\in \mathcal{B}$, $\mathcal{B}$ can still be a [[Topological Basis]] because $\emptyset = \bigcup\limits_{B \in \emptyset} B$.
2. To show $\mathcal{B}$ is a [[Topological Basis]], it is sufficient to show the [[Set]]s are [[Open]] in $X$ and every [[Open]] $U \subset X$ can be written as a $U = \bigcup\limits_{B \in \mathcal{C}} B$ for some $\mathcal{C} \subset \mathcal{B}.$ The first criterion ensures $\mathcal{B} \subset \tau$, so $\tau(\mathcal{B}) \subset \tau$. The second criterion ensures $\tau(\mathcal{B}) \supset \tau$. 