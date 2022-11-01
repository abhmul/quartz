---

title: "Compact Sets are Separable from Points in a Hausdorff Space"

---
# Statement
Let $X$ be a [[Hausdorff]] [[Topological Space]]. Then if $K \subset X$ is [[Compact]] and $y \not\in X$, then there exists $U, V \subset X$ [[Open]] so that
1. $K \subset U$
2. $y \in V$
3. $U \cap V = \emptyset$

## Proof
Let $x \in K$. Because $X$ is [[Hausdorff]], there exists [[Open]] $U_{x}, V_{x} \subset X$ so that $x \in U_{x}, y \in V_{x}$ and $U_{x} \cap V_{x} = \emptyset$. $\{U_{x}\}_{x \in K}$ forms an [[Open Cover]] of $K$, so it can be reduced to a [[Finite Set|finite]] [[Open Subcover]] $\{U_{x_{i}}\}_{i=1}^{n}$ for some $n \in \mathbb{N}$. Take 
$$V = \bigcap\limits_{i=1}^{n}V_{x_{i}} \text{ and } U = \bigcup\limits_{i=1}^{n} U_{x_{i}}.$$Then, $V$ is [[Open]] since it is just the [[Finite Set|finite]] [[Set Intersection]] of [[Open|open sets]]. Because $y \in V_{x_{i}}$ for each $i \in [n]$, $y \in V$. $U$ is also [[Open]] since it is a [[Set Union]] of [[Open]] sets. Since $\{U_{x_{i}}\}_{i=1}^{n}$ is an [[Open Cover]] of $K$, $K \subset U$. For each $i \in [n]$, Since $U_{x_{i}} \cap V_{x_{i}} = \emptyset$, and $V \subset V_{x_{i}}$, so we have $U_{x_{i}} \cap V = \emptyset$. Then $V \cap \bigcup\limits_{i=1}^{n} U_{x_{i}} = V \cap U = \emptyset$ as desired. $\blacksquare$

# Other Outlinks
- [[Mutually Disjoint]]
- [[Empty Set]]
- [[Natural Numbers]]