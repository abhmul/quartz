---

title: "A Vector Space is Infinite-Dimensional iff its Linearly Independent Set Size is Unbounded"

---
# Statement
Let $V$ be a [[Vector Space]]. Then $V$ is an [[Infinite-Dimensional Vector Space]] [[If and Only If]] for any $n \in \mathbb{N}$, there exists some $S \subset V$ so that $|S| > n$.

## Proof
We prove the [[Contraposition]] instead:

$(\Rightarrow)$ Suppoes $\exists n \in \mathbb{N}$ so that for all [[Linearly Independent]] $S \subset V$, we have $|S| \leq n$. We know such a [[Linearly Independent]] [[Set]] exists since [[The Empty Set is Linearly Independent]].  Now pick any such $S$. Run the process of [[Growing a Linearly Independent Set]] over $V$. This process must terminate in at most $n$ steps. This gives us a [[Maximal]] [[Linearly Independent]] [[Set]]. By [[A Set is a Basis iff it is a Maximal Linearly Independent Set]], we have exhibited a [[Finite Set|finite]] [[Vector Space Basis]] for $V$, and $V$ is a [[Finite-Dimensional Vector Space]]. $\checkmark$

($\Leftarrow$) Suppose $V$ is a [[Finite-Dimensional Vector Space]]. Then there exists a [[Vector Space Basis]] $S \subset V$ so that $S$ is a [[Finite Set]]. Since [[Spanning Set Size bound Linearly Independent Set Size]], we have that for all [[Linearly Independent]] $R \subset V$, $|R| \leq |S| =: n \in \mathbb{N}$. $\checkmark$ $\blacksquare$

[[TODO]] - do by [[Contraposition]]
- [[A Set is a Basis iff it is a Maximal Linearly Independent Set]]
- [[Spanning Set Size bound Linearly Independent Set Size]]