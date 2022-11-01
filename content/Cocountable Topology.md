---

title: "Cocountable Topology"

---
# Statement
Let $X$ be a [[Set]]. Then the [[Open]] sets $$\tau := \{U \subset X : U^{C} \text{ is countable}\} \cup \{X, \emptyset\}$$ make $X$ a [[Topological Space]]. This topology is known as the [[Cocountable Topology]].

## Proof
We simply need to check the [[Axiom]]s defining a [[Topological Space]].
1. By construction, $\{X, \emptyset\} \subset \tau$. $\checkmark$
2. Suppose $U, V \in \tau$. Then $$(U \cap V)^{C} = U^{C} \cup V^{C}$$ is [[Countable]] since [[A Union of Countable Sets is Countable]]. Thus $U \cap V \in \tau$.
3. Suppose $\{U_\alpha\}_{\alpha \in A} \subset \tau$. Then $$(\bigcup\limits_{\alpha \in A} U_{\alpha})^{C} = \bigcap\limits_{\alpha \in A} U_{\alpha}^{C} \subset U_{\alpha_{0}}^{C}$$ is [[Countable]] because $U_{\alpha_{0}}^{C}$ is [[Countable]] for some (really any) $\alpha_{0} \in A$ and [[Monotonicity of Cardinality]]. $\blacksquare$