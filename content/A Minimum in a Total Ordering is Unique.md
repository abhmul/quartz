---
title: "A Minimum in a Total Ordering is Unique"
---

# Statement
Suppose $(T, \leq)$ is a [[Total Ordering]]. Let $A \subset T$. Then if $x \in A$ is a [[Minimum|minimal element]] of $A$, $x$ is the only [[Minimum]] of $A$.

# Proof
Let $x, x' \in A$ be [[Minimum|minimal elements]]. Since $T$ is a total ordering, we can compare $x$ and $x'$. Since $x$ is a [[Minimum]], we know $x \leq x'$. However $x'$ is also a [[Minimum]], so $x' \leq x$. By definition of an [[Order Relation]], we have that $x' = x$ and the [[Minimum]] is unique. $\blacksquare$