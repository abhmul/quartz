---
title: "Optimal Solution of Bounded Linear Program is at Vertex"
---

# Statement
Suppose $n, m \in \mathbb{N}$, $\mathbf{b}, \mathbf{c} \in \mathbb{R}^{n}$, $A \in \mathbb{R}^{m \times n}$. Consider the [[Linear Program]]
$$\begin{align*}
&&\max \mathbf{c}^{T} \mathbf{x}\\
&\text{s.t.}&A \mathbf{x} \leq \mathbf{b}\\
&&\mathbf{x} \geq 0
\end{align*}$$
Suppose there exists an optimum $\mathbf{x}^{*} \in \mathbb{R}^{n}$. Then there is a [[Polytope Vertex]] $\mathbf{v}^{*} \in P$ of the [[Polytope]] $P$ defined by $A \mathbf{x} \leq \mathbf{b}$ s.t. $\max \mathbf{c}^{T} \mathbf{v}^{*} = \max \mathbf{c}^{T} \mathbf{x}^{*}$. That is, $\mathbf{v}^{*}$ is an optimal solution.
## Proof
[[TODO]] - this requires [[Convex Set|convexity]] of the [[Polytope]] and [[Open Halfspace]]s. Alternatively, could use [[Optimal Solution Set of Linear Program is a Face of Constraint Polytope]].