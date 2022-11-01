---

title: "A Set is Open in the Metric Topology iff it contains a Ball around each Point"

---
# Statement
Let $(M, d)$ be a [[Metric Space]] endowed with the [[Metric Topology]]. $U \subset M$ is [[Open]] [[If and Only If]] $\forall x \in U$, there exists $\epsilon > 0$ s.t. $B_{\epsilon}(x) \subset U$.

## Proof
($\Rightarrow$): Since we are in the [[Metric Topology]], there exists [[Index Set]] $I$ and $\{B_{\epsilon_\alpha}(x_\alpha)\}_{\alpha \in I}$ so that 
$$U = \bigcup\limits_{\alpha \in I} B_{\epsilon_\alpha}(x_\alpha)$$
Let $y \in U$. Then there exists $\alpha \in I$ so that $y \in B_{\epsilon_\alpha}(x_\alpha)$. Now apply [[Finite Intersections of Open Balls contain Open Balls about each point]] to $B_{\epsilon_\alpha}(x_\alpha) \cap B_{\epsilon_\alpha}(x_\alpha)$ to get $\zeta > 0$ so that $B_{\zeta}(y) \subset B_{\epsilon_\alpha}(x_{\alpha}) \subset U$. $\checkmark$

$(\Leftarrow)$: Let $\epsilon_{x} > 0$ be such that $B_{\epsilon_{x}}(x) \subset U$ for all $x \in U$. Then $\bigcup\limits_{x \in U}B_{\epsilon_{x}}(x) = U$. Since $B_{\epsilon_{x}}(x)$ is [[Open]] for each $x \in U$, $U$ is [[Open]]. $\checkmark$ $\blacksquare$

# Other Outlinks
- [[Open Ball]]
- [[Real Numbers]]
- [[Set Intersection]]