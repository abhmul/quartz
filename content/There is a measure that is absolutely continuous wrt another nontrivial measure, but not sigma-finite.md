---

title: "There is a measure that is absolutely continuous wrt another nontrivial measure, but not sigma-finite"

---
# Statement
Consider [[Measure Space]] $(X, \mathcal{M}, \mu)$ so that $\mu(X) > 0$. Consider $\nu: \mathcal{M} \to [0, \infty]$ defined as
$$\nu(S) = \begin{cases} 0 &\text{if }\mu(S) = 0 \\ \infty &\text{ otherwise} \end{cases}.$$
Then $\nu$ is a [[Measure]] on $(X, \mathcal{M})$ and $\nu << \mu$, but $\nu$ is not a [[Sigma-Finite Measure]].

## Proof
First we check $\nu$ is a [[Measure]]. 
1. $\mu(\emptyset) = 0$, so by construction, $\nu(\emptyset) = 0$. $\checkmark$
2. Suppose $\{E_{n}\}_{n \in \mathbb{N}} \subset \mathcal{M}$ are [[Disjoint Sets]].  We have two cases
	1. $\mu(E_{n}) = 0$ for all $n \in \mathbb{N}$. Then $\nu(E_{n}) = 0$ for all $n \in \mathbb{N}$, so $$\sum\limits_{n=1}^{\infty} \nu(E_{n}) = \sum\limits_{n=1}^{\infty} 0 = 0.$$Because $\mu$ is a [[Measure]], we know that $$\mu(\bigsqcup\limits_{n \in \mathbb{N}} E_{n}) = \sum\limits_{n=1}^{\infty}\mu(E_{n}) = \sum\limits_{n=1}^{\infty} 0 = 0.$$ Thus, $\nu(\bigsqcup\limits_{n \in \mathbb{N}} E_{n}) = 0$ also. Therefore, $$\sum\limits_{n=1}^{\infty} \nu(E_{n}) = 0 = \nu(\bigsqcup\limits_{n \in \mathbb{N}} E_{n}).$$ $\checkmark$
	2. $\exists k \in \mathbb{N}$ so that $\mu(E_{k}) > 0$. Then $\nu(E_{k}) = \infty$ and $$\sum\limits_{n=1}^{\infty} \nu(E_{n}) = \infty.$$ Because [[Monotonicity of Measures]], $\mu(\bigsqcup\limits_{n \in \mathbb{N}} E_{n}) \geq \mu(E_{k}) > 0$, so $\nu(\bigsqcup\limits_{n \in \mathbb{N}} E_{n}) = \infty$. Therefore $$\sum\limits_{n=1}^{\infty} \nu(E_{n}) = \infty = \nu(\bigsqcup\limits_{n \in \mathbb{N}} E_{n}).$$ $\checkmark$

Thus, we have that $\nu$ is a [[Measure]]. $\nu << \mu$ by construction. To see $\nu$ is not a [[Sigma-Finite Measure]], let $\{P_{n}\}_{n \in \mathbb{N}}$ be a [[Partition]] of $X$. Since $\mu(X) > 0$, there must be some $k \in \mathbb{N}$ so that $\mu(P_{k}) > 0$ (otherwise $\mu(X) = 0$ by [[Countable Additivity of Measures]]). Thus, $\nu(P_{k}) = \infty$, and $\nu$ cannot be a [[Sigma-Finite Measure]]. $\blacksquare$