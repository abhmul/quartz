---

title: "Cartesian Product"

---
# Definition 1
Let $A, B$ be [[Set]]s. The [[Cartesian Product]], denoted $A \times B$ is defined as the [[Set]] $$A \times B := \{(a, b) : a \in A, b \in B\}$$
## Proof of Existence
Consider $\mathcal{P}(\mathcal{P}(A \cup B))$. Observe that for $a \in A$ and $b \in B$, $$(a, b) = \{\{a\}, \{a, b\}\} \subset \mathcal{P}(A \cup B),$$ so $(a, b) \in \mathcal{P}(\mathcal{P}(A \cup B))$. Thus, by the [[Axiom Schema of Specification]] we can construct

$$\{(a, b) \subset \mathcal{P}(A \cup B) : a \in A \wedge b \in B \} = \{(a, b) : a \in A, b \in B\} := A \times B.$$
$\blacksquare$


