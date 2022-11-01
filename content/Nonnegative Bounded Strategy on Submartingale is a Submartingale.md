---

title: "Nonnegative Bounded Strategy on Submartingale is a Submartingale"

---
# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $(\mathcal{F}_{n})_{n=0}^{\infty}$ be a [[Discrete-Time Filtration]] on $\mathcal{B}$. Let $(X_{n})_{n=0}^{\infty}$ be a $(\mathcal{F}_{n})_{n=0}^{\infty}$-[[Submartingale]] on $\Omega, \mathcal{B}$ and let $(H_{n})_{n=1}^{\infty}$ be a [[Strategy]] for $(X_{n})_{n=0}^{\infty}$. Then the winnings $(H \cdot X)_{n}$ for $n \geq 1$ forms a [[Submartingale]].

## Proof
Recall that [[An Adapted Process is a Supermartingale iff its negative is a Submartingale]], so $({-X}_{n})_{n=0}^{\infty}$ is a [[Supermartingale]]. Then by [[Nonnegative Bounded Strategy on Supermartingale is a Supermartingale]], we have that $(H \cdot -X)_{n}$ is a [[Supermartingale]] for $n  \geq 1$. But for $n \geq 1$:
$$\begin{align*}
(H \cdot -X)_{n} &= \sum\limits_{m=1}^{n} H_{m} (-X_{m} + X_{m-1})\\
&=-\sum\limits_{m=1}^{n} H_{m} (X_{m} - X_{m-1})\\
&=-(H \cdot X)_{n}.
\end{align*}$$
Again, because [[An Adapted Process is a Supermartingale iff its negative is a Submartingale]] we have that $(H \cdot X)_{n}$ for $n \geq 1$ is a [[Submartingale]] $\blacksquare$

