---

title: "Extreme Value Theorem"

---

# Statement 1
Let $X$ be a [[Topological Space]]s and let $K \subset X$ be [[Nonempty]] and [[Compact]]. Let $Y$ be a [[Total Ordering]] endowed with the [[Order Topology]]. Let $f: X \to Y$ be a [[Continuous Function]]. Then $\sup\limits f(K)$ and $\inf\limits f(K)$ both exist and are achieved by some resp. $x \in K$ (or, in short, $f(K)$ is [[Tightly Bounded Set|tightly bounded]]).

## Proof
Because [[Continuous Functions Preserve Compactness]], we know $f(K)$ is [[Compact]] Since $K$ is [[Nonempty]], we know $f(K)$ is [[Nonempty]]. [[A Nonempty Set is Compact in the Order Topology iff it is Tightly Bounded and Complete]], so both $\sup\limits f(K) \in f(K)$ and $\inf\limits f(K) \in f(K)$. This means precisely that there exists $x,y \in K$ so that $f(x) = \sup\limits f(K)$ and $f(y) = \sup\limits f(K)$. $\blacksquare$


# Statement 2
Let $X$ be a [[Topological Space]] and let $K \subset X$ be [[Compact]]. Let $f: X \to \mathbb{R}$ be a [[Continuous Function]]. Then $\sup\limits f(K)$ and $\inf\limits f(K)$ both exist and are achieved by some resp. $x \in K$.
## Proof
Follows from Statement (1) after noting that the standard topology on the [[Real Numbers]] is the [[Order Topology]] with the natural ordering. $\square$