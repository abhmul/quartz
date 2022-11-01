---

title: "Expectations of a Martingale are Constant"

---
# Statement
Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a [[Probability Space]]. Let $(X_{t})_{t \in T}$ be a [[Martingale]] wrt [[Filtration]] $\mathcal{F}_{*} := (\mathcal{B}_{t})_{t \in T}$  on $\Omega$. Then $\forall r,t \in T$,  $\mathbb{E}(X_{r}) = \mathbb{E}(X_{t})$.

## Proof
This follows by [[Expectations of a Submartingale are Non-Decreasing]] and [[Expectations of a Supermartingale are Non-increasing]]. Recall that [[A Martingale is a Supermartingale and a Submartingale]] , so $\forall r \leq t \in T$
$$\begin{align*}
\mathbb{E}(X_{t}) \geq \mathbb{E}(X_{r})\\
\mathbb{E}(X_{t}) \leq \mathbb{E}(X_{r})\\
\end{align*}$$
Thus, $\mathbb{E}(X_{t}) = \mathbb{E}(X_{r})$, but now order of $r,t$ no longer matter (we can switch them), so we have the result $\forall r, t \in T$.

$\blacksquare$