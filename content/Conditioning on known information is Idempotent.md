---
title: "Conditioning on known information is Idempotent"
---

# Statement
Let $(\Omega, \mathcal{G}, \mathbb{P})$ be a [[Probability Space]] and let $\mathbb{B} \subset \mathcal{G}$ be a sub-[[Sigma Algebra]] of $\mathbb{G}$. Suppose $X$ is a $\mathcal{B}$-[[Measureable Function|measureable]] [[Random Variable]] on $\Omega$. Then

$$\mathbb{E}[X|\mathcal{G}] = X$$

[[Almost Surely|almost surely]].
## Proof
Because $X$ is $\mathcal{B}$-[[Measureable Function|measureable]], we know that $\forall S \in \mathcal{B}(\mathbb{R})$ $X^{-1}(S) \in \mathcal{B}$. Since $\mathcal{B} \subset \mathcal{G}$, we see $X^{-1}(S) \in \mathcal{G}$. Thus $X$ is $\mathcal{G}$-measureable and it satisfies $\forall A \in \mathcal{G}$:

$$\int\limits_{A} X d \mathbb{P}(\omega) = \int\limits_{A} X d \mathbb{P}(\omega)$$

so $X$ is a [[Conditional Expectation]] of $X$ with respect to $\mathcal{G}$. The last statement follows becuase [[Conditional Expectation Exists and is Almost Surely Unique]]. $\blacksquare$