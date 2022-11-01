---
title: "Almost Sure Convergence does not imply Lp Convergence"
---

# Statement
Suppose $(\Omega, \mathcal{M}, \mathbb{P})$ is a [[Probability Space]] and $(X_{n})$ is a [[Sequence]] of [[Random Variable]]s on $\Omega$. Suppose $X_{n} \to X$ [[Almost Sure Convergence|almost surely]]. Then, it does not follow that $X_{n} \to X$ in $L^{p}$ for any $p \geq 1$.

## Proof
We prove by constructing a [[Counterexample]]. Suppose $(X_{n})$ is a [[Sequence]] of [[Random Variable]]s defined on [[Probability Space]] $([0,1], \mathcal{B}([0,1]), \lambda)$ and for $x \in [0,1]$

$$X_{n}(x) = \begin{cases} n^{2} & x \in [0, \frac{1}{n}) \\ 0 & x \in [\frac{1}{n}, 1] \end{cases}$$
Then for $x \in (0, 1]$, if $n \geq \lceil{\frac{1}{x}}\rceil$, we have that $X_{n}(x) = 0$. Thus on $(0, 1]$, $X_{n} \to 0$ [[Pointwise Convergence|pointwise]]. Since $(0, 1]^{C} = \{0\}$ is a [[Null Set]], we have that $X_{n} \to 0$ [[Almost Sure Convergence|almost surely]].

Now suppose $X_{n} \overset{L^{p}}{\to} X$ for some $p \geq 1$. Recall that [[Lp Spaces are Banach]] so $X \in L^{p}$. Then, because [[Norms are Continous]]:

$$\mathbb{E}(|X_{n}|^{p})^{\frac{1}{p}} \to \mathbb{E}(|X|^{p})^{\frac{1}{p}}$$
and therefore
$$\mathbb{E}(|X_{n}|^{p}) \to \mathbb{E}(|X|^{p})$$
Now observe that,
$$\begin{align*}
\mathbb{E}(|X_{n}|^{p}) &= \frac{n^{2p}}{n}\\
&=n^{2p-1}\\
&\geq n^{1} &(\text{since }p \geq 1)\\
&\to \infty\\
\end{align*}$$
This [[Proof by Contradiction|contradicts]] $X_{n} \overset{L^{p}}{\to} X$ and therefore $X_{n}$ does not [[Lp Convergence|converge in Lp]]. $\blacksquare$


# Other Outlinks
- [[Lp Convergence]]
- [[Borel Sigma Algebra]]
- [[Lebesgue Measure]]