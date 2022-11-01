---
title: "A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition"
---

# Statement
$W$ is a [[Vector Subspace]] of $V$ [[If and Only If]] $c u + v \in W$ for all $c \in F$ and $u, v \in W$.
## Proof
$(\Rightarrow)$: If $W$ is a [[Vector Subspace]] of $V$, then it is a [[Vector Space]] itself and $c u + v \in W$ by closure of $W$ under $+$ and $*$. $\checkmark$

$(\Leftarrow)$: We simply check that $W$ is a [[Vector Space]] in its own right since we already know $W \subset V$. We let $c, d \in F$ and $u, v, w \in W$ be arbitrary.
1. [[Abelian Group]]:
	1. $W \ni (-1) u + u = \mathbf{0}$ because [[Scalar product with -1 is additive inverse in vector spaces]]
	2. $W \ni 1 * u + v = u + v = v + u$, so [[Commutativity]] is satisfied by inheritance from $V$. This also establishes that $+$ is well-defined when restricted to $W$
	3. $W \ni 1 * u + (1 * v + w) = u + (v + w) = (u + v) + w$, so [[Associativity]] is satisfied by inheritance from $V$.
	4. $W \ni (-1) * u + \mathbf{0} = -u$, so $W$ contains [[Additive Inverse]]s
2. Compatibility with [[Scalar Multiplication]]. Note that $W \ni c * u + \mathbf{0} = c * u$, so $*$ is well-defined when restricted to $W$.
	1. $1 * u = u$, by inheritance from $V$.
	2. $(cd)*u = c * (d * u)$, by inheritance from $V$.
	3. $(c + d) * u = c * u + d * u$ by inheritance from $V$.
	4. $c * (u + v) = c * u + c * v$ by inheritance from $V$

Thus $+$ and $*$ are well-defined when restricted to $W$, and $W$ is a [[Vector Space]]. $\blacksquare$

## Remarks
1. This provides an alternate definition for [[Vector Subspace]].