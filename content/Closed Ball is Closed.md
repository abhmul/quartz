---

title: "Closed Ball is Closed"

---
# Statement
Let $(M, d)$ be a [[Metric Space]]. Let $x \in M$ and $\epsilon > 0$. Then $\overline{B_{\epsilon}(x)}$ is [[Closed]].

## Proof
Consider $\overline{B_{\epsilon}(x)}^{C} = \{x' \in M: d(x', x) > \epsilon\}$. For any $x'$ in this [[Set]], let $\delta := d(x', x) - \epsilon$. If $y \in B_{\delta}(x')$, then $$d(x, y) + d(x, x') - \epsilon = d(x, y) + \delta > d(x, y) + d(y, x') \geq d(x, x').$$
Therefore, $d(x, y) > \epsilon$. Thus $B_\delta(x') \subset \overline{B_{\epsilon}(x)}^{C}$. Because [[A Set is Open in the Metric Topology iff it contains a Ball around each Point]], $\overline{B_{\epsilon}(x)}^{C}$ is [[Open]]. Therefore $\overline{B_{\epsilon}(x)}$ is [[Closed]]. $\blacksquare$

# Other Outlinks
- [[Closed Ball]]
- [[Open Ball]]