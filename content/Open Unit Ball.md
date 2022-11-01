---

title: "Open Unit Ball"

---
# Definition
Let $(X, ||\cdot||)$ be a [[Normed Vector Space]]. Then the [[Open Unit Ball]] is the [[Open Ball]] of radius $1$ about $0 \in X$. It is usually denoted $B(X)$

## Remarks
1. $B(X) := \{x \in X : ||x - 0|| < 1\} = \{x \in X : ||x|| < 1\}$.
2. Let $r > 0$ and $x \in X$. Then $B_{r}(x) = rB(X) + x$. 
	**Proof**: Let $x' \in B_{r}(x)$, observe that $x' = r\frac{x'-x}{r} + x$. Furthermore, $||x' - x|| < r$, so $||\frac{x'-x}{r}|| < 1$, giving us $\frac{x'-x}{r} \in B(X)$. Thus $B_{r}(X) \subset rB(X) + x$. On the other hand, let $x' \in B(X)$. Then $||(rx' + x) - x|| = ||rx'|| = r||x'|| < r$. Thus, $rx' + x \in B_{r}(X)$ and $B_{r}(X) \supset rB(X) + x$. $\blacksquare$

