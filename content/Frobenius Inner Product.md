---
title: "Frobenius Inner Product"
---

# Statement
Let $n, m \in \mathbb{N}$. Then $$\langle A, B \rangle := \text{tr} (A^{T} B)$$. This defines an [[Inner Product]] on $\mathbb{R}^{n \times m}$.

## Proof
We need to establish that we indeed have an [[Inner Product]]. We check the conditions: [[TODO]]

## Properties
1. Observe that $\langle A, B \rangle = \text{tr} (A^{T} B) = \sum\limits_{j=1}^{m} A_{\cdot j} \cdot B_{\cdot j} = \sum\limits_{j=1}^{m} \sum\limits_{i=1}^{n} A_{ij} B_{ij}$, where $A_{\cdot j}$ denotes the $j$th column of $A$. This establishes that this [[Inner Product]] is just the [[Dot Product]] when $A$ and $B$ are rolled out into vectors of $\mathbb{R}^{nm}$.

# Other Outlinks
- [[Euclidean Space]]
- [[Natural Numbers]]
- [[Real Matrix Vector Space]]