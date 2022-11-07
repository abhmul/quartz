---

title: "Closed Subset of a Complete Space is Complete"

---
# Statement 1
Let $(X, d)$ be a [[Complete Metric Space]]. Suppose $C \subset X$ is [[Closed]]. Then $(C, d {\big|}_{C \times C})$ is a [[Complete Metric Space]]. 

## Proof 
[[TODO]]
- [ ] [[A Set is Closed in a Metric Space iff it contains all its Sequential Limits]]
- [ ] definition of [[Complete Metric Space]]

# Statement 2
Let $(X, \leq)$ be a [[Complete Ordering]] equipped with the [[Order Topology]]. Suppose $C \subset X$ is [[Closed]]. Then $(C, \leq {\big|}_{C \times C})$ is a [[Complete Ordering]]. 

## Proof
If $C = \emptyset$ then this is vacuously true. Otherwise, assume $C \neq \emptyset$. Let $A \subset C$ be [[Nonempty]] be [[Upper Bound|bounded from above]]. Since $X$ is a [[Complete Ordering]] we know $\sup\limits A$ exists. Since a [[Supremum is in the Closure of a Nonempty Set]], we know $\sup\limits A \in \text{cl} A$. Because [[Closure is Monotonic]], $\text{cl} A \subset C$ and $\sup\limits A \in C$. Therefore $(C, \leq {\big|}_{C \times C})$ is a [[Complete Ordering]]. $\blacksquare$


# Other Outlinks
- [[Subspace Metric Space]]
- [[Empty Set]]
- [[Nonempty]]