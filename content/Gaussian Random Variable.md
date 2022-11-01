---
title: "Gaussian Random Variable"
---

# Definition
Suppose $(\Omega, \mathcal{M}, \mathbb{P})$ is a [[Probability Space]]. Then $X$ is a [[Gaussian Random Variable]] on $\Omega$ if it has [[Distribution]] determined by [[Probability Density Function]]

$$f_{X}(x) = \frac{1}{\sqrt{2 \pi} \sigma} e^{- \frac{1}{2} (\frac{x- \mu}{\sigma})^{2}}$$

where $\sigma$ and $\mu$ are parameters for the distribution. We write $X \sim  \mathcal{N}(\mu, \sigma^{2})$.

The [[Probability Density Function]] is taken with respect to the [[Lebesgue Measure]] on $\mathcal{B}(\mathbb{R})$.

## Properties
1. $\mu = \mathbb{E}(X)$ **Proof**: [[TODO]]
2. $\sigma^{2}= \text{Var}(X)$ **Proof**: [[TODO]]
3. [[Gaussian Distributions are Symmetric about their Mean]]