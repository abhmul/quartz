---

title: "Martingale Convergence Theorem"

---
# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] . Let $(X_{n})_{n \geq 1}$ be a [[Discrete-Time Process|discrete-time]] [[Submartingale]] wrt [[Discrete-Time Filtration]] $\mathcal{F}_{*} := (\mathcal{F}_{n} \subset \mathcal{B})_{n \in \mathbb{N}}$ so that $\sup\limits_{n \geq 1} \mathbb{E}(X_{n})^{+} < \infty$. Then there exists $X \in L^{1}(\mathcal{B})$ so that $X_{n} \to X$ [[Almost Sure Convergence|almost surely]].

## Proof
Letting $a < b \in \mathbb{R}$, we uniformly bound the number of [[Complete Upcrossings]] with the [[Upcrossing Inequality]]. First note that if $a \geq 0$ 
$$(X_{n} - a)^{+} = 1_{X_{n} \geq a}X_{n} -1_{X_{n} \geq a}a \leq 1_{X_{n} \geq a}X_{n} \leq (X_{n})^{+}$$
and if $a < 0$
$$(X_{n} - a)^{+} = 1_{X_{n} \geq a}X_{n} -1_{X_{n} \geq a}a = (X_{n})^{+} + 1_{0 > X_{n} \geq a}X_{n} -1_{X_{n} \geq a}a \leq (X_{n})^{+} + |a|.$$

So $\forall n \geq 1$
$$\begin{align*}
(b - a) \mathbb{E}(U_{n}[a, b]) &\leq \mathbb{E}(X_{n} - a)^{+} - \mathbb{E}(X_{1} - a)^{+}\\
&\leq \mathbb{E}(X_{n})^{+} + |a|\\
&\leq M + |a|
\end{align*}$$
for $\infty > M \geq \sup\limits_{n \geq 1} \mathbb{E}(X_{n})^{+}$. Therefore, we have that $\mathbb{E}(U_{n}[a,b]) \leq \frac{M + |a|}{b-a}$. Since $U_{n}[a,b]$ is [[Non-Decreasing Function]] as $n \to \infty$, it converges (possibly to $\infty$), say to $U[a,b]$. By [[Monotone Convergence Theorem]], we have that 
$$\frac{M + |a|}{b-a} \geq \lim\limits_{n \to \infty} \mathbb{E}(U_{n}[a,b]) = \mathbb{E}(U[a,b]).$$
Therefore, $U[a,b]$ must be [[Almost Surely]] [[Finite Set|finite]] (otherewise $\mathbb{E}(U[a,b]) = \infty$). This means that
$$\mathbb{P}[\liminf\limits_{n \to \infty} X_{n} \leq a < b \leq \limsup\limits_{n \to \infty} X_{n}] = 0,$$
since that [[Event]] occurs [[If and Only If]] $U[a,b] = \infty$.

Therefore
$$\bigcup\limits_{a, b \in \mathbb{Q}} [\liminf\limits_{n \to \infty} X_{n} \leq a < b \leq \limsup\limits_{n \to \infty} X_{n}]$$
is a [[Null Set]]. But then we must have that $\liminf\limits_{n \to \infty} X_{n} = \limsup\limits_{n \to \infty} X_{n} =: X$ [[Almost Surely]].

Finally, we show that $X \in L^{1}(\mathcal{B})$. Recall that [[A Submartingale has uniformly Bounded First Moment iff it has uniformly Bounded Positive Moment]], so $\infty > \sup\limits_{n \geq 1} \mathbb{E}|X_{n}|$. By [[Fatou's Lemma]], we have that
$$\mathbb{E}|X| \leq \liminf\limits_{n \to \infty} \mathbb{E}|X_{n}| \leq \sup\limits_{n \geq 1} \mathbb{E}|X_{n}| < \infty.$$
so $X \in L^{1}(\mathcal{B})$. $\blacksquare$

## Remarks
1. This holds for [[Martingale]]s as well since a [[Martingale]] is a [[Submartingale]]. A corresponding result holds for [[Supermartingale]]s since [[An Adapted Process is a Supermartingale iff its negative is a Submartingale]].