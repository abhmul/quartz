---

title: "Net Limits are unique in Hausdorff Spaces"

---
# Statement
Let $X$ be [[Hausdorff]] and let $(x_{\alpha})_{\alpha \in A} \subset X$ be a [[Net]] that [[Net Convergence|converges]] to both $x,y \in X$. Then $x = y$.

## Proof
Suppose $x \neq y$. Since $X$ is [[Hausdorff]], there exists [[Open]] sets $U, V \subset X$ so that $x \in U$, $y \in V$ and $U \cap V = \emptyset$. Since $x_{\alpha} \to x$, there exists $\alpha_{0} \in A$ so that $\forall \alpha \geq \alpha_{0}$, $x_{\alpha} \in U$. Likewise, since $x_{\alpha}\to y$, there exists $\alpha_{1} \in A$ so that $\forall \alpha \geq \alpha_{1}$, $x_{\alpha} \in V$. Because $A$ is a [[Directed Partial Ordering]], there exists $\beta \geq \alpha_{0}, \alpha_{1}$. But then $x_{\beta} \in U$ and $x_{\beta} \in V$, so $U$ and $V$ are not [[Disjoint Sets]] $\unicode{x21af}$. Thus, by [[Proof by Contradiction|contradiction]], $x = y$. $\blacksquare$
