---

title: "Extreme Value Theorem"

---
# Statement 1
Let $X$ be a [[Topological Space]]s and let $K \subset X$ be [[Compact]]. Let $Y$ be a [[Total Ordering]] endowed with the [[Order Topology]]. Let $f: X \to Y$ be a [[Continuous Function]]. Then $f(K)$ is a [[Bounded Set]]. Furthermore $\sup\limits f(K)$ and $\inf\limits f(K)$ both exist and are achieved by some resp. $x \in K$.

## Proof
Because [[Continuous Functions Preserve Compactness]], we know $f(K)$ is [[Compact]]. [[Compact Sets are Bounded]], so this gives us the first result. [[TODO]] I think I need to use [[Compact Sets are Complete]]


Let $M$ be such a bound (that is, $M \geq \sup\limits_{x \in K} |f(x)|$. Then $f(K)$ has [[Upper Bound]] $M$, so by [[Completeness of the Real Numbers]], we know $\sup\limits f(K)$ exists. Similarly, noting $-M$ is a [[Lower Bound]] for $f(K)$, we know $\inf\limits f(K)$ exists. We show that there exists $x \in K$ so $f(x) = \sup\limits f(K)$, the proof for $\inf\limits$ is similar. [[There Exists a Sequence Converging to Extremum]]

# Statement 2
Let $X$ be a [[Topological Space]] and let $K \subset X$ be [[Compact]]. Let $f: X \to \mathbb{R}$ be a [[Continuous Function]]. Then $f(K)$ is a [[Bounded Set]]. Furthermore $\sup\limits f(K)$ and $\inf\limits f(K)$ both exist and are achieved by some resp. $x \in K$.

## Proof
Because [[Continuous Functions Preserve Compactness]], we know $f(K)$ is [[Compact]]. [[Compact Sets are Bounded]], so this gives us the first result. Let $M$ be such a bound (that is, $M \geq \sup\limits_{x \in K} |f(x)|$. Then $f(K)$ has [[Upper Bound]] $M$, so by [[Completeness of the Real Numbers]], we know $\sup\limits f(K)$ exists. Similarly, noting $-M$ is a [[Lower Bound]] for $f(K)$, we know $\inf\limits f(K)$ exists. We show that there exists $x \in K$ so $f(x) = \sup\limits f(K)$, the proof for $\inf\limits$ is similar. [[There Exists a Sequence Converging to Extremum]]