---

title: "Metrics are Continuous"

---
# Statement
Suppose $(M, d)$ is a [[Metric Space]]. Then $d$ is a [[Continuous Function]] from $M \times M \to \mathbb{R}$ (where $\mathbb{R}$ is endowed with its standard [[Distance Function]] $x,y \mapsto |x - y|$ and $M \times M$ is endowed with the [[Product Metric Space]]).

## Proof
Let $\epsilon > 0$ and let $x,y \in M$. Let $\delta = \frac{\epsilon}{2}$. Suppose $x',y' \in M$ so that $\sup\limits \{d(x,x'), d(y,y')\} < \delta$. This means $d(x, x')$ and $d(y,y')$ are both less than $\delta$. Thus 
$$2\delta + d(x,y) > d(x', x) + d(x,y) + d(y,y') \geq d(x', y').$$
Therefore $d(x',y') - d(x,y) < 2 \delta$. Likewise
$$2\delta + d(x',y') > d(x, x') + d(x',y') + d(y',y) \geq d(x, y).$$
so $d(x,y) - d(x',y') < 2 \delta$. Therefore $|d(x,y) - d(x',y')| < 2 \delta = \epsilon$. Therefore, by the definition of [[Function Limit]], $\lim\limits_{(x',y') \to (x,y)} d(x',y') = d(x,y)$. Since $x,y \in M$ were arbitrary, $d$ is a [[Continuous Function]]. $\blacksquare$