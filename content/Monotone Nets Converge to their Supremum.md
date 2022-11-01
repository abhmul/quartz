---

title: "Monotone Nets Converge to their Supremum"

---
# Statement
Let $(X, \leq)$ be a [[Total Ordering]] with the [[Order Topology]]. Let $(x_{\alpha})_{\alpha \in A} \subset X$ be an [[Order-Preserving Function|monotone]] [[Net]] on $X$. Then $\sup\limits_{\alpha \in A}x_{\alpha}$ exists [[If and Only If]] $(x_{\alpha})_{\alpha \in A}$ converges in $X$. In that case $\sup\limits_{\alpha \in A} x_{\alpha}$ is the [[Net Convergence|limit]].

## Proof
($\Rightarrow$): Let $L = \sup\limits_{\alpha \in A} x_{\alpha}$. We will show $x_{\alpha} \to L$. Suppose $U \subset X$ is [[Open]] and $U \ni L$. Then there exists $(c, d) \subset U$ so that $c < L < d$ (where we can have $c =  \leftarrow$ or $d = \rightarrow$) because $X$ is an [[Order Topology]]. Because $L$ is the [[Supremum]], $c$ is not an [[Upper Bound]] for $(x_{\alpha})_{\alpha \in A}$, so there exists $\alpha_{0} \in A$ so that $x_{\alpha_{0}} \geq c$. Since $(x_{\alpha})_{\alpha \in A}$ is [[Order-Preserving Function|monotone]], if $\alpha \geq \alpha_{0}$, then $L \geq x_{\alpha} \geq x_{\alpha_{0}} \geq c$. Thus, $x_{\alpha} \in (c,d) \subset U$ for all $\alpha \geq \alpha_{0}$ and $x_{\alpha} \to L$. $\checkmark$

$(\Leftarrow)$: Suppose $x_{\alpha} \to L$. If there was $\alpha_{0} \in A$ so that $x_{\alpha_{0}} > L$, then for all $\beta \geq \alpha_{0}$, $L \in ( \leftarrow, x_{\alpha_{0}}) \not\ni x_{\beta}$ since $x_{\beta} \geq x_{\alpha_{0}}$. Thus, we would have $x_{\alpha} \not\to L$ $\unicode{x21af}$. Therefore, we know for all $\alpha \in A$, $x_{\alpha} \leq L$ and $L$ is an [[Upper Bound]] for $\{x_{\alpha}\}_{\alpha \in A}$. Suppose $b \in X$ so that $b$ is an [[Upper Bound]] of $\{x_{\alpha}\}_{\alpha \in A}$ and $b < L$. Then $L \in (b, \rightarrow) \not\ni x_{\alpha}$ for all $\alpha \in A$. Thus, $x_{\alpha} \not\to L$ $\unicode{x21af}$. Therefore, we have $L = \sup\limits_{\alpha \in A}x_{\alpha}$. $\checkmark$
$\blacksquare$