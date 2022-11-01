---
title: "Characteristic Function of Standard Gaussian Random Variable"
---

# Statement
Suppose $(\Omega, \mathcal{M}, \mathbb{P})$ is a [[Probability Space]] and $X$ is a [[Standard Gaussian Random Variable]]. Then

$$\phi_{X}(t) = \exp (\frac{t^{2}}{2})$$

## Proof
Since $X$ is a [[Standard Gaussian Random Variable]], we know $X \sim \mathcal{N}(0, 1)$. Applying the formula for the [[Characteristic Function of a Gaussian Random Variable]]:

$$\begin{align*}
\phi_{X}(t) &= \exp (i t 0 - \frac{1^{2} t^{2}}{2})\\
&=\exp (\frac{t^{2}}{2})
\end{align*}$$
$\blacksquare$

