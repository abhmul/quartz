---

title: "Borel-Cantelli Lemma"

---
# Statement
Let $(X, \mathcal{M}, \mu)$ be a [[Measure Space]] and let $({A}_{n})_{n=1}^{\infty} \in \mathcal{M}$. If 
$$\sum\limits_{n=1}^{\infty} \mu(A_{n}) < \infty$$ then 
$$\mu(\limsup\limits_{n \to \infty} A_{n}) = 0$$
## Proof 1
Since [[Convergence of Series implies tail goes to 0]], we have that
$$\begin{align*}
0 &=  \lim\limits_{n \to \infty} \sum\limits_{k=n}^{\infty} \mu(A_{k})\\
&\geq  \lim\limits_{n \to \infty} \mu(\bigcup\limits_{k \geq n}A_{k}) & \text{(subadditivity)}\\
&=\mu(\limsup\limits_{n \to \infty} A_{n}) &\text{(continuity from above)}.
\end{align*}$$
where [[Continuity of Measures from Above]] holds because for $\epsilon = 1$, there exists $N \in \mathbb{N}$ so that $\forall n \geq N$, $\mu(\bigcup\limits_{k \geq n}A_{k}) \leq 1$.

## Proof 2
[[TODO]] - from [[Durret - Probability Theory and Examples]], uses [[Fubini's Theorem]] and sum of [[Indicator Function]]s.

## Remarks
1. In the context of [[Probability Measure]]s, we might write $\mathbb{P}(A_{n} \text{ i.o.}) = 0$.

# Other Outlinks
- [[Limsup of Set Sequence]]