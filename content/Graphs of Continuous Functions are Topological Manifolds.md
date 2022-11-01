---

title: "Graphs of Continuous Functions are Topological Manifolds"

---
# Statement
Let $M, N$ be [[Topological Manifold]]s of [[Manifold Dimension]]s $m,n$ respectively and let $f: M \to N$ be a [[Continuous Function]]. Then the [[Graph of a Function|graph]]  of $f$, $\Gamma(F) \subset M \times N$, with the [[Subspace Topology]] is a [[Topological Manifold]] of [[Manifold Dimension]] $n$.

In fact, $\Gamma(f)$ is a [[Topological Submanifold]] of $M \times N$ endowed with the [[Product of Topological Manifolds is a Manifold|product manifold]].

## Proof
We simply check the definition of a [[Topological Manifold]].
1. [[Subspace Topology inherits Second Countability]]
2. [[Subspace Topology inherits Hausdorfness]]
3. Consider the [[Projection Map]] $\pi_{1} : \Gamma(f) \to M$ that sends $(x, y) \mapsto x$. First we show $\pi_{1}$ is a [[Homeomorphism]]. Indeed $\pi_{1}$ is [[Projection Maps are Continuous Functions|continuous]]. Observe that $\rho : M \to \Gamma(f)$ that sends $x \mapsto (x, f(x))$ is the [[Function Inverse]] of $\pi_{1}$ since $\pi_{1} \circ \rho$ sends $x \mapsto (x, f(x)) \mapsto x$ and $\rho \circ \pi_{1}$ sends $(x, f(x)) \mapsto x \mapsto (x, f(x))$. Furthermore $\rho$ is [[Continuous Function|continuous]]. To see this, note that because the [[Subspace Topology preserves Bases]], $$\mathcal{B} := \{(U_{1} \times U_{2}) \cap \Gamma(f) : U_{1} \subset M \text{ is open}, U_{2} \subset N \text{ is open}\}$$ is a [[Topological Basis]] for $\Gamma(f)$. For $V \in \mathcal{B}$, where $V = (U_{1} \times U_{2}) \cap \Gamma(f)$ for $U_{1}, U_{2}$ [[Open]] in $M,N$ respectively, $$\rho^{-1}(V) = \rho^{-1}((U_{1} \times U_{2}) \cap \Gamma(f)) = f^{-1}(U_{2}) \cap U_{1}.$$ The last equality follows because  $$\begin{align*}
x \in f^{-1}(U_{2}) \cap U_{1} &\Leftrightarrow x \in U_{1} \wedge f(x) \in U_{2}\\
&\Leftrightarrow (x, f(x)) \in (U_{1} \times U_{2}) \cap \Gamma(f)\\
&\Leftrightarrow \rho(x) \in (U_{1} \times U_{2}) \cap \Gamma(f)\\
&\Leftrightarrow x \in \rho^{-1}((U_{1} \times U_{2}) \cap \Gamma(f)).
\end{align*}$$So  $\rho$ is a [[Continuous Function]] because [[A Function is Continuous iff it takes Basis Sets back to Open Sets]] and $f^{-1}(U_{2}) \cap U_{1}$ is [[Open]] ($f$ is [[Continuous Function|continuous]]). Thus $\pi_{1}$ is a [[Homeomorphism]]. Now let $(x, f(x)) =: p \in \Gamma(f)$ and let $(U, \varphi)$ be a [[Coordinate Chart]] containing $x$ for $M$. Then because $\pi_{1}$ is a [[Homeomorphism]] and [[Composition of Homemorphisms is a Homeomorphism]], $\varphi \circ \pi_{1}$ us a [[Homeomorphism]] from $U \times f(U) = (U \times N) \cap \Gamma(f)$ to $\varphi(U) \subset \mathbb{R}^{n}$. Since $p \in \Gamma(f)$ was arbitrary, these [[Coordinate Chart]]s cover $\Gamma(f)$.

$\blacksquare$