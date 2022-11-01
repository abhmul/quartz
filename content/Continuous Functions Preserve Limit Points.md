---
title: "Continuous Functions Preserve Limit Points"
---

# Statement
Let $(X, \tau), (Y, \rho)$ be [[Topological Space]]s and suppose $f: X \to Y$ is [[Continuous Function]]. Suppose $S \subset X$. If $x \in X$ is a [[Limit Point]] of $S$, then $f(x)$ is a [[Limit Point]] of $f(S)$.

## Proof
Let $T = f(S)$ and $y = f(x)$. Suppose $V \subset Y$ is [[Open]] and $y \in V$. Then $f^{-1}(V)$ is [[Open]] ($f$ is [[Continuous Function]]) in $X$ and $x \in f^{-1}(V)$ since $f(x) = y \in V$. Since $x$ is a [[Limit Point]] of $S$, we know $f^{-1}(V) \cap S \neq \emptyset$. Thus there exists $z \in S$ so that $f(z) \in V$. Since $z \in S$, we also see $f(z) \in f(S) = T$. Thus $V \cap T \supset \{z\}$. Since $V$ was arbitrary, we have that $y$ is a [[Limit Point]] of $T$. $\blacksquare$

# Other Outlinks
- [[Function Image]]
- [[Function Preimage]]