---

title: "Supremum of an Increasing Function is Function of Supremum"

---
# Statement
Let $(X, \leq)$, $(Y, \leq)$ be [[Total Ordering]]s equipped with their respective [[Order Topology]]s and let $f: T \to S$ be a [[Continuous Function|continuous]]  [[Non-Decreasing Function]]. Let $A \subset T$ and suppose $\sup\limits A$ exists. Then
$$f(\sup\limits A) = \sup\limits f(A)$$
## Proof
Since $A$ is a [[Total Ordering]], it is also a [[Directed Partial Ordering]]. Thus, we can view $A$ as the [[Non-Decreasing Function|non-decreasing]] [[Net]] $(a_{a})_{a \in A}$. Since $\sup\limits A$ exists, we know $a_{a} \to \sup\limits A$ because [[Order-Preserving Nets Converge to their Supremum]]. Because [[A Function is Continuous iff it preserves Net Convergence]], $(f(a_{a}))_{a \in A} \to f(\sup\limits A)$. Since $f$ is [[Non-Decreasing Function|non-decreasing]], if $a \leq b \in A$, then $f(a_{a}) \leq f(b_{b})$. Therefore, $(f(a_{a}))_{a \in A}$ is a [[Non-Decreasing Function|non-decreasing]] [[Net]]. Since [[Order-Preserving Nets Converge to their Supremum]]\, we know $f(\sup\limits A) = \sup\limits_{a \in A} f(a_{a}) = \sup\limits f(A)$. $\blacksquare$

# Other Outlinks
- [[Function Image]]
- [[Supremum]]