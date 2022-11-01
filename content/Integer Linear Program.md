---
title: "Integer Linear Program"
---

# Definition
Suppose $n, m \in \mathbb{N}$, $\mathbf{b}, \mathbf{c} \in \mathbb{R}^{n}$, $A \in \mathbb{R}^{m \times n}$, $F \subset \mathbb{Z}$. Then the [[Constrained Optimization Program]] 

$$\begin{align*}
&&\max \mathbf{c}^{T} \mathbf{x}\\
&\text{s.t.}&A \mathbf{x} \leq \mathbf{b}\\
&&\mathbf{x} \in F
\end{align*}$$
is an [[Integer Linear Program]]

## Properties
1. An [[Integer Linear Program]] is just a [[Linear Program]] where the nonnegativity constraint is replaced with an [[Integer|integrality]] contraint.
2. [[Integer Linear Program|Integer Linear Programming]] is [[NP-Complete]].

# Other Outlinks
- [[Natural Numbers]]
- [[Real Numbers]]
- [[Matrix]]