---
title: "All Simple Functions can be Written in Standard Form"
---

# Statement
Let $\phi: X \to \mathbb{C}^{n}$ be a [[Simple Function]]. Let $F = \phi(X)$ (which is a [[Finite Set]]). Let $\{A_{i}\} = \{\phi^{-1}(\{a_{i}\}) \subset X : a_{i} \in F\}$. Then $\{A_{i}\}$ [[Partition]]s $X$ and we can write

$$\phi = \sum\limits_{i=1}^{|F|} a_{i}1_{A_{i}}$$
# Proof
To establish that $\{A_{i}\}$ partitions $X$, we show that
1. the collection is [[Mutually Disjoint]].
2. the [[Set Union|union]] of the collection is $X$.

This is all we need to show since $\{A_{i}\} \subset \mathcal{P}(X)$ by construction. To see (1) observe that for $i, j \in [|F|]$ s.t. $i \neq j$ we have that

$$\begin{align*}
A_{i} \cap A_{j} &= \phi^{-1}(\{a_{i}\}) \cap \phi^{-1}(\{a_{j}\})\\
&=\phi^{-1}(\{a_{i}\} \cap \{a_{j}\})\\
&= \phi^{-1}(\emptyset)\\
&= \emptyset
\end{align*}$$
[[TODO]] 

# Other Outlinks
- [[Complex Numbers]]
- [[Function Image]]
- [[Function Preimage]]
- [[Indicator Function]]
- [[Power Set]],
- [[Set Cardinality]]

# Encounters
1. [[Caliu - Deep Learning Architectures]] - Appendix, unknown page
2. [[Folland - Real Analysis]] - Ch 2, unknown page