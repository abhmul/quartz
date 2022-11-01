---

title: "Subset Relation"

---
# Definition 1
We say $A \subset B$ if $\forall t (t \in A \Rightarrow t \in B)$.

# Definition 2
Let $S$ be a [[Set]]. Then we can define the [[Order Relation]]  $\subset'$ over $\mathcal{P}(S)$ to be defined as $A \subset' B$ for $A, B \in \mathcal{P}(S)$ if $A \subset B$ in the sense of Definition 1.

## Remarks
1. This can be seen to be an [[Order Relation]] because
	1. $A = A$, so $A \subset A$ and thus $A \subset' A$.
	2. If $A \subset' B$ and $B \subset' A$, then we have $\forall t[(t \in A \Rightarrow t \in B) \wedge (t \in B \Rightarrow t \in A)]$. This means $\forall t [t \in A \Leftrightarrow t \in B]$, so by the [[Axiom of Extensionality]], $A = B$.
	3. If $A \subset' B$ and $B \subset' C$, then we have $\forall t[(t \in A \Rightarrow t \in B) \wedge (t \in B \Rightarrow t \in C)]$. Thus $\forall t[t \in A \Rightarrow t \in C]$ and there fore $A \subset' C$.
2. We overload the term $\subset$ with either the sense in Definition 1 or Definition 2 based on what we need it to do.