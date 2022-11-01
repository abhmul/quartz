---

title: "Convergent Sequences are Cauchy"

---
# Statement
Let $(M, d)$ be a [[Metric Space]] and let $({x}_{n})_{n=1}^{\infty} \subset M$. If $x_{n} \to x \in M$, then $({x}_{n})_{n=1}^{\infty}$ is a [[Cauchy Sequence]].

## Proof
Let $\epsilon > 0$. Since $x_{n} \to x$, we can find $N \in \mathbb{N}$ so that $\forall n \geq N$, $d(x_{n}, x) < \frac{\epsilon}{2}$. Then $\forall n,m \geq N$, $$d(x_{n},x_{m}) \leq d(x_{n}, x) + d(x, x_{m}) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon,$$
so $({x}_{n})_{n=1}^{\infty}$ is a [[Cauchy Sequence]].

# Other Outlinks
- [[Sequence]]
- [[Sequence Convergence]]
- [[Natural Numbers]]
- [[Real Numbers]]