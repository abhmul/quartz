---
title: "Sum of Independent Random Variables is in L1 if and only if Random Variables are in L1"
---

# Statement
Suppose $(\Omega, \mathcal{M}, \mathbb{P})$ is a [[Probability Space]] and $X, Y$ are [[Independence|independent]] [[Random Variable]]s on $\Omega$. Then $X+Y \in L^{1}(\Omega)$ [[If and Only If]] $X, Y \in L^{1}(\Omega)$.

## Proof
($\Leftarrow$): This is the easy direction. Suppose $X \in L^{1}$ and $Y \in L^{1}$. Since [[Lp Spaces are Vector Spaces]], we have that $X + Y \in L^{1}$ $\checkmark$

($\Rightarrow$): Suppose $X+Y \in L^{1}$. Recall from the definition of [[L1 Integrable Functions]], this means
$$\int\limits_{\Omega} |X(\omega)+Y(\omega)| d \mathbb{P}(\omega) < \infty$$
Since $(X, Y)$  [[Independent Random Elements induce Product Measure|are independent, they induce a product measure]] $F_{X,Y}$ on $\mathbb{R}^{2}$ where for $A,B \in \mathbb{R}$, $F_{X,Y}(A \times B) = F_{X}(A)F_{Y}(B)$ ($F_{X}$ and $F_{Y}$ are the [[Induced Probability Measure]] of $X$ and $Y$ respectively). Furthermore

$$\begin{align*}
\int\limits_{\Omega} |X(\omega)+Y(\omega)| d \mathbb{P}(\omega) &= \int\limits_{\mathbb{R}^{2}} |x+y| F_{X,Y}(d(x,y))\\
&=\int\limits_{\mathbb{R}} \left[\int\limits_{\mathbb{R}} |x+y| F_{X}(dx)\right] F_{Y}(dy)
\end{align*}$$
and $y \mapsto \int\limits_{\mathbb{R}} |x+y| F_{X}(dx) \in L^{1}(\Omega)$ by [[Fubini's Theorem]]. Thus, for $y \in \mathbb{R}$ [[Almost Everywhere]] we have that $\int\limits_{\mathbb{R}} |x+y| F_{X}(dx) < \infty$. Pick some such $y \in \mathbb{R}$. Then

$$\begin{align*}
\int\limits_{\Omega} |X(\omega)| d \mathbb{P}(\omega) &= \int\limits_\mathbb{R} |x| F_{X}(dx)\\
&=\int\limits_\mathbb{R} |x+y-y| F_{X}(dx)\\
&\leq \int\limits_\mathbb{R} |x+y| F_{X}(dx) + \int\limits_\mathbb{R} |y| F_{X}(dx)\\
&=\int\limits_\mathbb{R} |x+y| F_{X}(dx) + |y|\\
&< \infty
\end{align*}$$
and $X \in L^{1}(\Omega)$. Swap $X$ and $Y$ to get the same result for $Y$. $\checkmark$ $\blacksquare$


# Other Outlinks
- [[Expectation]]
- [[Fubini's Theorem]]