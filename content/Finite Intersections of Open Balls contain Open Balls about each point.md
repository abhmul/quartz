---
title: "Finite Intersections of Open Balls contain Open Balls about each point"
---

# Statement
Let $(M, d)$ be a [[Metric Space]]. Let $n \in \mathbb{N}$, $(x_{i})_{i=1}^{n} \subset M$, and $(\epsilon_{i})_{i=1}^{n} \subset [0, \infty)$. Then for each $y \in \bigcap\limits_{i \in [n]} B_{\epsilon_{i}}(x_{i})$, there exists $\zeta > 0$ so that $$B_{\zeta}(y) \subset \bigcap\limits_{i \in [n]} B_{\epsilon_{i}}(x_{i})$$

## Proof
We first show for two [[Open Ball]]s, then extend by [[Induction]]. Let $x, y \in M$ and let $\epsilon, \delta > 0$. Suppose $z \in B_\epsilon(x) \cap B_{\delta}(y)$. Then $d(x, z) < \epsilon$ and $d(y, z) < \delta$. Let $\zeta = \min(\epsilon - d(x, z), \delta - d(y, z))$. Then, if $w \in B_{\zeta}(z)$ then:
$$\begin{align*}
d(w, x) &\leq d(x, z)  + d(z, w)\\
&< d(x, z) + \zeta\\
&\leq d(x, z) + \epsilon - d(x, z)\\
&=\epsilon
\end{align*}$$
and $$\begin{align*}
d(w, y) &\leq d(y, z)  + d(z, w)\\
&< d(y, z) + \zeta\\
&\leq d(y, z) + \delta - d(y, z)\\
&=\delta
\end{align*}$$
Thus $w \in B_{\epsilon}(x) \cap B_{\delta}(y)$ and $B_{\zeta}(z) \subset B_{\epsilon}(x) \cap B_{\delta}(y)$.

[[TODO]] *make this more rigorous* Given $n$ [[Open Ball]]s and a point in their [[Set Intersection]], we can get an [[Open Ball]] around it that is contained in the first $n-1$ [[Open Ball]]s. Then we apply our argument above to find a smaller ball within its intersection with ball $n$. $\blacksquare$
	
	