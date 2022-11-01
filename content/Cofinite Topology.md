---

title: "Cofinite Topology"

---
# Definition
Let $S$ be a [[Set]]. The [[Cofinite Topology]] on $S$ is the [[Topological Space]] $$\tau := \{U \subset S : |U^{C}| < \infty \} \cup \{\emptyset\}$$
## Remarks
### Proof that this is a [[Topological Space]]
1. Since $S^{C} = \emptyset$ and $|\emptyset| = 0 < \infty$, $S \in \tau$. $\emptyset \in \tau$ by construction.
2. Suppose $\mathcal{U} \subset \tau$ is [[Nonempty]]. Then $|(\bigcup\limits_{U \in \mathcal{U} U )}^{C}| = |\bigcap\limits_{U \in \mathcal{U}} U^{C}| \leq |U_{0}^{C}| < \infty$ for arbitrary $U_{0} \in \mathcal{U}$. Thus $\bigcup\limits_{}\mathcal{U} \in \tau$.
3. Suppose $U, V \in \tau$. Then $|(U \cap V)^{C}| = |U^{C} \cup V^{C}| \leq |U^{C}| + |V^{C}| < \infty$. Thus $U \cap V \in \tau$. $\blacksquare$