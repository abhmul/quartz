---
title: "Continuous Functions Preserve Sequence Limits"
---

# Statement
Let $(X, \tau), (Y, \rho)$ be [[Topological Space]]s and suppose $f: X \to Y$ is [[Continuous Function]]. Suppose $(x_n) \subset X$. If $x_{n} \to x \in X$ , then $f(x_{n}) \to f(x) \in Y$.

## Proof 1
Suppose $V \subset Y$ is [[Open]] and $f(x) \in V$. Then $f^{-1}(V)$ is [[Open]] in $X$ and $x \in f^{-1}(V)$. Thus, there exists $N \in \mathbb{N}$ so that $\forall n \geq N$ we have that $x_{n} \in f^{-1}(V)$. Thus $\forall n \geq N$ we have  $f(x_{n}) \in V$. Since $V$ was arbitrary, $f(x_{n}) \to f(x)$. $\blacksquare$

## Proof 2
Follows by noting [[A Sequence is a Net]] and [[A Function is Continuous iff it preserves Net Convergence]]. $\blacksquare$

# Other Outlinks
- [[Sequence Convergence]]
