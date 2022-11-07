---

title: "Compact Function Space"

---
# Statement
Let $X$ be a [[Topological Space]] and let $K \subset X$ be [[Compact]]. Let $(Y, ||\cdot||)$ be a [[Normed Vector Space]]. Then $C(K, Y)$ equipped with the [[Supremum Norm]] $||\cdot||_{\infty}$ is a [[Normed Vector Space]]. It is known as the [[Compact Function Space]] from $K$ to $Y$.

## Proof
Note that [[Continuous Functions form a Vector Space]] so $C(K, Y)$ is indeed a [[Vector Space]]. Furthermore, by the [[Extreme Value Theorem]], $||f(K)|| \subset \overline{\mathbb{R}_{\geq 0}}$ is a [[Tightly Bounded Set]] for all $f \in C(K,Y)$. Therefore $\sup\limits ||f(K)|| =: ||f||_{\infty}$ exists and is [[Finite Set|finite]]. Thus, $C(K,Y) = C_{b}(K, Y)$. Since the [[Bounded Continuous Function Space]] is a [[Normed Vector Space]], the [[Compact Function Space]] is also one. $\blacksquare$

# Other Outlinks
- [[Norms are Continuous]]
- [[Composition of Continuous Functions is Continuous]]