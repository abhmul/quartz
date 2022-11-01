---
title: "Conditional Expectation over the Trivial Sigma Algebra is Expectation"
---

# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $X$ be a [[Random Variable]] on $\Omega$. Then

$$\mathbb{E}[X| \{\emptyset, \Omega\}] = \mathbb{E}[X]$$

## Proof
Observe that $\mathbb{E}[X]$ is indeed trivially measureable since [[Constant Functions are Measureable]]. Furthermore

$$\int\limits_{\Omega} X d \mathbb{P}(\omega) = \mathbb{E}[X] = \int\limits_{\Omega} \mathbb{E}[X]$$

and 

$$\int\limits_{\emptyset} X d \mathbb{P}(\omega) = 0 = \int\limits_{\emptyset} \mathbb{E}[X]$$

so $\mathbb{E}[X]$ is the [[Conditional Expectation]] of $X$ with respect to $\{\emptyset, \Omega\}$. $\blacksquare$

# Other Outlinks
- [[Conditional Expectation]]
- [[Expectation]]
- [[Trivial Sigma Algebra]]