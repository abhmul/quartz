---
title: "Sigma Algebra induced by Function"
---

# Definition
Let $X$ and $(Y, \mathcal{N})$ be [[Measure Space]]s. Let $f: X \to Y$ be a [[Function]]. Then the [[Sigma Algebra induced by Function|sigma algebra induced by]] $f$ is
$$\sigma(f) := \{f^{-1}(E) : E \in \mathcal{N}\}$$
## Remarks
1. We should check that $\sigma(f)$ is indeed a [[Sigma Algebra]]
	
	**Proof**: We check the criteria for being a [[Sigma Algebra]]
	1. $Y \in \mathcal{N}$ and $f^{-1}(Y) = X \in \sigma(f)$.
	2. Suppose $A \in \sigma(f)$. Then there exists $E \in \mathcal{N}$ so $f^{-1}(E) = A$. Since $\mathcal{N}$ is [[Sigma Algebra]] we know $E^{C} \in \mathcal{N}$. Thus $$A^{C} = f^{-1}(E)^{C} = f^{-1}(E^{C}) \in \sigma(f)$$
	3. Suppose $(A_n)_{n=1}^{\infty} \subset \sigma(f)$. Then there exists $(E_n)_{n=1}^{\infty} \subset \mathcal{N}$ such that $f^{-1}(E_{n}) = A_{n}$. Then $\bigcup\limits_{n \in \mathbb{N}} E_{n} \in \mathcal{N}$. $$\bigcup\limits_{n \in \mathbb{N}} f^{-1}(E_{n}) = f^{-1}\Big(\bigcup\limits_{n \in \mathbb{N}} E_{n} \Big) \in \sigma(f)$$ $\blacksquare$
