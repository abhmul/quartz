---
title: "A Simple Function Induces a Finite Sigma Algebra"
---

# Statement
Let $(Y, \mathcal{N})$ be a [[Measure Space]] and let $X$ be a [[Set]]. Suppose $f: X \to Y$ is a [[Simple Function]]. Then $\sigma(f)$ is a [[Finite Set]].

## Proof
Suppose $f$ is a [[Simple Function]]. Then $f(X) \subset Y$ is a [[Finite Set]]. Suppose $|f(X)| = n \in \mathbb{N}$. Let $E \in \mathcal{N}$ be a [[Measureable Set]]. Then
$$\begin{align*}
f^{-1}(E) &= f^{-1}(E) \cap X \\
&= f^{-1}(E) \cap f^{-1}(f(X))\\
&=f^{-1}(E \cap f(X))
\end{align*}$$
Since $E \cap f(X) \subset f(X)$ and $f(X)$ is finite, $E \cap f(X)$ has only $2^{n}$ possibilities. Thus, $|\sigma(f)| \leq 2^{n}$ and is thus a [[Finite Set]]. $\blacksquare$

# Other Outlinks
- [[Sigma Algebra induced by Function]]
- [[Function Image]]