---

title: "Limsup of Indicator Sequence is Indicator of Limsup"

---
# Statement
Let $({A}_{n})_{n=1}^{\infty} \subset X$ be a [[Sequence]] of [[Set]]s. Then
$$\limsup\limits_{n \to \infty} \mathbb{1}_{A_{n}} = \mathbb{1}_{\limsup\limits_{n \to \infty} A_{n}}.$$
## Proof
Observe that if $x \in \limsup\limits_{n \to \infty} A_{n}$, then $\forall n  \in \mathbb{N}$, there exists $k \geq n$ so that $x \in A_{k}$. Therefore, $\sup\limits_{k \geq n} \mathbb{1}_{A_{k}} = 1$ $\forall n \in \mathbb{N}$. Then, $\limsup\limits_{n \to \infty} \mathbb{1}_{A_{n}}= \lim\limits_{n \to \infty} \sup\limits_{k \geq n} \mathbb{1}_{A_{k}} = \lim\limits_{n \to \infty} 1 = 1$. On the other hand, if $x \not\in \limsup\limits_{n \to \infty} A_{n}$, then there exists $n \in \mathbb{N}$ s.t. $\forall k \geq n$, $x \not\in A_{k}$. But then for any $m \geq n$, $k \geq m \geq n$ is s.t. $x \not\in A_{k}$. Then $\sup\limits_{k \geq m} \mathbb{1}_{A_{k}} = 0$ $\forall m \geq n$. Then $\limsup\limits_{n \to \infty} \mathbb{1}_{A_{n}} = \lim\limits_{n \to \infty} \sup\limits_{k \geq n} \mathbb{1}_{A_{k}} = \lim\limits_{n \to \infty} 0 = 0$. Therefore
$$\limsup\limits_{n \to \infty} \mathbb{1}_{A_{n}} = \mathbb{1}_{\limsup\limits_{n \to \infty} A_{n}}.$$
$\blacksquare$
# Other Outlinks
- [[Indicator Function]]
- [[Limsup of Set Sequence]]
- [[Limsup of Sequence]]