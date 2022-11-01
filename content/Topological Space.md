---
title: "Topological Space"
---

# Definition
Let $X$ be a [[Set]] and $\tau \subset \mathcal{P}(X)$. Then $(X, \tau)$ is a [[Topological Space]] if
1. $X, \emptyset \in \tau$.
2. Suppose $F \subset \tau$. Then $\bigcup\limits_{U \in F} U \in \tau$.
3. Suppose $G \subset \tau$ and $G$ is a [[Finite Set]]. Then $\bigcap\limits_{U \in G} U \in \tau$

## Alternate Definition
We could have instead started from [[Closed]] sets and defined a topology $\tau'$ in a corresponding way
1. $X, \emptyset \in \tau'$
2. Suppose $\mathcal{F} \subset \tau'$. Then $\bigcup\limits_{C \in \mathcal{F}} C \in \tau'$.
3. Suppose $\mathcal{G} \subset \tau'$ and $\mathcal{G}$ is a [[Finite Set]]. Then $\bigcap\limits_{C \in \mathcal{G}} C \in \tau'$

## Remarks
1. We can relax $(3)$ to a weaker condition $(3')$ of closure under pairwise [[Set Intersection]]s: For $U, V \in \tau$, $U \cap V \in \tau$. Clearly $(3) \Rightarrow (3')$. We see $(3') \Rightarrow (3)$ by [[Induction]]. $(3')$ is usually easier to prove when we're trying to establish some structure is a [[Topological Space]].
2. Condition $(1)$ is actually redundant. Note $\bigcup\limits_{U \in \emptyset} U = \emptyset$ and $\bigcap\limits_{U \in \emptyset} U = X$.
