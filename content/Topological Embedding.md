---

title: "Topological Embedding"

---
# Definition
Let $X, Y$ be [[Topological Space]]s and let $f: X \to Y$. $f$ is a [[Topological Embedding]] into $Y$ if $f: X \to f(X)$ is a [[Homeomorphism]], where $f(X)$ is given the [[Subspace Topology]] in $Y$.

## Remarks
1. A [[Topological Embedding]] is necessarily [[Continuous Function|continuous]]. Indeed if $U \subset Y$ is [[Open]], then $f^{-1}(U) = f^{-1}(U \cap f(X))$, which is [[Open]] because $U \cap f(X)$ is [[Open]] in the [[Subspace Topology]] and $f: X \to f(X)$ is a [[Continuous Function]] by definition of a [[Homeomorphism]].
2. A [[Topological Embedding]] is necessarily [[Injection|injective]]. Indeed if $x_{1}, x_{2} \in X$ so that $f(x_{1}) = f(x_{2})$, then because  $f(x_{1}), f(x_{2}) \in f(X)$ and $f$ is a [[Bijection]] onto $f(X)$ by definition of a [[Homeomorphism]], $x_{1}= x_{2}$.