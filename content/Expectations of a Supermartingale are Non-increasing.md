---

title: "Expectations of a Supermartingale are Non-increasing"

---
# Statement
Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a [[Probability Space]]. Let $(X_{t})_{t \in T}$ be a [[Supermartingale]] wrt [[Filtration]] $\mathcal{F}_{*} := (\mathcal{B}_{t})_{t \in T}$  on $\Omega$. Then $\forall r \leq t \in T$,  $\mathbb{E}(X_{r}) \geq \mathbb{E}(X_{t})$.

## Proof
This follows by [[An Adapted Process is a Supermartingale iff its negative is a Submartingale]] and [[Expectations of a Submartingale are Non-Decreasing]] and [[Linearity of Expectation]]. That is,
$$\begin{align*}
&\mathbb{E}(-X_{t}) \geq \mathbb{E}(-X_{r})\\
\Rightarrow&\mathbb{E}(X_{t}) \leq \mathbb{E}(X_{r})\\
\end{align*}$$
$\blacksquare$