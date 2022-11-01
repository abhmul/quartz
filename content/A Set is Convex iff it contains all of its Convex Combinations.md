---
title: "A Set is Convex iff it contains all of its Convex Combinations"
---

# Statement
Let $V$ be a [[Vector Space]] over $\mathbb{R}$ and $S \subset V$. $S$ is a [[Convex Set]] [[If and Only If]] $\forall n \in \mathbb{N}$, $x_{1}, \dots, x_{n} \in S$, all [[Convex Combination]]s (of $x_{1}, \cdots, x_{n}$) $\lambda_{1} x_{1} + \cdots + \lambda_{n} x_{n} \in S$.

## Proof
$(\Leftarrow)$: Let $u, v \in S$. Note that for $\lambda \in [0,1]$, $\lambda u + (1 - \lambda) v = w$  is a [[Convex Combination]] of $u,v$ and, thus, $w \in S$. Thus, by definition, $S$ is a [[Convex Set]]. $\checkmark$

$(\Rightarrow)$: We proceed by [[Induction]]. We skip the trivial case where $n=1$.

*Base Case* ($n = 2$): Let $x_{1}, x_{2} \in S$ and let $\lambda_{1}, \lambda_{2} \in [0,1]$ so that $\lambda_{1} + \lambda_{2} = 1$. Then $\lambda_{2} = (1- \lambda_{1})$. Since $S$ is a [[Convex Set]], we have that $$S \ni \lambda_{1}x_{1} + (1 - \lambda_{1})x_{2} = \lambda_{1}x_{1} + \lambda_{2}x_{2}$$ establishing the case when $n = 2$.

*Inductive Step*: Let $n \in \mathbb{N}$ so that $n > 2$, and assume the result holds true for $k \in [n-1]$. Let $\lambda_{1}, \dots, \lambda_{n} \in [0,1]$ so that $\sum\limits_{i=1}^{n} \lambda_{i} = 1$. If $\lambda_{1} = 1$, then we can drop $\lambda_{i} = 0$ for $i \in \{2, \dots, n\}$ and our [[Convex Combination]] is just $x_{1} \in S$ $\checkmark$. Otherwise, assuming $\lambda_{1} \neq 1$. Then $\sum\limits_{i=2}^{n} \lambda_{i} = 1 - \lambda_{1}$ and $\sum\limits_{i=2}^{n} \frac{\lambda_{i}}{1- \lambda_{1}} = 1$. By [[Induction]] we know that $$\frac{\lambda_{2}}{1-\lambda_{1}}x_{2} + \cdots + \frac{\lambda_{n}}{1-\lambda_{1}}x_{n} \in S.$$ Because $S$ is a [[Convex Set]]
$$\begin{align*}
S &\ni \lambda_{1} x_{1} + (1 - \lambda_{1}) \left(\frac{\lambda_{2}}{1-\lambda_{1}}x_{2} + \cdots + \frac{\lambda_{n}}{1-\lambda_{1}}x_{n}\right)\\
&=\lambda_{1}x_{1} + \cdots + \lambda_{n} x_{n}
\end{align*}$$
so $S$ is closed under [[Convex Combination]]s. $\checkmark \blacksquare$