---
title: "Sigma Algebra"
---

# Definition
Let $X$ be a [[Nonempty]] [[Set]]. Then $\mathcal{M} \subset \mathcal{P}(X)$ is a [[Sigma Algebra]] on $X$ if
1. $X \in \mathcal{M}$
2. If $A \in \mathcal{M}$ then $A^{C} \in \mathcal{M}$
3. Suppose $(A_n)_{n \in \mathbb{N}} \subset \mathcal{M}$. Then $\bigcup\limits_{n \in \mathbb{N}} A_{n} \in \mathcal{M}$

## Properties
1. $\mathcal{M}$ is closed under [[Countable]] [[Set Intersection]]

	**Proof**: This follows from [[De Morgan's Law]]. Suppose  $(A_n)_{n \in \mathbb{N}} \subset \mathcal{M}$. Then
	$$\bigcap\limits_{n \in \mathbb{N}} A_{n} = \Big( \bigcup\limits_{n \in \mathbb{N}} A_{n}^{C} \Big)^{C} \in \mathcal{M}$$