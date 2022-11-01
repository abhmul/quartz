---

title: "Bounded Set"

---
# Definition 1
Let $(M, d)$ be a [[Metric Space]] and let $A \subset M$. We say $A$ is a [[Bounded Set]] if $\sup\limits_{x,y \in A} d(x,y) < \infty$. 
# Definition 2
Let $(X, ||\cdot||)$ be a [[Normed Vector Space]] and let $A \subset X$. We say $A$ is a [[Bounded Set]] if $\sup\limits_{x \in A} ||x|| < \infty$. 
## Remarks
1. Definition (1) $\Leftrightarrow$ Definition (2) in a [[Normed Vector Space]]: Suppose $\sup\limits_{x \in A} ||x|| < \infty$. Note $\sup\limits_{x,y \in A} ||x-y|| \leq \sup\limits_{x,y \in A} ||x|| + ||y|| \leq 2\sup\limits_{x \in A} ||x|| < \infty$. On the other hand, suppose $r := \sup\limits_{x,y \in A} ||x-y|| < \infty$. For any $x \in A$, $A \subset B_{r}(x)$. But then, $B_{r}(x) \subset (r + ||x||)B(X)$. Thus $\sup\limits_{y \in A} ||y|| < r + ||x|| < \infty$. $\blacksquare$

# Definition 3
Let $(X, \leq)$ be a [[Total Ordering]] endowed with the [[Order Topology]] and let $A \subset X$. We say $A$ is a [[Bounded Set]] if there exists $s,t \in X$ so that $A \subset [s,t]$. That is,  $s \geq a \geq t$ for all $a \in A$.

## Remarks
1. Definitions (1) and (2) are carrying definition (3) over to sets that are not [[Total Ordering]]s by a [[Continuous Function]] into $\mathbb{R}$ (namely $d$ and $||\cdot||$).

# Other Outlinks
- [[Closed Interval]]