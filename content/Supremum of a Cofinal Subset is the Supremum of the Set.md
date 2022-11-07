---

title: "Supremum of a Cofinal Subset is the Supremum of the Set"

---
# Statement
Let $(X, \leq)$ be a [[Total Ordering]] and let $A \subset X$. Let $S \subset A$ be a [[Cofinal Subset]]. If $\sup\limits S \in X$, then $\sup\limits A = \sup\limits S$.

## Proof
$\sup\limits S$ is an [[Upper Bound]] for $A$ since for every $a \in A$, there exists $b \in S$ so that $b \geq a$ ($S$ is a [[Cofinal Subset]] of $A$). Because $\sup\limits S \geq b$ for all $b \in S$, we have that $\sup\limits S \geq a$ for all $a \in A$. On the other hand, any [[Upper Bound]] for $A$ must also be an [[Upper Bound]] for $S$ since $S \subset A$. Thus, any [[Upper Bound]] for $A$ is at least $\sup\limits S$. This means $\sup\limits S$ is the [[Supremum|least upper bound]] of $A$ (i.e. $\sup\limits A = \sup\limits S$). $\blacksquare$

# Other Outlinks
- [[Supremum]]