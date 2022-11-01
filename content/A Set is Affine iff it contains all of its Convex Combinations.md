---
title: "A Set is Affine iff it contains all of its Affine Combinations"
---

# Statement
Let $V$ be a [[Vector Space]] over $\mathbb{R}$ and $S \subset V$. $S$ is a [[Affine Set]] [[If and Only If]] $\forall n \in \mathbb{N}$, $x_{1}, \dots, x_{n} \in S$, all [[Affine Combination]]s (of $x_{1}, \cdots, x_{n}$) $\lambda_{1} x_{1} + \cdots + \lambda_{n} x_{n} \in S$.

## Proof
$(\Leftarrow)$: Let $u, v \in S$. Note that for $\lambda \in \mathbb{R}$, $\lambda u + (1 - \lambda) v = w$  is a [[Affine Combination]] of $u,v$ and, thus, $w \in S$. Thus, by definition, $S$ is a [[Affine Set]]. $\checkmark$

$(\Rightarrow)$: We proceed by [[Induction]]. We skip the trivial case where $n=1$.

*Base Case* ($n = 2$): Let $x_{1}, x_{2} \in S$ and let $\lambda_{1}, \lambda_{2} \in \mathbb{R}$ so that $\lambda_{1} + \lambda_{2} = 1$. Then $\lambda_{2} = (1- \lambda_{1})$. Since $S$ is a [[Affine Set]], we have that $$S \ni \lambda_{1}x_{1} + (1 - \lambda_{1})x_{2} = \lambda_{1}x_{1} + \lambda_{2}x_{2}$$ establishing the case when $n = 2$.

*Inductive Step*: Let $n \in \mathbb{N}$ so that $n > 2$, and assume the result holds true for $k \in [n-1]$. Let $\lambda_{1}, \dots, \lambda_{n} \in \mathbb{R}$ so that $\sum\limits_{i=1}^{n} \lambda_{i} = 1$. We must have $\exists j \in [n]$ so that $\lambda_{j} \neq 1$, otherwise $\sum\limits_{i=1}^{n} \lambda_{i} = n \neq 1$.[[Without Loss of Generality]], let $j = 1$ (otherwise, we can just swap them). Then $\sum\limits_{i=2}^{n} \lambda_{i} = 1 - \lambda_{1}$ and $\sum\limits_{i=2}^{n} \frac{\lambda_{i}}{1- \lambda_{1}} = 1$. By [[Induction]] we know that $$\frac{\lambda_{2}}{1-\lambda_{1}}x_{2} + \cdots + \frac{\lambda_{n}}{1-\lambda_{1}}x_{n} \in S.$$ Because $S$ is a [[Affine Set]]
$$\begin{align*}
S &\ni \lambda_{1} x_{1} + (1 - \lambda_{1}) \left(\frac{\lambda_{2}}{1-\lambda_{1}}x_{2} + \cdots + \frac{\lambda_{n}}{1-\lambda_{1}}x_{n}\right)\\
&=\lambda_{1}x_{1} + \cdots + \lambda_{n} x_{n}
\end{align*}$$
so $S$ is closed under [[Affine Combination]]s. $\checkmark \blacksquare$