---
title: "Intersection Sigma Algebra"
---

# Definition
Suppose $(X, \mathcal{M})$ is a [[Measure Space]] and let $A \subset X$. Then the collection
$$\mathcal{M} \cap A := \{E \cap A : E \in \mathcal{M}\}$$
is the [[Intersection Sigma Algebra]] on $A$.

## Remarks
1. We should check that $\mathcal{M} \cap A$ is indeed a [[Sigma Algebra]]:
	
	**Proof**: We check the criteria for being a [[Sigma Algebra]]
	1. Since $X \in \mathcal{M}$ and $X \cap A = A$, we have that $A \in \mathcal{M} \cap A$. $\checkmark$
	2. Suppose $F \in \mathcal{M} \cap A$. Then there exists $E \in \mathcal{M}$ so $F = E \cap A$. Thus $$\begin{align*}
A \setminus F &= A \cap (E \cap A)^{C}\\
&= A \cap (E^{C} \cup A^{C})\\
&=(A \cap E^{C}) \cup (A \cap A^{C})\\
&=E^{C} \cap A \in \mathcal{M} \cap A
\end{align*}$$
		since $E^{C} \in \mathcal{M}$. $\checkmark$
	3. Suppose $(F_n)_{n=1}^{\infty} \subset \mathcal{M} \cap A$. Then there exists $(E_n)_{n=1}^{\infty} \subset \mathcal{M}$ so that $F_{n} = E_{n} \cap A$ $\forall n \in \mathbb{N}$. Then $$\bigcup\limits_{n \in \mathbb{N}} F_{n} = \bigcup\limits_{n \in \mathbb{N}} (E_{n} \cap A) =  A \cap \bigcup\limits_{n \in \mathbb{N}} E_{n} \in \mathcal{M} \cap A$$
		since $\bigcup\limits_{n \in \mathbb{N}} E_{n} \in \mathcal{M}$. $\checkmark$ $\blacksquare$
	