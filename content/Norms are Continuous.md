---

title: "Norms are Continuous"

---
# Statement
Let $(X, ||\cdot||)$ be a [[Normed Vector Space]]. Then $||\cdot||$ is a [[Continuous Function]].

## Proof
Recall $x,y \mapsto ||x - y||$ is the [[Norms induce Metrics|distance function induced by our norm]]. Let $x \in X$. Let $x_{n} \to x$ be a [[Sequence Convergence|convergent sequence]] in $X$. Then $(x_{n}, 0) \to (x, 0)$ in $X \times X$ because [[Components Converge iff Sequence Converges in Finite Product Metric Spaces]]. Because [[Metrics are Continuous]] and [[Continuous Functions Preserve Sequence Limits]], $||x_{n}|| = ||x_{n} - 0|| \to ||x - 0|| = ||x||$. By the definition of [[Continuous Function]] in a [[Metric Space]], $||\cdot||$ is a [[Continuous Function]]. $\blacksquare$