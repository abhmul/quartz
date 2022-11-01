---

title: "Sigma Field up to Stopping Time"

---
# Definition
Let $\mathcal{F} = \{\mathcal{B}_{n} : n \in \mathbb{N}\}$ be a [[Discrete-Time Filtration]] over $\Omega$ and let $\nu : \Omega \to \bar{\mathbb{N}}$ be a [[Stopping Time]] on $\mathcal{F}$. Then the [[Sigma Field up to Stopping Time]] is the [[Sigma Algebra]]
$$\mathcal{B}_{\nu} := \{A \in \mathcal{B}_{\infty}: A \cap [\nu = n] \in \mathcal{B}_{n} \text{ }\forall n \in \mathbb{N}\}$$
## The [[Sigma Field up to Stopping Time]] is a [[Sigma Algebra]]
We verify the axioms of a [[Sigma Algebra]].
1. Observe that $\Omega \cap [\nu = n] = [\nu = n] \in \mathcal{B}_{n}$ for all $n \in \mathbb{N}$ by definition of [[Stopping Time]]. Thus $\Omega \in \mathcal{B}_\nu$. $\checkmark$
2. Suppose $A \in \mathcal{B}_\nu$. Then for all $n \in \mathbb{N}$ $$A^{C} \cap [\nu = n] = (A \cap [\nu = n])^{C} \cap [\nu =n] \in \mathcal{B}_n$$ since $A \cap [\nu = n], [\nu = n] \in \mathcal{B}_n$ and $\mathcal{B}_{n}$ is a [[Sigma Algebra]]. Thus, $A^{C} \in \mathcal{B}_\nu$. $\checkmark$
3. Suppose $\{A_{i}\}_{i \in \mathbb{N}} \subset \mathcal{B}_\nu$. Then $\forall n \in \mathbb{N}$ $$[\nu = n] \cap\bigcup\limits_{i \in \mathbb{N}} A_{i} = \bigcup\limits_{i \in \mathbb{N}} (A_{i} \cap [\nu = n]) \in \mathcal{B}_{n}$$ since $A_{i} \cap [\nu = n] \in \mathcal{B}_{n}$ $\forall i \in \mathbb{N}$ and $\mathcal{B}_{n}$ is a [[Sigma Algebra]]. $\checkmark$

Thus, $\mathcal{B}_\nu$ is a [[Sigma Algebra]]. $\blacksquare$

## Properties
1. [[Sigma Field up to Constant Stopping Time is just the Sigma Field at that time]]
2. [[A Stopping Time is Measurable with respect to the Sigma Field up to it]]
3. [[Corollary]] of (2): [[A Stopping Time is Measureable with respect to the Maximal Sigma Field of its Filtration]]
4. [[Equivalent Conditions for being a Sigma Field up to a Stopping Time]]
5. [[Comparing two Stopping Times is in Sigma Field up to either Stopping Time]]

## Remarks
1. If $A \in \mathcal{B}_{\nu}\subset \mathcal{B}_\infty$ then since $[\nu = \infty] \in \mathcal{B}_\infty$, we get that $A \cap [\nu = \infty] \in \mathcal{B}_\infty$. Thus, the defining property can be extended to $\bar{\mathbb{N}}$.