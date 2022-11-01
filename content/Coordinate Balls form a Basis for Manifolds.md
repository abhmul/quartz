---

title: "Coordinate Balls form a Basis for Manifolds"

---
# Statement
Let $M$ be a [[Topological Manifold]] of [[Manifold Dimension]] $n$. Then $$\mathcal{B} := \{B \subset M : B \text{ is a coordinate ball}\}$$ is a [[Topological Basis]] for $M$.

## Proof
We will carry over the defining [[Topological Basis]] from $\mathbb{R}^{n}$. Suppose $U \subset M$ is [[Open]]. Let $(V, \varphi)$ be any [[Coordinate Chart]] of $M$. Because $\varphi$ is a [[Homeomorphism]] and [[A Function is a Homeomorphism iff it is a Bijective Continuous Open Map]], $\varphi(V \cap U)$ is [[Open]] in $\mathbb{R}^{n}$. Thus it can be written as a [[Set Union]] of [[Open Ball]]s (by definition of [[Metric Topology]]). Thus $V \cap U$ can be written as a [[Set Union]] of [[Coordinate Ball]]s. Since $(V, \varphi)$ was arbitrary, $U$ can be written as a [[Set Union]] of [[Coordinate Ball]]s (from potentially multiple different [[Coordinate Chart]]s). Since $U$ was arbitrary, we see that [[Coordinate Ball]]s form a [[Topological Basis]] for $M$. $\blacksquare$

