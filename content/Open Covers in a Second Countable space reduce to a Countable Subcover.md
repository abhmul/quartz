---

title: "Open Covers in a Second Countable space reduce to a Countable Subcover"

---
# Statement
Let $X$ be a [[Topological Space]] that is [[Second Countable]]. Let $S \subset X$ and let $\mathcal{U} := \{U_\alpha\}_{\alpha \in I}$ be an [[Open Cover]] of $S$. Then there exists a [[Countable]] [[Open Subcover]] $\mathcal{V} \subset \mathcal{U}$ of $S$.

## Proof
We first prove the result for $X$, then carry it over to $S$ through the [[Subspace Topology]]. Let $\mathcal{U}:= \{U_\alpha\}_{\alpha \in I}$ be an [[Open Cover]] for $X$. Since $X$ is [[Second Countable]], there exists a [[Countable]] [[Topological Basis]] $\mathcal{B}$ of $X$. For each $\alpha \in I$, for each $x \in U_\alpha$, let $B_{\alpha}^{(x)} \in \mathcal{B}$ be such that $x \in B_{\alpha}^{(x)} \subset U_\alpha$. Now consider $$\mathcal{B}' := \{B_\alpha^{(x)} : \alpha \in I, x \in U_{\alpha\}}\subset \mathcal{B}.$$First note that $\mathcal{B}'$ is an [[Open Cover]] for $X$, since $\forall x \in X$, there is some $\alpha \in I$ so that $x \in U_\alpha$. Also, it is [[Countable]] since $\mathcal{B}$ is [[Countable]].

We use $\mathcal{B}'$ to construct our [[Countable]] [[Open Subcover]] $\mathcal{V}$. For each $B \in \mathcal{B}'$, choose $\beta \in I$ so that $U_{\beta} \supset B$. Such a $\beta$ exists by construction of $\mathcal{B}'$. Denote this sub-[[Index Set]] $J \subset I$ and set $\mathcal{V} := \{U_{\beta}\}_{\beta \in J}$. Then, for all $x \in X$
1. There exists $B \in \mathcal{B}'$ so that $x \in B$, since $\mathcal{B}'$ is an [[Open Cover]] of $X$.
2. There exists $U \in \mathcal{V}$ so that $U \supset B$, by construction of $\mathcal{V}$. Thus $x \in U$.

Therefore, $\mathcal{V} \subset \mathcal{U}$ is an [[Open Subcover]]. Since we only made one choice per $B \in \mathcal{B}'$, $\mathcal{V} \preccurlyeq \mathcal{B}'$ and $\mathcal{V}$ is [[Countable]]. 

Now we carry the result over to an $S \subset X$. Suppose $\mathcal{U}$ is an [[Open Cover]] of $S$. Endow $S$ with the [[Subspace Topology]]. Since [[Subspace Topology inherits Second Countability]], and $S \cap \mathcal{U}$ is an [[Open Cover]] in $S$, we can reduce to a [[Countable]] [[Open Subcover]] $\mathcal{V}_{S}$. Then, for each $V_{S}\in \mathcal{V}_{S} \subset S \cap \mathcal{U}$ there exists a $V \in \mathcal{U}$ so that $V_{S} = S \cap V$. Thus $\mathcal{V}_{S}$ induces a $\mathcal{V} \subset \mathcal{U}$ so that $$S = \bigcup\limits_{V \in \mathcal{V}} V \cap S \subset \bigcup\limits_{V \in \mathcal{V}}V$$
so $\mathcal{V}$ is an [[Open Subcover]] of $S$ in $X$. Since $\mathcal{V}_{S}$ was [[Countable]], $\mathcal{V}$ is as well. $\blacksquare$

# Other Outlinks
- [[Surjection]]
- [[Set Cardinality]]
