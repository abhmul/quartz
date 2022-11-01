---

title: "Partial Converse of Borel-Cantelli Lemma"

---
# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and suppose $({A}_{n})_{n=1}^{\infty} \subset \mathcal{B}$ is a [[Sequence]] of [[Independence|independent events]]. If $$\sum\limits_{n=1}^{\infty} \mathbb{P}(A_{n}) = \infty$$
then 
$$\mathbb{P}(A_{n} \text{ i.o. }) = 1$$
## Proof
Observe that for any $M \in \mathbb{N}$
$$\begin{align*}
\mathbb{P}(\bigcap\limits_{k \geq M} A_{k}^{C}) &= \prod\limits_{k=M}^{\infty} \mathbb{P}(A_{k}^{C})\\
&=\prod\limits_{k=M}^{\infty} (1 - \mathbb{P}(A_{k}))\\
&\leq \prod\limits_{k=M}^{\infty} \exp(- \mathbb{P}(A_{k})) \tag{3}\\
&=\exp\left(-\sum\limits_{n=M}^{\infty} \mathbb{P}(A_{n})\right)\\
&= 0 \tag{5}
\end{align*}$$
where at (3) we used the fact that $1 - x \leq e^{-x}$ and at (5) we used the [[Continuity of Exponentiation]]. Therefore,
$$\begin{align*}
\mathbb{P}(\limsup\limits_{n \to \infty} A_{n}) &=  \lim\limits_{n \to \infty} \mathbb{P}(\bigcup\limits_{k \geq n} A_{n}) & \text{(continuity from above)}\\
&=\lim\limits_{n \to \infty} (1 - \mathbb{P}(\bigcap\limits_{k \geq n} A_{n}^{C})) &\text{De Morgan's Law}\\
& =\lim\limits_{n \to \infty} 1\\
&= 1
\end{align*}$$
$\blacksquare$
# Other Outlinks
- [[Limsup of Set Sequence]]
- [[Linear and Exponential Inequality]]
- [[Continuity of Measures from Above]]
- [[De Morgan's Law]]