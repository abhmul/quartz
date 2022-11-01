---

title: "Fourier Expansion of a Pseudo-Boolean Function"

---
# Definition 1
Let $f: \{-1, 1\}^{n} \to \mathbb{R}$ be a [[Pseudo-Boolean Function]] for $n \in \mathbb{N}$. The [[Fourier Expansion of a Pseudo-Boolean Function]] is the unique [[Multilinear]] [[Polynomial]] representation of $f$.

## Construction
We construct a [[Polynomial]] that interpolates $f$. Enumerate $\{a^{(i)}\}_{i=1}^{2^{n}} = \{-1, 1\}^{n}$. Write
$$f(x) = \sum\limits_{i=1}^{2^{n}} f(a^{(i)}) \mathbb{1}_{x = {a^{(i)}}}$$
Furthermore, we can write
$$\mathbb{1}_{x=a^{(i)}} = \prod\limits_{k=1}^{n} \frac{a^{(i)}_{k}x_{k} + 1}{2}$$
since if $x \neq a^{(i)}$, one of the terms in the product will be $0$. Otherwise all terms will be $1$. Expanding our formula for $f$ out, we get a [[Polynomial]]. 

First observe that since $x_{k}^{2} = 1$ for all $k \in [n]$, $x \in \{-1, 1\}^{n}$, all higher exponents of $x_{k}$ can be reduced to either $0$ or $1$. Thus, we can write $f$ in the form
$$f(x) = \sum\limits_{S \subset [n]} \hat{f}(S) \prod_{k \in S} x_{k}$$
where we use $S$ to iterate over all possible [[Monomial]]s, and let $\hat{f}(S)$ be the coefficient of the respective [[Monomial]] in our [[Polynomial]] representation. 

Now we show that this representation is [[Multilinear]] and it is unique.

[[TODO]] - check multilinearity, then uniqueness because subtracting two different representations will have nonzero coefficients on some monomials. Take the smallest $S \subset [n]$ with a nonzero coefficient, assign $x_{k} = 1$ iff $k \in S$, then output of function is that nonzero coefficient and thus is not $0$, giving us a [[Proof by Contradiction|contradiction]].

We define $\hat{f}(S)$ to be the [[Boolean Fourier Coefficient]] of $f$ at $S$.

# Definition 2
[[TODO]] in terms of [[Boolean Fourier Basis]] for [[Functions to a Field form a Vector Space|boolean function vector space]].

# Encounters
- [[O'Donnell - Analysis of Boolean Functions]] - Ch 1