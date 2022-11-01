---
title: "Every Subsequence of a Convergent Sequence converges to the same Limit"
---

# Statement
Let $(a_{n}) \subset X$ be a sequence in [[Metric Space]] $(X, d)$. If $a_{n} \to a \in X$  every [[Subsequence]] of $(a_{n})$ [[Sequence Convergence|converges]] to $a$.

# Proof
Suppose $a_{n} \to a$. Let $(a_{n_{k}})$ be a [[Subsequence]] of $(a_{n})$. Since $a_{n} \to a$, we know $\forall \epsilon > 0$, $\exists \mathbb{N}\in N$ s.t. $\forall n \geq N$ we have that
$$d(a_{n}, a) < \epsilon$$
Let $K = \min\{k \in \mathbb{N} : n_{k} \geq N\}$. Then we have that 
$$d(a_{n_{k}}, a) < \epsilon$$
for all $k \geq K$ since $n_{k} \geq N$ by our choice of $K$. Thus $a_{n_{k}} \to a$ as well. $\blacksquare$
# Other Outlinks
- [[Natural Numbers]]
- [[Natural Numbers are Well-Ordered]]

# Encounters
1. [[Pugh - Real Mathematical Analysis]] - Ch 2, pg unknown