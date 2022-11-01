---

title: "Assignment"

---
# Definition
Let $V = \{v_{0}, v_{1}, \dots\}$ be the [[Set]] of [[Variable Symbol]]s. Let $\mathcal{L}$ be a [[Language]] and $\mathcal{M}$ an $\mathcal{L}$-[[Language Structure|structure]]. An [[Assignment]] is a [[Function]] $\sigma : V \to M$ (where $M$ is the [[Universe]] of $\mathcal{M}$).

## Remarks
1. [[Assignment]] gives us a means to [[Term Evaluation|evaluate]] [[Term]]s. Suppose $\sigma$ is an [[Assignment]] and $t$ is an $\mathcal{L}$-[[Term]]. Then $t^{\mathcal{M}} [\sigma]$ is defined as 
	1. $c^\mathcal{M}$ if $t = c \in \mathcal{C}$.
	2. $\sigma(v_{i})$ if $t = v_{i}$, a [[Variable Symbol]].
	3. $f^\mathcal{M}(t_{1}^{\mathcal{M}}[\sigma], \dots t_{n_{f}}^{\mathcal{M}}[\sigma])$ if $t_{1}, \dots, t_{n_{f}}$ are [[Term]]s and $t = f(t_{1}, \dots, t_{n_{f}})$.
2. A useful notation is $\sigma[\frac{a}{v}]$ defined as $$\sigma\left[\frac{a}{v}\right](v_{i})= \begin{cases} a & \text{if } v_{i} = v \\ v & \text{otherwise }  \end{cases}.$$ This will be helpful when we want to override the the assignment of a [[Variable Symbol]] because it is a [[Bound Variable]]