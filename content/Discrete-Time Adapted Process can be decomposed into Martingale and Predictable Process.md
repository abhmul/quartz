# Statement
Let $(Z_{n})$ be a [[Discrete-Time Process|discrete-time]] [[Adapted Process]] on [[State Space]] $\mathbb{R}$ wrt [[Filtration]] $(\mathcal{B}_{n})$ s.t. $Z_{n} \in L^{1}$ $\forall n \in \mathbb{N}$. Then there exists a [[Martingale]] $(X_{n})$ and a [[Predictable Sequence]] $(U_{n})$ so that $$Z_{n} = X_{n} + U_{n}$$
## Proof
Let $Z_{0} := 0$ and let $\mathcal{B}_{0}$ be the [[Trivial Sigma Algebra]]. Consider the [[Discrete-Time Process]]es:
1. $u_{n}$ = $\mathbb{E}(Z_{n}|\mathcal{B}_{n-1}) - Z_{n-1}$
2. $d_{n} = Z_{n} - \mathbb{E}(Z_{n}|\mathcal{B}_{n-1})$

Let
1. $U_{n} = \sum\limits_{i=1}^{n} u_{n}$
2. $X_{n} = \sum\limits_{i=1}^{n} d_{n}$

We claim that $X_{n} + U_{n}$ is the decomposition we are looking for. Observe that by definition of [[Conditional Expectation]] and because $Z_{n-1} \in L^{0}(\mathcal{B}_{n-1})$, we know $u_{n} \in L^{0}(\mathcal{B}_{n-1})$ $\forall n \in \mathbb{N}$. Since $\mathcal{B}_{n}$ forms a [[Filtration]], we then know then that $\sigma(u_{i}) \subset \mathcal{B}_{i-1} \subset \mathcal{B}_{n-1}$ $\forall i \leq n$, so $u_{i} \in L^{0}(\mathcal{B_{n}})$. Thus $U_{n} \in L^{0}(\mathcal{B}_{n-1})$ and $U_{n}$ is a [[Predictable Sequence]].

Now consider $(d_{n})$. Observe that because [[Conditional Expectation is Linear]] and [[Conditioning on known information is Idempotent]], we have that
$$\mathbb{E}(d_{n} | \mathcal{B}_{n-1}) = \mathbb{E}(Z_{n} - \mathbb{E}(Z_{n}|\mathcal{B}_{n-1}) | \mathcal{B}_{n-1}) = \mathbb{E}(Z_{n} | \mathcal{B}_{n-1}) - \mathbb{E}(Z_{n}|\mathcal{B}_{n-1}) = 0$$
and $(d_{n})$ is a [[Martingale Difference Sequence]]. Recall that [[Accumulation of Martingale Difference Sequence is a Martingale]], so $X_{n}$ is a [[Martingale]] wrt [[Filtration]] $(\mathcal{B}_{n})$.

Finally, observe that
$$\begin{align*}
X_{n} + U_{n} &= \sum\limits_{i=1}^{n} d_{i} + \sum\limits_{i=1}^{n} u_{i}\\
&=\sum\limits_{i=1}^{n} Z_{i} - \mathbb{E}(Z_{i}|\mathcal{B}_{i-1}) + \mathbb{E}(Z_{i}|\mathcal{B}_{i-1}) - Z_{i-1}\\
&=Z_{n} - Z_{0}\\
&=Z_{n},
\end{align*}$$
completing the proof. $\blacksquare$

# Other Outlinks
- [[Random Variable]]