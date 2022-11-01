---
title: "Finite Extremums get arbitrarily close"
---
# Statement 1
Suppose $X \subset \mathbb{R}$ and $X$ has an [[Upper Bound]]. Then for any $\epsilon > 0$, there exists $y \in X$ so that $\sup X - y < \epsilon$.

## Proof
Because $X$ has an [[Upper Bound]], the [[Completeness of the Real Numbers]] tells us that $\sup X < \infty$. Suppose there was some $\epsilon > 0$ so that $\forall y \in X$, $\sup X - y \geq \epsilon$. Then we have that $\forall y \in X$, 
$\sup X - \epsilon \geq y$, and thus $\sup X - \epsilon$  is an [[Upper Bound]] for $X$. But since $\sup X - \epsilon < \sup X$, this violates the definition of [[Supremum]], giving us a [[Proof by Contradiction|contradiction]]. $\blacksquare$

# Statement 2
Suppose $X \subset \mathbb{R}$ and $X$ has a [[Lower Bound]]. Then for any $\epsilon > 0$, there exists $y \in X$ so that $y - \inf X < \epsilon$.

## Proof
If $X$ has a [[Lower Bound]] then $-X = \{-x  \in \mathbb{R} : x \in X\}$ has an [[Upper Bound]]. By Statement 1, we have that for any $\epsilon > 0$, $\exists y \in X$,
$$\begin{align*}
\epsilon &> \sup (-X) - (-y)\\
&= -\inf X + y\\
&= y - \inf X
\end{align*}$$
establishing the result., since [[Supremum of Negative is Negative of Infimum]]. $\blacksquare$