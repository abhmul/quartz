---
title: "The Feasible Set of a Linear Program is a Convex Polytope"
---

# Statement
Suppose $n, m \in \mathbb{N}$, $\mathbf{b}, \mathbf{c} \in \mathbb{R}^{n}$, $A \in \mathbb{R}^{m \times n}$ define the [[Linear Program]]
$$\begin{align*}
&&\max \mathbf{c}^{T} \mathbf{x}\\
&\text{s.t.}&A \mathbf{x} \leq \mathbf{b}\\
&&\mathbf{x} \geq 0
\end{align*}$$

Then the [[Feasible Set]] of this [[Linear Program]] is a [[Convex Polytope]].
## Proof
$A \mathbf{x} \leq \mathbf{b}$ is a system of [[Closed Halfspace]]s $\blacksquare$