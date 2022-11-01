---
title: "Infinite Pigeonhole"
---

# Statement
Let $X$ be an [[Infinite Set]]. Let $\bigsqcup\limits_{i \in [n]} A_{i} = X$ be a [[Finite Set|finite]] [[Partition]] of $X$ for $n \in \mathbb{N}$. Then $\exists j \in [n]$ s.t. $A_{j}$ is infinite.

# Proof
Suppose not. Then each $A_{i}$ is finite for $i \in [n]$. Denote $|A_{i}|= c_{i}$. Since $A_{i}$ are [[Mutually Disjoint]], we have that $\infty > \sum\limits_{i \in [n]} c_{i} = \big|\bigsqcup\limits_{i \in [n]} A_{i} \big|  = |X|$, [[Proof by Contradiction|contradicting]] our assumption that $X$ was infinite. $\blacksquare$

# Other Outlinks
- [[Cardinal Arithmetic]]