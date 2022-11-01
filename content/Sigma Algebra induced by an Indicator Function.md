---
title: "Sigma Algebra induced by an Indicator Function"
---

# Statement
Let $X$ be a [[Set]]. Let $A \in \mathcal{P}(X)$. Then $$\sigma(1_{A}) = \{\emptyset, A, A^{C}, X\}$$

## Proof
We must check that 
$$\sigma(1_{A}) = \{1_{A}^{-1}(E) : E \in \mathcal{B}(\mathbb{R}) \} = \{\emptyset, A, A^{C}, X\}$$

Suppose $E \in \mathcal{B}(\mathbb{R})$. Then there are 4 possiblities
1. $E \cap \{0, 1\} = \emptyset$: Then $1_{A}^{-1}(E) = \emptyset$.
2. $E \cap \{0, 1\} = \{0\}$: Then $1_{A}^{-1}(E) = A^{C}$.
3. $E \cap \{0, 1\} = \{1\}$: Then $1_{A}^{-1}(E) = A$.
4. $E \cap \{0, 1\} = \{0, 1\}$: Then $1_{A}^{-1}(E) = X$.

Since these are the only 4 possibilities, we have that 
$$\sigma(1_{A}) = \{1_{A}^{-1}(E) : E \in \mathcal{B}(\mathbb{R}) \} = \{\emptyset, A, A^{C}, X\}$$
$\blacksquare$

# Other Outlinks
- [[Sigma Algebra induced by Function]]
- [[Borel Sigma Algebra]]
- [[Real Numbers]]
- [[Power Set]]