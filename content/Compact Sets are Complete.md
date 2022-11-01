---

title: "Compact Sets are Complete"

---
# Statement 1
Let $(K, \leq)$ be a [[Total Ordering]] equipped with the [[Order Topology]] that is [[Compact]]. Then it is a [[Complete Ordering]].

## Proof
Let $A \subset K$ be [[Upper Bound|bounded from above]]. Consider $A$ as a [[Order-Preserving Function|monotone]] [[Net]], $(a_{a})_{a \in A} = A$. Because $K$ is [[Compact]] and [[A Set is Compact iff all Nets have a Convergent Subnet]], we know there exists a [[Cofinal Subset]] $S \subset A$ so that $(b_{b})_{b \in S}$ is a [[Net Convergence|convergent]] [[Subnet]]. It is [[Order-Preserving Function|montone]] because its parent is. Because [[Monotone Nets Converge to their Supremum]], we know $b_{b} \to \sup\limits_{b \in S} b_{b} := z$. We claim $a_{a} \to z$. Let $U \subset K$ be [[Open]] so that $z \in U$. [[Without Loss of Generality]] we can let it be an [[Open Interval]] (including [[Open Ray]]s and $K$). Because $b_{b} \to z$, we know that there is a $b_{0}$ so that for all $b \in S$ so $b \geq b_{0}$, $b \in U$. Since $U$ is an [[Open Interval]] that contains $b_{0}$ and $z$, $[b_{0}, z] \subset U$. Suppose $a \in A$ so that $a \geq b_{0}$. We can't have $a > z$, because $S$ is a [[Cofinal Subset]] of $A$. Thus $a \in [b_{0},z]$, so $a \in U$. Since $U$ was arbitrary, we have that $a_{a} \to z$. Since [[Monotone Nets Converge to their Supremum]], we know $\sup\limits_{a \in A} a = z$. $\blacksquare$