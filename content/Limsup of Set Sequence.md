---

title: "Limsup of Set Sequence"

---
Let $({A}_{n})_{n=1}^{\infty}$ be a [[Sequence]] of [[Set]]s. Then
$$\limsup\limits_{n \to \infty} A_{n} = \bigcap\limits_{n \in \mathbb{N}} \bigcup\limits_{k \geq n} A_{k}.$$

## Remarks
1. Since $\bigcup\limits_{k \geq n} A_{k} \supset \bigcup\limits_{k \geq n+1} A_{k}$ for any $n \in \mathbb{N}$, $(\bigcup\limits_{k \geq n} A_{k})_{n=1}^{\infty}$ is [[Non-Increasing Function]] and we can write $$\limsup\limits_{n \to \infty} A_{n} = \lim\limits_{n \to \infty} \bigcup\limits_{k \geq n} A_{k}.$$
2. If $x \in \limsup\limits_{n \to \infty} A_{n}$ [[If and Only If]] for every $n \in \mathbb{N}$ there exists $k \geq n$, s.t. $x \in A_{k}$ by definition of [[Set Union]] and [[Set Intersection]]. Thus $$\limsup\limits_{n \to \infty} A_{n} = \{x \in \bigcup\limits_{n \in \mathbb{N}} A_{n} : x \in A_{n} \text{ for infinitely many } n \in \mathbb{N}\}.$$
# Other Outlinks
- [[Set Union]]
- [[Set Intersection]]
- [[Limit of a Monotonic Set Sequence]]