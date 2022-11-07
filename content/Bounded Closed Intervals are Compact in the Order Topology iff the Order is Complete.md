---

title: "Bounded Closed Intervals are Compact in the Order Topology iff the Order is Complete"

---
# Statement

Let $(X, \leq)$ be a [[Total Ordering]] endowed with the [[Order Topology]]. Then for $a,b \in X$, $[a,b]$ is [[Compact]] [[If and Only If]] $(X, \leq)$ is a [[Complete Ordering]].

## Proof

$(\Leftarrow)$: Let $a,b \in X$. $[a,b]$ is a [[Tightly Bounded Set]]. $[a,b]$ is also [[Closed]] since [[Closed Intervals are Closed]]. Recall [[Closed Subset of a Complete Space is Complete]] and [[A Nonempty Set is Compact in the Order Topology iff it is Tightly Bounded and Complete]], so $[a,b]$ is [[Compact]] $\checkmark$.

$(\Rightarrow)$: Let $A \subset X$ be a [[Nonempty]] [[Bounded Set]]. Suppose $a \in A$ and $b \geq A$, and let $S := A \cap [a,b]$. We see $\sup\limits S \in S$ because $[a,b]$ is [[Compact]] and [[Compact Spaces are Complete]]. $S$ is a [[Cofinal Subset]] of $A$ (either $x < a$ or $x \in [a,b]$ for $x \in A$). Because [[Supremum of a Cofinal Subset is the Supremum of the Set]], $\sup\limits A = \sup\limits S$. Therefore $\sup\limits A$ exists. Since $A$ was arbitrary, $(X, \leq)$ is a [[Complete Ordering]] $\checkmark$. $\blacksquare$

# Other Outlinks
- [[Supremum]]