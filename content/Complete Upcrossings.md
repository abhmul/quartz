---

title: "Upcrossings"

---
# Definition 1
Suppose $(x_{n})_{n=0}^{\infty} \subset \mathbb{R}$ is a [[Sequence]] and $a < b \in \mathbb{R}$. [[Induction|Inductively]] define for $i \in \mathbb{N}$:

$$\begin{align*}
& \tau_{0} = 0\\
&\sigma_{i} = \inf \{j \in \mathbb{N} : j > \tau_{i-1}, x_{j} \leq a\}\\
&\tau_{i} = \inf \{j \in \mathbb{N} : j > \sigma_{i}, x_{j} \geq b\}
\end{align*}$$
Then the number of [[Complete Upcrossings]], $U_{N}^{*}[a, b]$, of $x_{1}, \dots x_{N}$ for $N \in \mathbb{N}$ is
$$U_{N}^{*}[a, b] = \sup \{i \in \mathbb{N} : \tau_{i} \leq N\}$$
Furthermore we call
$$U_{\infty}^{*}[a, b] = \lim\limits_{N \to \infty} U_{N}^{*}[a, b] \in \bar{\mathbb{R}}$$
## Remarks
1. We are measuring the number of times that our sequence has fallen down to $a$, then come back up to $b$.
2. Our defintion for $U_{\infty}^{*}$ makes sense since $U_{N}^{*}[a, b]$ is a [[Monotone Sequence]] and [[Monotone Sequences converge to their Extremum]].

# Statement 2
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $(\mathcal{F}_{n})_{n=1}^{\infty}$ be a [[Discrete-Time Filtration]] on $\mathcal{B}$. Let $(X_{n})_{n=1}^{\infty}$ be a $(\mathcal{F}_{n})_{n=1}^{\infty}$-[[Adapted Process]]. Let $a < b \in \mathbb{R}$. Then the following [[Random Variable]]s are [[Stopping Time]]s for $k \geq 1$:
$$\begin{align*}
N_{0} &:= 0\\
N_{2k-1} &:= \inf\limits \{m > N_{2k-2} : X_{m} \leq a\}\\
N_{2k} &:= \inf\limits \{m > N_{2k-1} : X_{m} \geq b\}\\
\end{align*}$$
We define the $\mathcal{F}_{n}$-[[Random Variable]] 
$$U_{n}[a,b] = \sup\limits \{k \geq 0 : N_{2k} \leq n\}$$
to be the number of [[Complete Upcrossings]] by time $n \in \mathbb{N}$.

## Proof
We check that $N_{2k-1}$ and $N_{2k}$ are [[Stopping Time]]s by [[Induction]]. First observe that, letting $n \in \mathbb{N}$,
$$\begin{align*}
[N_{1} = n] &= [X_{1} > a, \dots, X_{n-1} > a] \cap [X_{n} \leq a] \in \mathcal{F}_{n}\\
\end{align*}$$
by virtue of being a [[Filtration]], so $N_{1}$ is a [[Stopping Time]]. Now suppose $N_{1}, \dots, N_{2k-1}$ are [[Stopping Time]]s for $k \geq 1$ . Then, letting $n \in \mathbb{N}$,
$$\begin{align*}
[N_{2k} = n] &= [X_{N_{2k-1}+1} < b, \dots, X_{n-1} < b] \cap [X_{n} \geq b] \in \mathcal{F}_{n}\\
&\bigcup\limits_{m = 1}^{n-1} [X_{m+1} < b, \dots, X_{n-1} < b] \cap [X_{n} \geq b] \cap [N_{2k-1} = m] \in \mathcal{F}_{n}
\end{align*}$$
by virtue of $N_{2k-1}$ being a [[Stopping Time]] and $(\mathcal{F}_{n})_{n=1}^{\infty}$ being a [[Filtration]]. Thus, $N_{2k}$ is a [[Stopping Time]]. A similar approach will show that $N_{2k+1}$ must also be a [[Stopping Time]].

Now we check that $U_{n}[a,b] \in \mathcal{F}_{n}$. Let $k \in \mathbb{N}$ 
$$[U_{n}[a,b] = k] = [N_{2k} \leq n] \cap [N_{2k+2} > n] \in \mathcal{F}_{n}$$
which holds because $N_{2k}$ and $N_{2k+2}$ are both [[Stopping Time]]s. $\blacksquare$
# Other Outlinks
- [[Real Numbers]]
- [[Natural Numbers]]
- [[Infimum]]
- [[Supremum]]
- [[Extended Real Numbers]]