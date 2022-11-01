---

title: "Topological Manifolds have Countably many Connected Components"

---
# Statement
Let $M$ be a [[Topological Manifold]] of [[Manifold Dimension]] $n$. $M$ has [[Countable|countably]] many [[Connected Component]]s.

## Proof
Because
- [[Topological Manifolds are Locally Path-Connected]]
- [[Connected Components of Locally Path-Connected Spaces are Open]]
- [[Connected Components Partition the Space]]

we have that our [[Connected Component]]s form an [[Open Cover]] of $M$, which we denote as $\mathcal{C}$. Because $M$ is [[Second Countable]] by definition and [[Open Covers in a Second Countable space reduce to a Countable Subcover]], we can find an [[Open Subcover]] of [[Connected Component]]s $\mathcal{C}' \subset \mathcal{C}$. Since $\mathcal{C}$ is a [[Partition]] of $M$, if $\mathcal{C}' \subsetneq \mathcal{C}$, there would be some partition set of $\mathcal{C}$ not included and $\mathcal{C}'$, but then $\mathcal{C}'$ would not be an [[Open Cover]]. Thus $\mathcal{C}' = \mathcal{C}$. $\blacksquare$