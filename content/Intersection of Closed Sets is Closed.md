---
title: "Intersection of Closed Sets is Closed"
---

# Statement
Suppose $(X, \tau)$ is a [[Topological Space]]. Suppose $\mathcal{K} \subset \mathcal{P}(X)$ is a collection of [[Closed|closed sets]] in $X$. Then $\bigcap\limits \mathcal{K}$ is [[Closed]] in $X$.

## Proof
This follows from [[De Morgan's Law]]. [[Index Set|Index]] $\mathcal{K}$ with $I$. That is, $\{K_{\alpha}\}_{\alpha \in I} = \mathcal{K}$. Then $K_{\alpha}^{C}$ is [[Open]] in $X$ since $K_{\alpha}$ is [[Closed]] for all $\alpha \in I$. Thus,

$$\begin{align*}
\Big( \bigcap\limits_{\alpha \in I} K_{\alpha} \Big)^{C} &= \bigcup\limits_{\alpha \in I} K_{\alpha}^{C} & \text{De Morgan's Law}\\
& \in \tau
\end{align*}$$

since $\tau$ is closed under [[Set Union|union]]s. Thus $\bigcap\limits_{\alpha \in I} K_\alpha$ is [[Closed]]. $\blacksquare$