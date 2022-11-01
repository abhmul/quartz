---

title: "Discrete Topology"

---
# Statement
Let $X$ be a [[Set]]. Then $\mathcal{P}(X)$ is a [[Topological Space|topology]] on $X$. It is known as the [[Discrete Topology]].

## Proof
1. $X, \emptyset$ in  $\mathcal{P}(X)$ because they are subsets of $X$.
2. $\mathcal{P}(X)$ is closed under [[Set Union]], because [[Set Union]]s of subsets are still subsets [[Set Union]]
3. $\mathcal{P}(X)$ is closed under [[Finite Set|finite]] [[Set Intersection]] because [[Set Intersection]] of subsets is still a subset.

$\blacksquare$

## Properties
1. Every subset of $X$ is [[Closed]]. This is because for any $A \subset X$, $A^{C}$ is also a subset of $X$, so $A^{C} \in \mathcal{P}(X)$.
2. By (1), every singleton [[Set]] is both [[Closed]] and [[Open]], so no [[Set]] with more than one element can be [[Connected]]. Thus the singletons are the [[Connected Component]]s and $X$ is [[Totally Disconnected]].
3. The [[Discrete Topology]] has a [[Topological Basis]] of singletons, $\mathcal{B} = \{\{x\} \in \mathcal{P}(X) : x \in X\}$. This is because each singleton is a subset of $X$, so it is [[Open]], and every subset $A \subset X$ can be written as $\bigcup\limits_{x \in A}\{x\}$.
4. The [[Discrete Topology]] is the *finest* possible [[Topological Space]]. It contains every other [[Topological Space]] on $X$. This is by definition, since a [[Topological Space|topology]] is a subset of $\mathcal{P}(X)$.

# Other Outlinks
- [[Power Set]].