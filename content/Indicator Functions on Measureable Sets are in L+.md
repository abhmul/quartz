---
title: "Indicator Functions on Measureable Sets are in L+"
---

# Statement
Let $(X, \mathcal{M})$ be a [[Measure Space]]. Suppose $A \in \mathcal{M}$ . Then $1_{A} \in L^{+}(\mathcal{M})$.

## Proof
[[Indicator Function]]s have by definition the [[Codomain]] $\{0, 1\}$, so they are non-negative. Thus, it suffices to check that $1_{A}$ is $\mathcal{M}$-[[Borel Measureable Function|measureable]]. Checking the definition of [[Measureable Function]] and recalling the form of a [[Sigma Algebra induced by an Indicator Function]]:
$$\sigma(1_{A}) = \{\emptyset, A, A^{C}, X\} \subset \mathcal{M}$$

since $A \in \mathcal{M}$. Thus $1_{A}$ is $\mathcal{M}$-measureable. $\blacksquare$

# Other Outlinks
- [[Real Numbers]]
- [[L-Plus Functions]]