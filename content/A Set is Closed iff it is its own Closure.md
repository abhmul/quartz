---
title: "A Set is Closed iff it is its own Closure"
---

# Statement
Let $(X, \tau)$ be a [[Topological Space]]. Then $K \subset X$ is [[Closed]] [[If and Only If]] $\text{cl} K = K$.

## Proof
($\Rightarrow$) Suppose $K$ is [[Closed]]. A [[Closure]] is defined as

$$\text{cl} K = \bigcap\limits \{R : R \text{ is closed in } X, R \supset K\}$$

$K$ is one such [[Set]] in the [[Set Intersection|intersection]] so $\text{cl} K \subset K$. However, all sets in the intersection contain $K$ so $\text{cl} K \supset K$. Therefore $\text{cl} K = K$. $\checkmark$

($\Leftarrow$) Suppose $\text{cl} K = K$. Since $\text{cl} K$ is [[Closed]], we have that $K$ is [[Closed]]. $\checkmark$ $\blacksquare$

# Other Outlinks
