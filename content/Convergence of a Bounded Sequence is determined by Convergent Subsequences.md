---
title: "Convergence of a Bounded Sequence is determined by Convergent Subsequences"
---

# Statement
Let $(a_{n}) \subset \mathbb{R}$ be a [[Bounded Sequence]]. Then $a_{n} \to a \in \mathbb{R}$  [[If and Only If|iff]] every [[Sequence Convergence|convergent]] [[Subsequence]] of $(a_{n})$ converges to $a$.

# Proof
($\Rightarrow$) Suppose $a_{n} \to a$. Let $(a_{n_{k}})$ be a convergent subsequence of $(a_{n})$. Because [[Every Subsequence of a Convergent Sequence converges to the same Limit]], we know $a_{n_{k}} \to a$.

($\Leftarrow$) Suppose every convergent subsequence of $(a_{n})$ converges to $a \in \mathbb{R}$. First we show that such a subsequence exists. 

Let $M \in \mathbb{R}$ be s.t. $|a_{n}| \leq M$ $\forall n \in \mathbb{N}$. By the [[Bolzano-Weierstrass Theorem]], we know there exists some convergent subsequence.

Next we show that $(a_{n}) \to a$. Suppose not. Then there exists an $\epsilon > 0$ s.t. $\forall N \in \mathbb{N}$, $n \geq N$ s.t. $|a_{n} - a| \geq \epsilon$. Let $n_{1}$ be such an element for $N = 1$. Next let $n_{2}$ be such an element for $N = 2$. Continue in this way to get a subsequence $(a_{n_{k}})$ s.t.

$$|a_{n_{k}} - a| \geq \epsilon \text{ for all }k \in \mathbb{N}$$
Because $\{a_{n_{k}}\} \subset \{a_{n}\}$, it has the same bound of $M$. Thus by the [[Bolzano-Weierstrass Theorem]], $(a_{n_{k}})$ has a convergent subsequence. This subsequence is also a subsequence of $(a_{n})$ so it must also converge to $a$ by our given. If we denote this sub-subsequence $(a_{n_{k_{l}}})$, we have that there exists an $L \in \mathbb{N}$ s.t.

$$|a_{n_{k_{l}}} - a| < \epsilon \text{ for all }l \in \mathbb{N}$$
But this [[Proof by Contradiction|contradicts]] our construction of $(a_{n_{k}})$. Therefore $(a_{n}) \to a$. $\blacksquare$

# Other Outlinks
- [[Real Numbers]]
- [[Natural Numbers]]
