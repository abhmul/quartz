---

title: "Compact Sets are Bounded"

---
# Statement
Let $(Y, \leq)$ be a [[Total Ordering]] with the [[Order Topology]]. Let $K \subset Y$ be [[Compact]]. Then $K$ is a [[Bounded Set]].

## Proof
If $K = \emptyset$, it is vacuously a [[Bounded Set]]. Otherwise, consider the [[Order-Preserving Function|monotone]] [[Net]] $(y_{y})_{y \in K} = K$. This is a [[Net]] because $K$ is [[Total Ordering|totally ordered]] and a [[Total Ordering]] is a [[Directed Partial Ordering]]. Suppose $K$ was not [[Bounded Set|bounded]] and it is not [[Upper Bound|bounded from above]].  Recall [[A Set is Compact iff all Nets have a Convergent Subnet]]. Therefore $(y_{y})_{y \in K}$ must have a [[Net Convergence|convergent]] [[Subnet]], $(y_{\beta})_{\beta \in S}$ (where $S \subset K$ is a [[Cofinal Subset]]). Call the [[Net Convergence|limit]] of this [[Subnet]] $z$. Since $(y_{\beta})_{\beta \in S}$ is a [[Order-Preserving Function|monotone]] [[Net]], we know $\sup\limits_{\beta \in S} y_{\beta} = z$ because [[Monotone Nets Converge to their Supremum]]. But $K$ has no [[Upper Bound]], so there exists $y_{0} \in K$ so that $y_{0} > z$. Because $(y_{\beta})_{\beta \in S}$ is a [[Subnet]], there exists $\beta \in S$ so that $y_{\beta} = \beta \geq y_{0}$. But then $y_{\beta} > z =\sup\limits_{\beta \in S} y_{\beta}$ $\unicode{x21af}$. If $K$ instead had no [[Lower Bound]], then we could apply the same argument to $K$ under the [[Reverse Ordering]], since the [[Reverse Ordering generates same Topology]]. Therefore $K$ is [[Bounded Set|bounded]]. $\blacksquare$
