---
title: "Monotone Sequences converge to their Extremum"
---

# Statement
$(x_{n}) \subset \mathbb{R}$ be a [[Monotone Sequence]]. Let $t \in \bar{\mathbb{R}}$ be it's [[Extremum]] corresponding to the direction of the monotone sequence ( if [[Non-Increasing Function]] then [[Infimum]]; if [[Non-Decreasing Function]] then [[Supremum]]). Then $x_{n} \to t$.

# Proof
First suppose that $(x_{n})$ is [[Non-Decreasing Function]]. Observe that $t = \sup\{x_{n}\}$ exists in $\bar{\mathbb{R}}$ since either
1. $(x_{n})$ is bounded from above in $\mathbb{R}$: By [[Completeness of the Real Numbers]], we know $\sup\{x_{n}\} \in \mathbb{R}$.
2. $(x_{n})$ is not bounded from above in $\mathbb{R}$: $\infty$ is always an [[Upper Bound]]  (by definition), so $\sup\{x_{n}\}$ exists. Since no other element of $\bar{\mathbb{R}}$ is an [[Upper Bound]] (we're not bounded in $\mathbb{R}$ and $- \infty$ is less than every element in $\mathbb{R}$), $\infty$ is the only upper bound and thus the [[Supremum]].

First we prove the statement for when $t \in \mathbb{R}$. Now let $\epsilon > 0$. Then because [[Finite Extremums get arbitrarily close]], we know there exists $N \in \mathbb{N}$ so that $x_{N} > t - \epsilon$. Since $(x_{n})$ is non-decreasing and $t = \sup\{x_{n}\}$, we know for all $n \geq N$:
$$t \geq x_{n} \geq x_{N} > t - \epsilon$$
Thus, for all $n \geq N$:
$$|t - x_{n}| = t - x_{n} < \epsilon$$
We've satisfied the definition of [[Sequence Convergence]], so we have that $(x_{n}) \to t$.

Now suppose $t = \infty$. Then we know $(x_{n})$ has no [[Upper Bound]] in $\mathbb{R}$. In other words, $\forall M \in \mathbb{R}$, we know there exists $N \in \mathbb{N}$ so that $x_{N} > M$. Since $(x_{n})$ is [[Non-Decreasing Function]], we have that for all $n \geq N$
$$x_{n} \geq x_{N} > M$$
This satisfies the definition of [[Sequence Convergence to Infinity]], so $(x_{n}) \to \infty$ . 

Now consider when $(x_{n})$ is [[Non-Increasing Function]]. Then $\forall n > m \in \mathbb{N}$, we have that
$$x_{n} \leq x_{m}$$
Thus,
$$-x_{n} \geq -x_{m}$$
and $(-x_{n})$ is a [[Non-Decreasing Function]] sequence. By our proof above, we know

$$(-x_{n}) \to \sup\{-x_{n}\} = -\inf\{x_{n}\}$$
where the last equality follows because [[Supremum of Negative is Negative of Infimum]]. Since $x \mapsto -x$ is [[Continuous Function]], we know $(x_{n}) \to \inf\{x_{n}\}$. $\blacksquare$

# Other Outlinks
 - [[Real Numbers]]
 - [[Extended Real Numbers]]
 - [[Sequence Convergence]]