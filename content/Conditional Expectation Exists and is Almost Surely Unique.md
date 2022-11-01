---
title: "Conditional Expectation Exists and is Almost Surely Unique"
---

# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $X$ be a [[Random Variable]] on $\Omega$. Let $\mathcal{G} \subset \mathcal{B}$ be a sub-[[Sigma Algebra]]. Then there exists a [[Conditional Expectation]]  $Y$ for $X$ with respect to $\mathcal{G}$. If $Y'$ is another such [[Conditional Expectation]] then $$Y = Y' \text{ almost surely}$$

Therefore, it makes sense to refer to $\mathbb{E}[X|\mathcal{G}]$ as **the** [[Conditional Expectation]] of $X$ with respect to $\mathcal{G}$.

## Proof
Write for $A \in \mathcal{G}$

$$\nu(A) = \int\limits_{A} X d \mathbb{P}(\omega)$$

Then, because [[Integration defines an Absolutely Continuous Measure]], we know that $\nu$ is a [[Signed Measure]] on $\mathcal{G}$ and $\nu << \mathbb{P} {\big|}_{\mathcal{G}}$. Furthermore, $\mathbb{P}$ is a [[Finite Measure]] and thus a [[Sigma-Finite Measure]]Thus, there exists a $\mathbb{P}$-[[Almost Surely]] $\mathcal{G}$-[[Measureable Function|measureable]] unique [[Radon-Nikodym Derivative]] $Z = \frac{d\nu}{d \mathbb{P} {\big|}_{\mathcal{G}}}$ so that for $A \in \mathcal{G}$

$$\nu(A) = \int\limits_{A} Z d \mathbb{P}(\omega) = \int\limits_{A} X d \mathbb{P}(\omega)$$

Thus $Z$ satisfies the definition of [[Conditional Expectation]]. Since $Z$ is $\mathbb{P}$-[[Almost Surely]] unique, any other $\mathcal{G}$-[[Measureable Function|measureable]] [[Random Variable]] satisfying the definition of [[Conditional Expectation]] is also a [[Radon-Nikodym Derivative]] and is thus [[Almost Surely]] $Z$. $\blacksquare$