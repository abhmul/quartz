---

title: "A point is a Limit Point iff it is a Net Limit"

---
# Definition
Let $X$ be a [[Topological Space]] and let $S \subset X$. Then $x \in X$ is a [[Limit Point]] of $S$ [[If and Only If]] there exists a [[Net]] $\{x_{\alpha}\}_{\alpha \in A} \subset S$ such that $x_{\alpha}\to x$.

## Proof
$(\Rightarrow)$ Suppose $x \in X$ is a [[Limit Point]] of $S$. Consider the [[Set|collection]] $A := \{U \subset X: U \text{ is open}, x \in U\}$. Then observe $A$ is a [[Directed Partial Ordering]] when ordered by [[Reverse Ordering|reverse]] [[Subset Relation]] since If $U, V \in A$, then $U \cap V \ni x$ and is [[Open]], so $U \cap V \in A$. By definition of [[Set Intersection]], $U \cap V \subset U, V$, so $U \cap V \geq U, V$. Since $x$ is a [[Limit Point]], for each $U \in A$, there exists $x_{U} \in U \cap S$. We will show that the [[Net]] $\{x_{U}\}_{U \in A} \subset S$ [[Net Convergence|converges]] to $x$. Observe that for any [[Open]] $V \subset X$ so that $V \ni x$, every $U \geq V$ (that is $U \subset V$) has $x_{U} \in U \subset V$.  Thus $\lim\limits_{U \in A}x_{U} = x$ and we have a [[Net]] that [[Net Convergence|converges]] to the [[Limit Point]] $x$ $\checkmark$.

$(\Leftarrow)$: Suppose $x \in X$ is a [[Net Convergence|limit]] of [[Net]] $\{x_{\alpha}\}_{\alpha \in A} \subset S$. Let $U \subset X$ so that $x \in U$. Then there exists some $\alpha_{0} \in A$ so that $x_{\alpha_{0}} \in U$. Since $x_{\alpha_{0}} \in S$ already, we have $x_{\alpha_{0}} \in U \cap S$. Thus $x$ is a [[Limit Point]] of $S$ $\checkmark$. $\blacksquare$