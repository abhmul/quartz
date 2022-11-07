---

title: "Nonempty Compact Sets are Tightly Bounded"

---
# Statement 1
Let $(Y, \leq)$ be a [[Total Ordering]] with the [[Order Topology]]. Let $K \subset Y$ be [[Nonempty]] and [[Compact]]. Then $K$ is a [[Tightly Bounded Set]].

## Proof
Consider $K$ as an [[Order-Preserving Net]] $(a_{a})_{a \in K} \subset K$. Since $K$ is [[Compact]] and [[A Set is Compact iff all Nets have a Convergent Subnet]], we know there exists a [[Cofinal Subset]] $S \subset K$ so that $(b_{b})_{b \in S}$ is a [[Net Convergence|convergent]] [[Subnet]]. It is [[Order-Preserving Net|order-preserving]] because its parent is. Because [[Order-Preserving Nets Converge to their Supremum]], we know $b_{b} \to \sup\limits_{b \in S} b_{b} = \sup\limits S$. Because [[Supremum of a Cofinal Subset is the Supremum of the Set]], it follows that $\sup\limits S = \sup\limits K$. Therefore $K$ has an [[Upper Bound]] (namely $\sup\limits K$). Since the [[Subnet]] [[Net Convergence|converges]] in $K$, we know $\sup\limits K \in K$. Because the [[Reverse Ordering generates same Topology]], we can apply the same argument on the [[Reverse Ordering]] to get $\inf\limits K \in K$. Therefore $K$ is a [[Tightly Bounded Set]]. $\blacksquare$

# Statement 2
[[TODO]] - the corresponding statement for [[Metric Space]]s

# Other Outlinks
- [[Empty Set]]
- [[Supremum]]
- [[Infimum]]