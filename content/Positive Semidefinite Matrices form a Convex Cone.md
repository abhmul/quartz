---
title: "Positive Semidefinite Matrices form a Convex Cone"
---

# Statement
Suppose $n \in \mathbb{N}$. Then $\mathbb{S}_{n}^{+}$ is a [[Convex Cone]] over $\mathbb{R}$.

## Proof
Suppose $X, Y \in \mathbb{S}_{n}^{+}$ and $a, b \geq 0$. Consider $Z = aX + bY$. For any $x \in \mathbb{R}^{n}$, we have that

$$\begin{align*}
x^{T}Z x &= x^{T}(aX + bY) x\\
&=a x^{T}X x + b x^{T} Y x\\
&\geq 0
\end{align*}$$

Since $X, Y \in \mathbb{S}_{n}^{+}$ and $a, b \geq 0$. $\blacksquare$

# Other Outlinks
- [[Positive Semidefinite Matrix]]
- [[Real Numbers]]