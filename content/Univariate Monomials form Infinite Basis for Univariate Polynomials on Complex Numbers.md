---

title: "Univariate Monomials form Infinite Basis for Univariate Polynomials on Complex Numbers"

---
# Statement
Let $P[\mathbb{C}]$ to be the [[Space of Polynomials over a Field form a Vector Subspace of Function Vector Space|polynomial vector space]] over $\mathbb{C}$. Then the [[Set]] of [[Monomial]]s $S = \{1, x, x^{2}, \dots\}$ is an [[Infinite Set|infinite]] [[Vector Space Basis]] for $P[\mathbb{C}]$.

## Proof
Consider the [[Set]] $S = \{1, x, x^{2}, \dots\}$. We will show that $S$ is a [[Vector Space Basis]] for $P[\mathbb{C}]$. Observe that by definition, we can write any [[Polynomial]] as a [[Linear Combination]] of finitely many [[Monomial]]s, and $S$ is the [[Set]] of all [[Monomial]]s. Therefore $\text{span} S = P[\mathbb{C}]$, since [[The Subspace Span is the Set of all Linear Combinations]].

On the other hand, suppose that there exists some nontrivial $c_{1}, \dots, c_{n} \in \mathbb{C}$ and $x^{a_{1}}, \dots x^{a_{n}} \in S$ for some $n \in \mathbb{N}$ so that
$$c_{1} x^{a_{1}} + \cdots + c_{n} x^{a_{n}} = \mathbf{0}.$$
[[Without Loss of Generality|WLOG]] let $a_{1}, \dots, a_{n}$ be arranged in [[Increasing]] order (by [[Commutativity]] of $+$). Then, by definition of $\mathbf{0}$, $c_{1} x^{a_{1}} + \cdots + c_{n} x^{a_{n}}$ has [[Infinite Set|infinitely]] many [[Polynomial Zeroes]]. However, the [[Fundamental Theorem of Algebra]] tells us that $c_{1} x^{a_{1}} + \cdots + c_{n} x^{a_{n}}$ has at most $a_{n}$ [[Polynomial Zeroes]] in $\mathbb{C}$ (since some $c_{i} \neq 0$ for $i \in [n]$) and $a_{n}$ is [[Finite Set|finite]] $\unicode{x21af}$. Therefore, we must have that $c_{1} = \cdots = c_{n} = 0$ and $S$ is a [[Linearly Independent]] [[Set]].

Thus, $S$ is a [[Vector Space Basis]]. To see that it is an [[Infinite Set]], consider $S' = \{x, x^{2}, \dots\}$. [[Function|Mapping]] $x^{n} \mapsto x^{n+1}$ for $n \in \mathbb{Z}_{\geq 0}$ gives us a [[Bijection]] between $S$ and $S'$ since:
1. For each $x^{k}$ for $k \in \mathbb{N}$, we have that $k-1 \in \mathbb{Z}_{\geq 0}$, so there is $x^{k-1} \in S$ that maps to $x^{k} \in S'$. So our mapping is a [[Surjection]].
2. If $k, l \in \mathbb{N}$ so that $x^{k} \neq x^{l}$, then we have that $k \neq l$ and $x^{k-1} \neq x^{l-1}$. Therefore our mapping is an [[Injection]].

Then, since $S' \subsetneq S$ ($1 \not\in S'$), we have that $S$ is an [[Infinite Set]] by definition. $\blacksquare$

# Other Outlinks
- [[Complex Numbers]]
- [[Subspace Span]]

# Encounters
1. [[Hoffman and Kunze - Linear Algebra]] - Sec 2.3 pg 43