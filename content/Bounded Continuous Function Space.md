---

title: "Bounded Continuous Function Space"

---
# Statement
Let $X$ be a [[Topological Space]] and let $(Y, ||\cdot||)$ be a [[Normed Vector Space]]. Then
$$C_{b}(X, Y) := \{f: X \to Y : \sup\limits_{x \in X} ||f(x)|| < \infty, f \text{ is continuous}\}$$
is a [[Normed Vector Space]] with the [[Supremum Norm]] $||\cdot||_{\infty}$. It is called the [[Bounded Continuous Function Space]] from $X$ to $Y$.

## Proof
Note that $C_{b}(X, Y)$ is simply the restrcition of the [[Vector Space]] $C(X, Y)$ to those with [[Finite Set|finite]] [[Supremum Norm]]. Since [[Restricting an Extended Norm to elements of Finite Norm form a Normed Vector Space]], we have that $C_{b}(X, Y)$ is a [[Normed Vector Space]]. $\blacksquare$

# Other Outlinks
- [[Continuous Functions form a Vector Space]]
- [[A Normed Vector Space is a Topological Vector Space]]