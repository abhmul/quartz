---
title: "Expectation does not always exist"
---

# Statement
Suppose $(\Omega, \mathcal{M}, \mathbb{P})$ is a [[Probability Space]]. There exists a [[Random Variable]] $X$ on $\Omega$ so that $X \not\in \bar{L^{1}}(\Omega)$. In other words, $\mathbb{E}(X)$ does not exist and we cannot even assign it a value of $\infty$ or $-\infty$ in the [[Compactification]] of the [[Real Numbers]].

## Proof
Consider the [[Probability Space]] $([-1, 1], \mathcal{B}([-1, 1]), \frac{1}{2}\lambda)$, where $\lambda$ is the [[Lebesgue Measure]]. Consider [[Random Variable]]

$$X = \begin{cases} \frac{1}{x} & \text{if } x \neq 0\\
0 & \text{if } x=0\end{cases}$$
Then $$X^{+} = \begin{cases} \frac{1}{x} & \text{if } x > 0\\ 0 & \text{if } x \leq 0\end{cases}$$ and $$X^{-} = \begin{cases} -\frac{1}{x} & \text{if } x < 0\\ 0 & \text{if } x \geq 0\end{cases}$$
Then

$$\begin{align*}
\frac{1}{2} \int\limits X^{+} d \lambda &= \frac{1}{2} \int\limits_{(0,1]} \frac{1}{x} d \lambda\\
&=\lim\limits_{\epsilon \downarrow 0}\left[-\frac{1}{2} \frac{1}{x^{2}}\right]_{\epsilon}^{1} \\
&=-\frac{1}{2} + \lim\limits_{\epsilon \downarrow 0}\frac{1}{2\epsilon^{2}}\\
&= \infty
\end{align*} $$
Likewise
$$\begin{align*}
\frac{1}{2} \int\limits X^{-} d \lambda &= \frac{1}{2} \int\limits_{[-1,0)} -\frac{1}{x} d \lambda\\
&=\lim\limits_{\epsilon \downarrow 0}\left[\frac{1}{2} \frac{1}{x^{2}}\right]_{-1}^{-\epsilon} \\
&=-\frac{1}{2} + \lim\limits_{\epsilon \downarrow 0}\frac{1}{2\epsilon^{2}}\\
&= \infty
\end{align*} $$
Thus, by definition of [[Extended L1 Functions]], $X \not\in \bar{L^{1}}$. $\blacksquare$