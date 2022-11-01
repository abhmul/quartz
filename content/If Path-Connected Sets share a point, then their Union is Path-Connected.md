---

title: "If Path-Connected Sets share a point, then their Union is Path-Connected"

---
# Statement
Let $X$ be a [[Topological Space]], $x \in X$, and suppose $\mathcal{P} \subset \mathcal{P}(X)$ is such that for all $P \in \mathcal{P}$
1. $P$ is [[Connected]]
2. $x \in P$

Then $D := \bigcup\limits_{P \in \mathcal{P}} P$ is [[Connected]].

## Proof
Let $y, z \in D$. Then there exists $P_{y}, P_{z} \in \mathcal{P}$ s.t. $y \in P_{y}$ and $z \in P_{z}$. Since both are [[Path-Connected]], there exist [[Continuous Path]]s
$$\begin{align*}
f: [0, 1] \to D \text{ s.t. } f(0)=y,f(1)=x\\
g: [0, 1] \to D \text{ s.t. } g(0)=x,g(1)=z
\end{align*}$$
Then we can take $h := f*g$. Since $f(1) = g(0)$, [[Continuous Path Concatenation]] is valid here so $h$ is a [[Continuous Path]]. Then $h(0) = f(0) = y$ and $h(1) = g(1) = z$. Since $y,z \in D$ were arbitrary, $D$ is [[Path-Connected]].  $\blacksquare$