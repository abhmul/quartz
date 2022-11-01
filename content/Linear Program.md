---
title: "Linear Program"
---

[[TODO]] Build down deeper into general constrained optimization programs
# Definition
Suppose $n, m \in \mathbb{N}$, $\mathbf{b}, \mathbf{c} \in \mathbb{R}^{n}$, $A \in \mathbb{R}^{m \times n}$. Then the [[Constrained Optimization Program]] 

$$\begin{align*}
&&\max \mathbf{c}^{T} \mathbf{x}\\
&\text{s.t.}&A \mathbf{x} \leq \mathbf{b}\\
&&\mathbf{x} \geq 0
\end{align*}$$

## Properties
1. [[The Feasible Set of a Linear Program is a Convex Polytope]].
2. [[TODO]]:
	- Show equivalence between different forms
	- [[Dual Linear Program]]
3. [[Linear Program|Linear Programming]] is in [[Polynomial Time Solvable|P]]