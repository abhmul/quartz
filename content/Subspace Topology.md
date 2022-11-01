---

title: "Subspace Topology"

---
# Statement
Let $(X, \tau)$ be a [[Topological Space]] and let $S \subset X$. Then $(S, \tau \cap S)$, where $\tau \cap S := \{U \cap S \subset X : U \in \tau\}$, is a [[Topological Space]] on $S$.

## Proof
We show that $(S, \tau \cap S)$ is a [[Topological Space]]:
1. Since $\emptyset \in \tau$, $\emptyset \cap S = \emptyset \in \tau \cap S$. Since $X \in \tau$, $X \cap S = S \in \tau \cap S$.
2. Let $\mathcal{V} \subset \tau \cap S$. Then there exists $\mathcal{U} \subset \tau$ such that $\mathcal{V} = \{U \cap S \subset X: U \in \mathcal{U}\}$ and $$\bigcup\limits_{V \in \mathcal{V}} V = \bigcup\limits_{U \in \mathcal{U}} U \cap S = \left(\bigcup\limits_{U \in \mathcal{U}}U\right)  \cap S.$$ Since $\bigcup\limits_{U \in \mathcal{U}} \in \tau$, we have that $\bigcup\limits_{V \in \mathcal{V}}V \in \tau \cap S$.
3. Suppose $V_{1}, V_{2} \in \tau \cap S$. Then there exists $U_{1}, U_{2} \in \tau$ such that $V_{i} = U_{i} \cap S$ for $i \in [2]$. Then $$V_{1} \cap V_{2} = U_{1} \cap S \cap U_{2} \cap S = (U_{1} \cap U_{2}) \cap S.$$ Since $U_{1} \cap U_{2} \in \tau$, $V_{1} \cap V_{2} \in \tau \cap S$. $\blacksquare$

# Other Outlinks
- [[Subset Relation]]
- [[Open]]
