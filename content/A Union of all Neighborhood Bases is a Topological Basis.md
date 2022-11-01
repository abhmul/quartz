---
title: "A Union of all Neighborhood Bases is a Topological Basis"
---

# Statement
Suppose $(X, \tau)$ is a [[Topological Space]] and for each $x \in X$, $\mathcal{B}_{x}$ is a [[Neighborhood Basis]] for $x$. Then $$\mathcal{B} = \bigcup\limits_{x \in X} \mathcal{B}_{x}$$ is a [[Topological Basis]] for $X$.

## Proof
Suppose $U \subset X$ is [[Open]]. Then for each $x \in U$, there exists some $B_{x} \in \mathcal{B}_{x}$ so that $B_{x} \subset U$ (by definition of [[Neighborhood Basis]]). Thus

$$\bigcup\limits_{x \in U} B_{x} \subset U$$

On the other hand, for each $x \in U$, we have $x \in B_{x}$ since $B_{x}$ is in a [[Neighborhood Basis]] for $x$. Thus

$$U \subset \bigcup\limits_{x \in U} B_{x}$$

Therefore $U = \bigcup\limits_{x \in U} B_{x}$, completing the proof. $\blacksquare$