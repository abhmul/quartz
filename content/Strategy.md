---

title: "Strategy"

---
# Definition
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $(\mathcal{F}_{n})_{n=1}^{\infty}$ be a [[Discrete-Time Filtration]] on $\mathcal{B}$. Let $(H_{n})_{n=1}^{\infty}$ be a [[Predictable Sequence]] on $(\mathcal{F}_{n})_{n=1}^{\infty}$ and let $(X_{n})_{n=1}^{\infty}$ be a $\mathcal{F}_{n}$-[[Adapted Process]] $\Omega, \mathcal{B}$. Then we call $(H_{n})_{n=1}^{\infty}$ a [[Strategy]] on $(X_{n})_{n=1}^\infty$with *winnings*
$$(H \cdot X)_{n} = \sum\limits_{m=1}^{n} H_{m} (X_{m} - X_{m-1})$$
for $n \geq 1$, where $X_{0} = 0$.
## Properties
1. [[Nonnegative Bounded Strategy on Supermartingale is a Supermartingale]]
2. [[Nonnegative Bounded Strategy on Submartingale is a Submartingale]]
3. [[Bounded Strategy on Martingale is a Martingale]]