---

title: "Intersection of Vector Subspaces is a Vector Subspace"

---
# Statement
Let $V$ be a [[Vector Space]] over [[Field]] $F$ and let $\{W_{\alpha} \subset V\}_{\alpha \in A}$ be a [[Set|collection]] of [[Vector Subspace]]s of $V$. Then $\bigcap\limits_{\alpha \in A} W_{\alpha}$ is a [[Vector Subspace]] of $V$.

## Proof
Let $\mathbf{a}, \mathbf{b} \in \bigcap\limits_{\alpha \in A} W_{\alpha}$ and let $c \in F$. Then $c \mathbf{a} + \mathbf{b} \in W_{\alpha}$ $\forall \alpha \in A$ since [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]], so we have that $c \mathbf{a} + \mathbf{b} \in \bigcap\limits_{\alpha \in A} W_\alpha$. Because [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]], we see $\bigcap\limits_{\alpha \in A} W_\alpha$ is a [[Vector Subspace]] of $V$. $\blacksquare$

## Remarks
1. [[Intersection of Structures is still a Structure]].