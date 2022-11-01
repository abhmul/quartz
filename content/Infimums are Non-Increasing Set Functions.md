---
title: "Infimums are Non-Increasing Set Functions"
---

# Statement
Let $(T, \leq)$ be a [[Total Ordering]] and suppose $A \subset B \subset T$ such that $\inf A$ and $\inf B$ both exist. Then $\inf A \geq \inf B$.

# Proof
Let $L_{A}$ be the [[Set]] of [[Lower Bound]]s for $A$ and let $L_{B}$ be likewise for $B$. Observe that if $x \in L_{B}$, then $x \leq b$ $\forall b \in B$. Since every $a \in A$ is also in $B$, we have that $x \leq a$ $\forall a \in A$. Thus $x$ is a [[Lower Bound]] for $A$ and $L_{B} \subset L_{A}$. Since $\inf A = \max L_{A}$ and $\inf B = \max L_{B}$, we know that
$$\inf A = \max L_{A} \geq \max L_{B} = \inf B$$
since [[Maximums are Non-Decreasing Set Functions]]. $\blacksquare$
# Other Outlinks
- [[Infimum]]
- [[Maximum]]