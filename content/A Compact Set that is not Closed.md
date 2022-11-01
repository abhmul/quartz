---

title: "A Compact Set that is not Closed"

---
# [[Counterexample]]
Suppose $\mathbb{Z}$ is given the [[Cofinite Topology]]. Suppose $S \subset \mathbb{Z}$. Then $S$ is [[Compact]]. In particular there exists, $S \subset \mathbb{Z}$ that  is [[Compact]] but not [[Closed]].

## Proof
Let $\mathcal{U} = \{U_{\alpha}\}_{\alpha \in I}$ be an [[Open Cover]] for $S$. By definition of $\mathbb{Z}$, $|U_{\alpha}^{C}| < \infty$ for each $\alpha \in I$. Let $\alpha_{0} \in I$. Let $U_{\alpha_{0}}^{C} \cap S =: \{x_{i}\}_{i=1}^{n}$ for $n = |U_{\alpha_{0}}^{C} \cap S| < \infty$. Since $\mathcal{U}$ is an [[Open Cover]] of $S$, for each $i \in [n]$, there exists an $\alpha_{i} \in I$ so that $U_{\alpha_{i}} \ni x_{i}$.Thus, $\{U_{\alpha_{0}}, \dots, U_{\alpha_{n}}\}$ is a [[Finite Set|finite]] [[Open Subcover]] for $S$ and $S$ is [[Compact]]. 

Simply finding an $S \subset \mathbb{Z}$ that is not [[Closed]] will prove the second assertion. Recall $K \subset \mathbb{Z}$ is [[Closed]] [[If and Only If]] there is an [[Open]] $U \subset \mathbb{Z}$ s.t. $U^{C} = K$. Since $\mathbb{Z}$ has the [[Cofinite Topology]], $K$ must be a [[Finite Set]] or $\mathbb{Z}$ itself.  So $\mathbb{Z} \setminus \{0\}$ is not [[Closed]], but by above, it is [[Compact]].
$\blacksquare$