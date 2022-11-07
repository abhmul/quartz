---

title: "Tightly Bounded Set"

---
# Definition 1
Let $(M, d)$ be a [[Metric Space]] and let $A \subset M$. We say $A$ is a [[Tightly Bounded Set]] if$\sup\limits_{x,y \in A} d(x,y) < \infty$ and there exist $x',y' \in A$ s.t. $d(x',y') = \sup\limits_{x,y \in A} d(x,y)$. 
# Definition 2
Let $(X, ||\cdot||)$ be a [[Normed Vector Space]] and let $A \subset X$. We say $A$ is a [[Tightly Bounded Set]] if $\sup\limits_{x,y \in A} ||x-y|| < \infty$ and there exists $x',y' \in A$ so that $||x' - y'|| = \sup\limits_{x,y \in A}||x - y||$. 
## Remarks
1. Definition (1) $\Leftrightarrow$ Definition (2) in a [[Normed Vector Space]].

# Definition 3
Let $(X, \leq)$ be a [[Total Ordering]] endowed with the [[Order Topology]] and let $A \subset X$. We say $A$ is a [[Tightly Bounded Set]] if there exists $s,t \in A$ so that $A \subset [s,t]$. That is, for some $s,t \in A$,  $s \geq a \geq t$ for all $a \in A$.

## Remarks
1. Definitions (1) and (2) are carrying definition (3) over to sets that are not [[Total Ordering]]s by a [[Continuous Function]] into $\mathbb{R}$ (namely $d$). The [[Lower Bound]] is always achieved in a [[Metric Space]] because $d(x,x) = 0$ for any $x \in A$.
2. If $A$ is a [[Tightly Bounded Set]], this is equivalent $\sup\limits A \in A$ and $\inf\limits A \in A$. This is because $A$ contains is [[Upper Bound]] and its [[Lower Bound]] if it is [[Tightly Bounded Set]].
# Other Outlinks
- [[Closed Interval]]
- [[Supremum]]
- [[Infimum]]

