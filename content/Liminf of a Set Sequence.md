---

title: "Liminf of Set Sequence"

---
Let $({A}_{n})_{n=1}^{\infty}$ be a [[Sequence]] of [[Set]]s. Then
$$\liminf\limits_{n \to \infty} A_{n} = \bigcup\limits_{n \in \mathbb{N}} \bigcap\limits_{k \geq n} A_{k}.$$

## Remarks
1. Since $\bigcap\limits_{k \geq n} A_{k} \subset \bigcap\limits_{k \geq n+1} A_{k}$ for any $n \in \mathbb{N}$, $(\bigcap\limits_{k \geq n} A_{k})_{n=1}^{\infty}$ is [[Non-Decreasing Function]] and we can write $$\liminf\limits_{n \to \infty} A_{n} = \lim\limits_{n \to \infty} \bigcap\limits_{k \geq n} A_{k}.$$
2. $x \in \liminf\limits_{n \to \infty} A_{n}$ [[If and Only If]] there exists an $n \in \mathbb{N}$ so that $\forall k \geq n$, $x \in A_{k}$ by definition of [[Set Union]] and [[Set Intersection]]. Thus $$\liminf\limits_{n \to \infty} A_{n} = \{x \in \bigcup\limits_{n \in \mathbb{N}} A_{n} : x \not\in A_{n} \text{ for finitely many } n \in \mathbb{N}\}$$
# Other Outlinks
- [[Set Union]]
- [[Set Intersection]]
- [[Limit of a Monotonic Set Sequence]]
- [[Finite Set]]