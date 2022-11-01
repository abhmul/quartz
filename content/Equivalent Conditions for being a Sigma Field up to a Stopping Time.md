---

title: "Equivalent Conditions for being a Sigma Field up to a Stopping Time"

---
# Statement
Let $\{\mathcal{B}_{n} : n \in \mathbb{N}\}$ be a [[Discrete-Time Filtration]] on $\Omega$ and let $\nu : \Omega \to \bar{\mathbb{N}}$. Then the following [[Sigma Algebra]]s are equal:
1. $\mathcal{B}_{\nu}$
2. $\{B \in \mathcal{B}_{\infty}: B \cap [\nu \leq n] \in \mathcal{B}_{n}\}$

## Proof
[[TODO]]. Use [[Equivalent Conditions for being a Stopping Time]]
## Remarks
1. It is not immediately clear that (2) is a [[Sigma Algebra]], but we know (1) is, so it suffices to show equivalence.
2. It is not in general true that if $B \in \mathcal{B}_\nu$, then $B \cap [\nu > n] \in B_{n}$. [[TODO]] what is an example of this? However, if $A \cap [\nu > n] \in \mathcal{B}_{n}$ for all $n \in \mathbb{N}$, then $(A^{C} \cap [\nu > n]) \sqcup (A \cap [\nu \leq n]) \in \mathcal{B}_{n}$, and $A^{C} \cap [\nu > n] \in \mathcal{B}_{n}$, so $A \cap [\nu \leq n] \in \mathcal{B}_{n}$. Thus $A \in \mathcal{B}_{\nu}$ and $\{A : A \cap [\nu > n] \in \mathcal{B}_{n}\} \subset \mathcal{B}_\nu$.