---

title: "Restricting an Extended Norm to elements of Finite Norm form a Normed Vector Space"

---
# Statement
Let $V$ be a [[Vector Space]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. Suppose $||\cdot||: V \to \overline{\mathbb{R}_{\geq0}}$ is an [[Extended Norm]] on $V$. Then 
$$X := \{x \in V : ||x|| < \infty\}$$
is a [[Normed Vector Space]] and a [[Vector Subspace]] of $V$.

## Proof
We can quickly see that $X$ is a [[Vector Subspace]] of $V$ because for $c \in \mathbb{K}$ and $u,v \in X$:
$$||c u + v || \leq |c| ||u|| + ||v|| < \infty.$$
Thus, $cu + v \in X$ and $X$ is a [[Vector Subspace]] because [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]]. This also makes $X$ a [[Vector Space]] in its own right.

It follows that $X$ is a [[Normed Vector Space]] because [[Finite Set|finiteness]] is preserved by the 3 defining [[Axiom]]s of a [[Norm]]. $\blacksquare$

# Other Outlinks
- [[Extended Real Numbers]]