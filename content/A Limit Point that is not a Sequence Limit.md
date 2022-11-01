---

title: "A Limit Point that is not a Sequence Limit"

---
# Example
Consider $\mathbb{R}$ equipped with the [[Cocountable Topology]]. Consider $S = \mathbb{R} \setminus \{0\}$. Then $0$ is a [[Limit Point]] of $S$. To see this, observe $\{0\}$ cannot be [[Open]] because $\{0\}^{C}$ is [[Uncountable]]. Thus any $U \subset \mathbb{R}$ [[Open]] must be s.t. $U \cap S \neq \emptyset$.

However, $0$ cannot be a [[Sequence Convergence|sequence limit]] for any [[Sequence]] on $S$. Indeed, let $({x}_{n})_{n=1}^{\infty} \subset S$. Then consider the [[Open]] set $U = \{0\} \cup \{x_n: n \in \mathbb{N}\}^{C}$. $U$ is indeed [[Open]] becase $U^{C} \subset \{x_n\}_{n=1}^{\infty}$. On the other hand, since $0 \not\in \{x_n\}_{n=1}^{\infty}$, there is no $n \in \mathbb{N}$ for which $x_{n} \in U$. Thus $x_{n} \not\to 0$. $\blacksquare$