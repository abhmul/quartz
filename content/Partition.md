---
title: "Partition"
---

# Definition
Let $X$ be a [[Set]]. A [[Partition]] $\mathcal{S} \subset \mathcal{P}(X)$ of $X$ is a collection of [[Mutually Disjoint]] [[Nonempty]] subsets of $X$ that [[Set Cover|cover]]  $X$. That is:
1. $\emptyset \not\in \mathcal{S}$.
2. $\forall A, B \in \mathcal{S}$, either $A \cap B = \emptyset$ or $A = B$.
3. $\bigsqcup\limits_{A \in \mathcal{S}} A = X$.

# Remarks
- For condition (2), observe that the two possibilities are [[Mutually Exclusive]]. Since $\emptyset \not\in \mathcal{S}$, if $A, B \in \mathcal{S}$ and $A = B$, then $\exists x \in A \cap B$.
- Condition (2) can equivalently be written as $\forall A, B \in \mathcal{S} (A \cap B \neq \emptyset \Rightarrow A = B)$. This follows from the definition of [[Logical Implication]].
# Other Outlinks
- [[Power Set]]
- [[Empty Set]]