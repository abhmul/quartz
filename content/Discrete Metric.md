---

title: "Discrete Metric"

---
# Statement
Let $S$ be a [[Set]]. The [[Function]] $d: S \times S \to \mathbb{R}_{\geq 0}$ defined
$$d(x, y) = \begin{cases} 1 & \text{if } x \neq y  \\ 0  & \text{otherwise} \end{cases}$$
is a [[Distance Function]]. It is known as the [[Discrete Metric]].

## Proof
We check the [[Axiom]]s of a [[Distance Function]]. 
1. By construction, if $x,y \in S$ so that $d(x, y) = 0$, then $x = y$.
2. If $x,y \in S$, then if $x = y$, $d(x,y) = d(x,x) = d(y,x)$. If $x \neq y$, then $d(x,y) = 1 = d(y,x)$.
3. Suppose $x, y, z \in S$. If $x=y=z$, then $d(x,z) = 0 = d(x,y) + d(y,z)$, so the [[Triangle Inequality]] holds. If either $x \neq y$ or $y \neq z$, then $$d(x,z) \leq 1 = \max\limits(d(x,y), d(y,z)) \leq d(x,y) + d(y,z).$$
Therefore $d$ is a [[Distance Function]].