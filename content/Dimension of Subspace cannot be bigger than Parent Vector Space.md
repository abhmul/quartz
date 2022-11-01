---

title: "Dimension of Subspace cannot be bigger than Parent Vector Space"

---
# Statement
Let $V$ be a [[Vector Space]] and let $W \subset V$ be a [[Vector Subspace]] of $V$. Then $\dim W \leq \dim V$.

## Proof
First note that if $\dim V = \infty$, then this statement is trivially true since $\dim W \leq \infty$ is always true by definition of [[Dimension of a Vector Space]].

Suppose $\dim V = n < \infty$ for some $n \in \mathbb{N}$. First observe that any [[Linearly Independent]] $S \subset W$ is also a [[Linearly Independent]] $S \subset V$, since [[Linearly Independent|linear independence]] is only defined in terms of the vectors and underlying [[Field]]. Therefore, because [[Dimension of a Vector Space upper bounds Linearly Independent Set size]], we must have that $|S| \leq n$ for such $S$. Applying the process inremark (1) of [[Growing a Linearly Independent Set]] on $W$, we must terminate in at most $n$ steps. By that remark, we have that $R$ is a [[Vector Space Basis]] for $W$. Since $|R| \leq n$, $W$ is indeed a [[Finite-Dimensional Vector Space]] and $\dim W = |R| \leq n = \dim V$. $\blacksquare$

# Other Outlinks
- [[Natural Numbers]]