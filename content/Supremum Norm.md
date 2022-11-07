---

title: "Supremum Norm"

---
# Statement

Let $(X_{i}, ||\cdot||_{i})_{i \in I}$ be [[Normed Vector Space]]s over [[Field]] $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ with [[Index Set]] $I$ and let $X = \prod\limits_{i \in I}^{}  X_{i}$. Then the function $||\cdot||: X \to \overline{\mathbb{R}_{\geq 0}}$ defined
$$||x|| := \sup\limits_{i \in I} ||x_{i}||_{i}$$
(where $||x|| = \infty$ if $||x_{i}||_{i}$ is [[Bounded Set|unbounded]]) is an [[Extended Norm]] over the [[Product Vector Space]] $X$. It is known as the [[Supremum Norm]].

## Proof
First note that by [[Completeness of the Real Numbers]], the [[Supremum Norm]] is well-defined. We check the [[Axiom]]s of an [[Extended Norm]]:
1. Suppose $x \in X$ so that $||x|| = 0$. Then $||x_{i}||_{i} \leq 0$ for all $i \in I$. But $||x_{i}||_{i} \geq 0$ already so $||x_{i}||_{i} = 0$ for all $i  \in I$. Since $||\cdot||_{i}$ is a [[Norm]], $x_{i} = 0$ for all $i  \in I$. Thus, $x = 0$. $\checkmark$
2. Suppose $\alpha \in \mathbb{K}$. Then $$||\alpha x|| = \sup\limits_{i \in I} ||\alpha x_{i}||_{i} = \sup\limits_{i \in I} |\alpha| || x_{i}||_{i} = |\alpha|\sup\limits_{i \in I}||x_{i}||_{i}= |\alpha| ||x||. \checkmark$$
3. Suppose $x, y \in X$. Then $$\begin{align*}
||x + y|| &= \sup\limits_{i \in I} ||x_{i} + y_{i}||_{i} \\
&\leq \sup\limits_{i \in I} (||x_{i}||_{i} + ||y_{i}||_{i}) \\
&\leq \sup\limits_{i \in I} ||x_{i}||_{i} + \sup\limits_{i \in I} ||y_{i}||_{i} \\
&= ||x + y||. \checkmark
\end{align*}$$

$\blacksquare$

# Other Outlinks
- [[Non-negative Multiplication Commutes with Supremum]]
- [[Sum of Supremum bounds Supremum of Sum]]
