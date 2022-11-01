---

title: "Equivalent Conditions for Local Compactness of Hausdorff Spaces"

---
# Statement
Let $X$ be a [[Hausdorff]] [[Topological Space]]. Then [[The following are Equivalent]]:
1. $X$ is [[Locally Compact]].
2. Each $p \in X$ has a [[Precompact]] [[Open|neighborhood]].
3. $X$ has a [[Topological Basis]] of [[Precompact]] [[Set]]s.

## Proof
$(1 \Rightarrow 2)$: Let $p \in X$. Since $X$ is [[Locally Compact]], there exists [[Open]] $U \subset X$ so that $p \in U$ and $U \subset K$ for some [[Compact]] $K \subset X$. Since $X$ is [[Hausdorff]], we know $K$ is [[Closed]] because [[Compact Sets in Hausdorff Spaces are Closed]]. Then, by definition of [[Closure]], $\text{cl}U \subset K$. Recall, [[Closed Subset of a Compact Set is Compact]], so $U$ is [[Precompact]]. $\checkmark$

$(2 \Rightarrow 3)$: For each $p \in X$, let $U_{p} \subset X$ be a [[Precompact]] [[Open|neighborhood]] of $p \in X$. Consider the [[Set|collection]]:
$$\mathcal{B} := \{U_{p} \cap V : p \in X, V \subset X\text{ open}\}.$$
$\mathcal{B}$ is a [[Set|collection]] of [[Open]] [[Set]]s, because [[Finite Set|finite]] [[Set Intersection]] of [[Open]] sets is [[Open]]. $\mathcal{B}$ is also a collection of [[Precompact]] sets because for each $B \in \mathcal{B}$, there exists $p \in X$ so that
$B \subset U_{p}$. Since $U_{p}$ is [[Precompact]], we see $B$ is [[Precompact]] as well because [[Subset of a Precompact Set is Precompact]]. Finally, we show $\mathcal{B}$ is a [[Topological Basis]] for $X$. Suppose $V \subset X$ is [[Open]]. Then for each $p \in V$, $U_{p} \cap V \in \mathcal{B}$. Then we have
$$\bigcup\limits_{p \in V} U_{p} \cap V = (\bigcup\limits_{p \in V}U_{p}) \cap V = V.$$
Therefore, $\mathcal{B}$ is a [[Topological Basis]] for $X$. $\checkmark$

$(3 \Rightarrow 1)$: Let $p \in X$ and let $\mathcal{B}$ be a [[Topological Basis]] of [[Precompact]] sets. Since $p \in X$ and $X$ is [[Open]], there must be some $B \in \mathcal{B}$ such that $p \in B$. Because $B$ is [[Precompact]], $B \subset \text{cl}B$, which is [[Compact]]. By definition of [[Topological Basis]], $B$ is [[Open]]. Thus $X$ is [[Locally Compact]]. $\checkmark$ $\blacksquare$

## Encounters
1. [[Lee - Introduction to Smooth Manifolds]] - Exercise A.55
2. 