---
title: "Convergence Almost Surely does not imply convergence of moments"
---

# Statement
Let $(\Omega, \mathcal{M}, \mathbb{P})$ be a [[Probability Space]]. There exists a sequence of [[Random Variable]]s $(X_n)_{n=1}^{\infty}$ on $\Omega$ s.t. $X_{n} \to X$ but $\mathbb{E}|X_{n}| \not\to \mathbb{E}|X|$.

## Proof
We construct the example. Let $([0,1], \mathcal{B}([0,1]), \lambda)$ be our probability space. Suppose $X_{n}$ is defined as
$$X_{n} = 0*1_{x \leq 1 - \frac{1}{n}} + 7n1_{x > 1 - \frac{1}{n}}$$

Then $X_{n} \to 0$ [[Almost Sure Convergence|almost surely]]. To see this, observe that for $s \in [0, 1)$, there exists $N \in \mathbb{N}$ s.t. $1 - \frac{1}{N} > s$ (by the [[Archimedean]] property of the [[Natural Numbers]]). For all $n \geq N$, we have $\frac{1}{n} \leq \frac{1}{N}$ so $$X_{n}(s) = 0*1_{x \leq 1 - \frac{1}{n}}(s) + 7n1_{x > 1 - \frac{1}{n}}(s) = 0$$

Thus $\mathbb{P}[X_{n} \to 0] = \lambda([0, 1)) = 1 \checkmark$ .

On the other hand, observe that

$$\mathbb{E}|X_{n}| = 0*\lambda([0, 1 - \frac{1}{n}]) + 7n \lambda\left(\left(1-\frac{1}{n}, 1\right)\right) = 0 + \frac{7n}{n} = 7$$

While

$$\mathbb{E}|X| = 0$$

Since $7 \not\to 0$ we have that the [[Moment]]s do not converge. $\blacksquare$

## Remarks
1. In this example, all random variables are non-negative, so the construction also shows that almost sure convergence does not imply expectation converges.
2. Any form of convergence implied by almost sure ([[Convergence in Distribution]], [[Convergence in Probability]]) will also have this counterexample.
3. This is an example where [[Fatou's Lemma]] is strict. 
4. This example also works as a general example for generic [[Measure Space]]s.

## Source
1. Adapted from [Does Convergence in Distribution Imply Convergence of Expectation](https://math.stackexchange.com/questions/153293/does-convergence-in-distribution-implies-convergence-of-expectation)

# Other Outlinks
- [[Lebesgue Measure]]
- [[Real Numbers]]
- [[Closed Interval]]