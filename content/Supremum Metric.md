---

title: "Supremum Metric"

---
# Statement
Let $(M_{i}, d_{i})_{i \in I}$ be [[Metric Space]]s with [[Index Set]] $I$ and let $M = \prod\limits_{i \in I}^{}  M_{i}$. Then the function $d: M \times M \to \overline{\mathbb{R}_{\geq 0}}$ defined
$$d(x, y) := \sup\limits_{i \in I} d_{i}(x_{i}, y_{i})$$
(where $d(x,y) = \infty$ if $d_{i}(x_{i},y_{i})$ is [[Bounded Set|unbounded]]) is an [[Extended Distance Function]]. It is known as the [[Supremum Metric]].

## Proof
We show that it satisfies the [[Axiom]]s of a [[Distance Function]]:
1. Let $x, y \in M$. Suppose $d(x, y) = 0$. Then, by definition of [[Supremum]], $d_{i}(x_{i}, y_{i}) \leq 0$ for all $i \in I$. But already $d_{i}(x_{i}, y_{i}) \geq 0$ for all $i \in I$, so we have $d_{i}(x_{i}, y_{i}) = 0$. By definition of [[Distance Function]], this means $x_{i} = y_{i}$ for all $i \in I$. Then $x = y$. $\checkmark$
2. Let $x, y \in M$. Observe $$d(x,y) = \sup\limits_{i \in I} d_{i}(x_{i}, y_{i}) = \sup\limits_{i \in I} d_{i}(y_{i}, x_{i}) = d(y,x)$$ $\checkmark$
3. Let $x,y,z \in M$. Then $$\begin{align*}
d(x,y) + d(y,z) &= \sup\limits_{i \in I} d_{i}(x_{i}, y_{i}) + \sup\limits_{i \in I} d_{i}(y_{i}, z_{i}) \\
&\geq\sup\limits_{i \in I} (d_{i}(x_{i}, y_{i}) + d_{i}(y_{i}, z_{i}))\\
&\geq \sup\limits_{i \in I} d_{i}(x_{i}, z_{i})\\
&= d(x, z)
\end{align*}$$ $\checkmark$

## Remarks
1. The [[Norms induce Metrics|metric induced by]] a [[Supremum Norm]] is a [[Supremum Metric]].
# Other Outlinks
- [[Cartesian Product]]
- [[Sum of Supremum bounds Supremum of Sum]]