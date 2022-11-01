---

title: "Compact Sets in Hausdorff Spaces are Closed"

---
# Statement
Let $X$ be a [[Hausdorff]] [[Topological Space]]. Then if $K \subset X$ is [[Compact]], $K$ is [[Closed]].

## Proof
Let $x \in K^{C}$. Because [[Compact Sets are Separable from Points in a Hausdorff Space]], there exists [[Open]] $V_{x} \subset X$ such that $x \in V_{x}$ and $V_{x} \cap K = \emptyset$. That is, $V_{x} \subset K^{C}$. Then, we can create [[Open]]
$$V := \bigcup\limits_{x \in K^{C}}V_{x}$$
Since, for each $x \in K^{C}$, $V_{x} \subset K^{C}$, we see $V \subset K^{C}$. On the other hand, for each $x \in K^{C}, x \in V_{x}$, so $x \in V$. Thus $K^{C} \subset V$. Thus $K^{C} = V$. By definition of [[Closed]], $K$ is [[Closed]]. $\blacksquare$