---
title: "Classification Problem"
---

# Definition
Let $(\Omega, \mathcal{M}, \mathbb{P})$ be a [[Probability Space]]. Let $(\mathcal{D}, \Sigma_{1})$ and $([n], \mathcal{P}([n]))$ be [[Measure Space]]s (for $n \in \mathbb{N}$). Let $X: \Omega \to \mathcal{D}$ and $Y: \Omega \to [n]$ be [[Random Element]]s representing [[Data]] and [[Label]]s respectively. A [[Classification Problem]] is a [[Tuple]] $(\Omega, \mathcal{M}, \mathbb{P}, \mathcal{D}, \Sigma_{1}, n, X, Y)$.

## Remarks
1. The goal of this problem is to find a [[Function]] $f: \mathcal{D} \to [n]$ so that the [[Risk]] of $f$ is minimized. We say $f$ is a [[Classifier]]
2. This definition is a bit unwieldy. We usually just refer to the problem as $(X, Y, n)$ or $(X, Y)$ instantiating all other [[Object]]s implicitly.