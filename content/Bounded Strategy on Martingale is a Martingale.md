---

title: "Bounded Strategy on Martingale is a Martingale"

---
# Statement
a

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
&=\sum\limits_{m=1}^{n}H_{m}(X_{m} - X_{m-1}) - \mathbb{E}(H_{n+1} (X_{n+1} - X_{n}) | \mathcal{F}_{n})\\
&= (H \cdot X)_{n}
\end{align*}$$
since
$$\begin{align*}
\mathbb{E}(H_{n+1} (X_{n+1} - X_{n}) | \mathcal{F}_{n}) &= H_{n+1} (\mathbb{E}(X_{n+1} | \mathcal{F}_{n}) -X_{n})\\
&= 0.
\end{align*}$$
$\checkmark$ $\blacksquare$

## Remarks
1. This theorem nicely states that any **bounded** gambling strategy cannot make an unfavorable game favorable.