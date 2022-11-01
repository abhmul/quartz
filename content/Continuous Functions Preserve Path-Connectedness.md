---

title: "Continuous Functions Preserve Path-Connectedness"

---
# Statement
Let $X, Y$ be [[Topological Space]]s and suppose $X$ is [[Path-Connected]]. Then if $f: X \to Y$ is a [[Continuous Function]], $f(X)$ is also [[Path-Connected]].

## Proof
Let $y, y' \in f(X)$. Then there exist $x, x' \in X$ so that $f(x) = y$ and $f(x') = y'$. Since $X$ is [[Path-Connected]], there a [[Continuous Path]]  $\gamma : [0,1] \to X$ so that $\gamma(0)=x$ and $\gamma(1) = x'$. Since $f$ is [[Continuous Function|continuous]], $f \circ \gamma$ is also a [[Continuous Path]]. Furthermore $f(\gamma(0)) = y$ and $f(\gamma(1)) = y'$, so there exists a [[Continuous Path]] from $y$ to $y'$. Since $y,y' \in f(X)$ were arbitrary, $f(X)$ is [[Path-Connected]]. $\blacksquare$
