---

title: "Sigma Field up to Constant Stopping Time is just the Sigma Field at that time"

---
# Statement
Let $\mathcal{F} = \{\mathcal{B}_{n} : n \in \mathbb{N}\}$ be a [[Discrete-Time Filtration]] over $\Omega$, let $k \in \bar{\mathbb{N}}$, and let $\nu : \Omega \to \bar{\mathbb{N}}$ be the [[Stopping Time]] on $\mathcal{F}$ defined as $\nu(\omega) = k$. Then $\mathcal{B}_{\nu} = \mathcal{B}_{k}$.

## Proof
Suppose $A \in \mathcal{B}_{\nu}$. Then $\forall n \in \bar{\mathbb{N}}$, $A \cap [\nu = n] \in \mathcal{B}_{n}$. Note that $$[\nu = n] = \begin{cases} \emptyset &\text{if }n \neq k\\
\Omega &\text{if }n=k
\end{cases}$$ so $\mathcal{B}_{k} \ni A \cap [\nu = k] = A$ and $\mathcal{B}_{\nu}\subset \mathcal{B}_{k}$. $\checkmark$

On the other hand, if $B \in \mathcal{B}_{k}$, then $B \in \mathcal{B}_{\infty} \supset \mathcal{B}_{k}$. Observe that $B \cap [\nu = k] = B \in \mathcal{B}_{k}$ by construction and $B \cap [\nu = n] = \emptyset \in \mathcal{B}_{n}$ by definition of [[Sigma Algebra]], for $n \neq k$. Thus, $B \in \mathcal{B}_\nu$ and $B_{\nu} \supset \mathcal{B}_{k}$. $\checkmark$

Therefore $\mathcal{B}_{\nu}= \mathcal{B}_{k}$. $\blacksquare$


# Other Outlinks
- [[Sigma Field up to Stopping Time]]