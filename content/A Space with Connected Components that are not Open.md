---

title: "A Space with Connected Components that are not Open"

---
# Example
Consider $\mathbb{Q}$ equipped with the [[Subspace Topology]] of [[Euclidean Space]]. Then no [[Connected Component]] of $\mathbb{Q}$ is [[Open]].

## Proof
Singletons are always [[Connected]]. If $S \subset \mathbb{Q}$ s.t. $|S| \geq 2$, then there exist distinct [[Rational Numbers]] $p< q \in S$. By [[Irrationals are Dense in Reals]], there exists an $r \not\in \mathbb{Q}$ so that $p < r < q$. Thus, if we take $U = (-\infty, r)$ and $V = (r, \infty)$,
1. $p \in U \cap S, q \in V \cap S$, so both are non-trivial
2. $U \cap V = \emptyset$
3. $(U \cup V) \cap S = S$

Thus $U, V$ disconnect $S$ and $S$ is not [[Connected]]. So every singleton in $\mathbb{Q}$ is a [[Connected Component]]. None of them are [[Open]] because every [[Open]] $U \subset \mathbb{R}$ contains an [[Interval]], which contains [[Infinite Set|infinitely]] many [[Rational Numbers]]s (because [[Rationals are Dense in the Reals]]). $\blacksquare$

## Source
- https://math.stackexchange.com/a/1306391/706719