---

title: "Nonnegative Bounded Strategy on Supermartingale is a Supermartingale"

---
# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $(\mathcal{F}_{n})_{n=0}^{\infty}$ be a [[Discrete-Time Filtration]] on $\mathcal{B}$. Let $(X_{n})_{n=0}^{\infty}$ be a $(\mathcal{F}_{n})_{n=0}^{\infty}$-[[Supermartingale]] on $\Omega, \mathcal{B}$ and let $(H_{n})_{n=1}^{\infty}$ be a [[Strategy]] for $(X_{n})_{n=0}^{\infty}$. Then the winnings $(H \cdot X)_{n}$ for $n \geq 1$ forms a [[Supermartingale]].

## Proof
First note that for $n \geq 1$ because $H_{n}$ is [[Bounded Function|bounded]], say by $M \in \mathbb{R}_{\geq 0}$ 
$$\begin{align*}
\mathbb{E}|(H \cdot X)_{n}| &= \mathbb{E}\left|\sum\limits_{m=1}^{n}H_{m}(X_{m} - X_{m-1})\right|\\
&\leq M \sum\limits_{m=1}^{n} \mathbb{E}|X_{m} - X_{m-1}| & \text{(Triangle Inequality)}\\
&\leq M \sum\limits_{m=1}^{n} \mathbb{E}|X_{m}| + \mathbb{E}| X_{m-1}| & \text{(Triangle Inequality)}\\\\
&< \infty
\end{align*}$$
since $X_{m} \in L^{1}(\mathcal{B})$ $\forall m \geq 0$. So $(H \cdot X)_{n} \in L^{1}(\mathcal{B})$ as well. $\checkmark$

Next, for $n \geq 1$, we have that $X_{m}, H_{m+1} \in \mathcal{F}_{n}$ for all $0 \leq m \leq n$, so
$$(H \cdot X)_{n} = \sum\limits_{m=1}^{n} H_{m} (X_{m} - X_{m-1}) \in \mathcal{F}_{n}$$
$\checkmark$

Observe that for $n \geq 0$
$$\begin{align*}
\mathbb{E}((H \cdot X)_{n+1} | \mathcal{F}_{n}) &= \mathbb{E}(\sum\limits_{m=1}^{n+1} H_{m}(X_{m} - X_{m-1}) | \mathcal{F}_{n})\\
&=\sum\limits_{m=1}^{n+1}\mathbb{E}(H_{m}(X_{m} - X_{m-1}) | \mathcal{F}_{n})\\
&=\sum\limits_{m=1}^{n}H_{m}(X_{m} - X_{m-1}) + \mathbb{E}(H_{n+1} (X_{n+1} - X_{n}) | \mathcal{F}_{n})\\
&\leq (H \cdot X)_{n}
\end{align*}$$
since $H_{n+1} \geq 0$, so
$$\begin{align*}
\mathbb{E}(H_{n+1} (X_{n+1} - X_{n}) | \mathcal{F}_{n}) &= H_{n+1} (\mathbb{E}(X_{n+1} | \mathcal{F}_{n}) -X_{n})\\
&\leq 0.
\end{align*}$$
$\checkmark$ $\blacksquare$

## Remarks
1. We use the [[Bounded Function|boundedness]] of $H_{n}$ in the first step to pull it out of the [[Expectation]] and give us that $(H \cdot X)_{n} \in L^{1}(\mathcal{B})$. However, there are other constraints that get use the same result. For example, if we had $H_{n}, X_{n-1} \in L^{2}(\mathcal{B})$ $\forall n \in \mathbb{N}$, then we could apply [[Cauchy-Schwarz Inequality]] to get that $(H \cdot X)_{n} \in L^{1}(\mathcal{B})$. 
2. However, simply requiring $H_{n} \in L^{1}(\mathcal{B})$ is not enough since if $X_{n} = 1/\sqrt{x_{n}}$ for $x_{n} \sim [0,1]$ [[Continuous Uniform Distribution|uniformly]] [[Independently and Identically Distributed|iid]] and we have $H_{n} = \frac{1}{\sqrt{x_{n-1}}}$, then $(H \cdot X)_{1} = \frac{1}{\sqrt{x_{0}}} \cdot \frac{1}{\sqrt{x_{1}}} - \frac{1}{x_{0}}$. Since 
	$$\begin{align*}
\mathbb{E}\left(\frac{1}{\sqrt{x_{0}}} \cdot \frac{1}{\sqrt{x_{1}}}\right) &= \mathbb{E}\left(\frac{1}{\sqrt{x_{0}}} \right) \mathbb{E}\left(\frac{1}{\sqrt{x_{1}}}\right) & \text{ independence}\\
&= 4\\
\mathbb{E}\left(\frac{1}{x_{0}}\right) &= \infty
\end{align*}$$
	we must have that $\mathbb{E}|(H \cdot X)_{1}| = \infty$.