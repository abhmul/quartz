---

title: "Continuous Mapping Theorem"

---
# Statement
Let $({X_n}_{n})_{n=0}^{\infty}$ be a [[Sequence]] of [[Random Variable]]s such that 
$$X_{n} \Rightarrow X_{0}.$$
Assume $F_{n}$ is the [[Probability Distribution Function]] for $X_{n}$ for $n \geq 0$. Let $h: \mathbb{R} \to \mathbb{R}$ be s.t.
$$\mathbb{P}[X_{0} \in \text{Disc}(h)] = 0.$$
Then
$$h(X_{n}) \Rightarrow h(X_{0}).$$
If $h$ is [[Bounded Function|bounded]], then
$$\mathbb{E}(h(X_{n})) = \int\limits h(x) F_{n}(dx) \to \mathbb{E}(h(X_{0})) = \int\limits h(x) F_{0}(dx)$$

## Proof
[[TODO]]
- [[Baby Skorohod Theorem]]

See [[Resnick - A Probability Path]] Cor 8.3.1 pg 261