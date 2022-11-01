---
title: "Equivalent Conditions for Convexity"
---

# Statement
Suppose $V$ is a [[Vector Space]] of $\mathbb{R}$ and $f: V \to \mathbb{R}$. Then [[The following are Equivalent]]:
1. $f$ is a [[Convex Function]]
2. The [[Epigraph]] of $f$, $\text{Epi}(f) \subset V \times \mathbb{R}$ (endowed with the [[Product Vector Space]]), is a [[Convex Set]].
3. (Check this - [[TODO]]) [[First Order Condition for Convexity]]: Further suppose $V$ is a [[Normed Vector Space]] and $f$ has [[Frechet Derivative]] $D_{v} f$ at all $v \in V$. For all $x, y \in V$ $$f(x) + D_{x}f(y-x) \leq f(y)$$
4. (Check this - [[TODO]]) [[Second Order Condition for Convexity]]: Further  suppose $V$ is a [[Normed Vector Space]]  and $f$ has 2nd [[Frechet Derivative]] $D_{v}^{2}f$ at all $v \in V$. For all $x, y \in V$ $$D^{2}_{x}f(y)(y) \geq 0$$
5. (Check this - [[TODO]]) $\forall b \in \mathbb{R}$ , $\{x \in V: f(x) \leq b\}$ is a [[Convex Set]].
	- I think it is easiest to prove equivalence with (2). Do not (2) $\Rightarrow$ not (5), then (2) $\Rightarrow$ (5).
	- This makes it easy to prove [[Norms are Convex]] since it would follow from [[Balls are Convex]]
## Proof
(1) $\Rightarrow$ (2): Suppose $(u, a), (v, b) \in \text{Epi}(f)$. Then $f(u) \leq a$ and $f(v) \leq b$. Let $\lambda \in [0,1]$. Then $$f(\lambda u + (1-\lambda)v) \leq \lambda f(u) + (1-\lambda) f(v) \leq \lambda a + (1- \lambda) b$$  so $$\Big( \lambda u + (1- \lambda) v, \lambda a + (1-\lambda)b \Big) = \lambda (u, a) + (1- \lambda) (v, b) \in \text{Epi}(f)$$ and $\text{Epi}(f)$ is a [[Convex Set]]. $\checkmark$

(2) $\Rightarrow$ (1): Suppose $u, v \in V$ and $\lambda \in [0,1]$. Then, by definition of [[Epigraph]], $(u, f(u)), (v, f(v)) \in \text{Epi}(f)$. Since $\text{Epi}(f)$ is [[Convex Set|Convex]], we know $$S \ni \lambda (u, f(u)) + (1 - \lambda) (v, f(v)) = \Big(\lambda u + (1- \lambda)v, \lambda f(u) + (1- \lambda)f(v)\Big)$$ Thus, by definition of [[Epigraph]], we have that $$f(\lambda u + (1-\lambda)v) \leq \lambda f(u) + (1-\lambda) f(v)$$ and $f$ is a [[Convex Function]]. $\checkmark$
