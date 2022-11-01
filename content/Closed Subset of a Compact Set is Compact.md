---

title: "Closed Subset of a Compact Set is Compact"

---
# Statement
Let $X$ be a [[Topological Space]]. Suppose $S \subset X$ is [[Compact]] and $K \subset S$ is [[Closed]]. Then $K$ is [[Compact]].

## Proof
Let $\mathcal{U} := \{U_\alpha\}_{\alpha \in I}$ be an [[Open Cover]] for $K$. Since $K^{C}$ is [[Open]], then we have that $K^{C} \cup \mathcal{U}$ is an [[Open Cover]] for $X$, and thus an [[Open Cover]] for $S$. Since $S$ is [[Compact]], we can reduce this [[Open Cover]] to a [[Finite Set|finite]] [[Open Subcover]] $\{V_{i}\}_{i=1}^{n}$ for some $n \in \mathbb{N}$. Taking $\{V_{i}\}_{i=1}^{n} \setminus \{K^{C}\}$, we get a [[Finite Set|finite]] [[Open Subcover]] of $\mathcal{U}$, proving that $K$ is [[Compact]]. $\blacksquare$

# Other Outlinks
- [[Natural Numbers]]