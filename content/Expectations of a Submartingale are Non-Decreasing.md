---

title: "Expectations of a Submartingale are Non-Decreasing"

---
# Statement
Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a [[Probability Space]]. Let $(X_{t})_{t \in T}$ be a [[Submartingale]] wrt [[Filtration]] $\mathcal{F}_{*} := (\mathcal{B}_{t})_{t \in T}$  on $\Omega$. Then $\forall r \leq t \in T$,  $\mathbb{E}(X_{r}) \leq \mathbb{E}(X_{t})$.

## Proof
This follows by [[Smoothing]] and [[Expectation is Non-Decreasing]]: 
$$\begin{align*}
&\mathbb{E}(X_{t}|\mathcal{B}_{r}) \geq X_{r}\\
\Rightarrow&\mathbb{E}(X_{t}) = \mathbb{E}(\mathbb{E}(X_{t}|\mathcal{B}_{r})) \geq \mathbb{E}(X_{r})
\end{align*}$$
$\blacksquare$