---
title: "Constant Functions are Measureable"
---

# Statement
Let $X$ be a [[Set]] and let $\mathcal{M}$ be any [[Sigma Algebra]] on $X$. Likewise, let $Y$ be a [[Set]] and let $\mathcal{N}$ be any [[Sigma Algebra]] on $Y$. Suppose $f: X \to Y$ is such that $\forall x \in X$ $f(x) = c$ for some $c \in Y$. Then $f$ is $(\mathcal{M}, \mathcal{N})$-[[Measureable Function|measureable]].

## Proof
Suppose $S \in \mathcal{N}$. If $c \in S$ then every element of $X$ maps into  
$S$ and $f^{-1}(S) = X$. If $c \not\in S$, then no element of $X$ maps into $S$ and $f^{-1}(S) = \emptyset$. Since $\{\emptyset, X\} \subset \mathcal{M}$ by definition of [[Sigma Algebra]], we see that $f$ is $(\mathcal{M}, \mathcal{N})$-[[Measureable Function|measureable]]. $\blacksquare$