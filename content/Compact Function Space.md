---

title: "Compact Function Space"

---
# Statement
Let $X$ be a [[Topological Space]] and let $K \subset X$ be [[Compact]]. Let $Y$ be a [[Normed Vector Space]]. Then the [[Compact Function Space]] on $K$ to $Y$, denoted $C(K, Y)$ is the [[Normed Vector Space]]
$$C(K, Y) := \{f : K \to Y : f \text{ is continuous}\}$$
endowed with the [[Supremum Norm]].

## Proof
Note that [[Continuous Functions form a Vector Space]] so $C(K, Y)$ is indeed a [[Vector Space]]. Furthermore, by the [[Extreme Value Theorem]], $||f(K)||_{Y}$ is a [[Bounded Set]]. Therefore, by [[Completeness of the Real Numbers]], $||f|| = \sup\limits_{x \in K} ||f(x)||_{Y} < \infty$. Therefore the [[Supremum Norm]] is a true [[Norm]] (as opposed to an [[Extended Norm]]) on $C(K, Y)$, making it a [[Normed Vector Space]]. $\blacksquare$