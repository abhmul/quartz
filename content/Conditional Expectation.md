---
title: "Conditional Expectation"
---

[[TODO]] I am going to rework this page into
1. [[Conditional Expectation with respect to Sigma Field]]
2. [[Conditional Expectation with respect to Random Element]]
3. [[Conditional Expectation with respect to Event]]

# Definition 1
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $X$ be a [[Random Variable]] in $\bar{L^{1}}(\mathcal{B})$. Let $\mathcal{G} \subset \mathcal{B}$ be a sub-[[Sigma Algebra]]. Then the [[Conditional Expectation]] of $X$ (denoted $\mathbb{E}[X | \mathcal{G}]$) with respect to $\mathcal{G}$ is a  [[Random Variable]] in $\bar{L^{1}}(\mathcal{G})$ such that $\forall A \in \mathcal{G}$

$$\int\limits_{A} \mathbb{E}[X | \mathcal{G}] d \mathbb{P}(\omega) = \int\limits_{A} X d \mathbb{P}(\omega)$$

When we talk about [[Conditional Expectation]] with respect to another [[Random Variable]] $Y$, use the shorthand
$$\mathbb{E}[X | Y] = \mathbb{E}[X | \sigma(Y)]$$

When we talk about [[Conditional Expectation]] with respect to  a [[Random Variable]] $Y$ equal to $y \in \mathbb{R}$, we use the shorthand
$$\mathbb{E}[X | Y=y] = \mathbb{E}[X | Y](\omega)$$
for (any) $\omega \in Y^{-1}(\{y\})$. Note that this value may not be [[Well-Defined]], but given a particular [[Conditional Expectation]], we can get a reasonable answer [[Almost Surely]].

When we talk about [[Conditional Expectation]] with respect to a [[Set]] $B \in \mathcal{B}$, we use the shorthand:
$$\mathbb{E}[X|B] := \mathbb{E}[X|1_{B}](\omega)$$
for (any) $\omega \in B$. Note that this value is only [[Well-Defined]] if $\mathbb{P}(B) > 0$. For details on its exact form, see [[Conditional Expectation with respect to a Set is Integral divided by Probability]].

## Remarks
1. We require $X$ to be in $\bar{L^{1}}$ so the above integral is defined. 
2. With [[Conditional Expectation]] with respect to a [[Set]], it does not matter what $\omega \in B$ we choose, the value is the same. To see this, recall that $\sigma(1_{B}) = \{\emptyset, B, B^{C}, \Omega\}$. Since $\mathbb{E}[X|1_{B}]$ is $\sigma(1_{B})$-[[Borel Measureable Function|measureable]], $\sigma(\mathbb{E}[X|1_{B}]) \subset \sigma(1_{B})$. Let $\omega \in B$. Since [[Singletons are Closed in the Real Numbers]], we know $\{\mathbb{E}[X|1_{B}](\omega)\} \in \mathcal{B}(\mathbb{R})$. Thus we have that $\mathbb{E}[X|1_{B}]^{-1}(\{\mathbb{E}[X|1_{B}](\omega)\}) \in \sigma(1_{B})$ and it is not [[Disjoint Sets|disjoint]] with $B$. The only two sets that satisfy this criterion in $\sigma(1_{B})$ are $\Omega$ and $B$ itself. In either case, $\mathbb{E}[X|1_{B}](B) = \{\mathbb{E}[X|1_{B}](\omega)\}$ and $\mathbb{E}[X|1_{B}]$ is constant on $B$. $\blacksquare$

## Properties
1. [[Conditional Expectation Exists and is Almost Surely Unique]]
2. [[Conditioning on known information is Idempotent]]
3. [[Conditional Expectation over the Trivial Sigma Algebra is Expectation]]
4. [[Smoothing]]
5. [[Conditional Expectation is Linear]]
6. [[Conditional Expectation is Non-Decreasing]]
7. [[Conditional Expectation satisfies Jensen's Inequality]]
8. [[Conditional Expectation with respect to a Set is Integral divided by Probability]]
9. [[Monotone Convergence Theorem for Conditional Expectation]]
10. [[Fatou's Lemma for Conditional Expectation]]
11. [[Dominated Convergence Theorem for Conditional Expectation]]
12. [[Conditioning on Independent Information is just Expectation]]
 

I want to connect to the ways I think of [[Conditional Expectation]]. For example
1. I think of conditional expectation (especially in the sense discrete random variables) as expectation over the  conditional probability. Maybe it would be good to define conditional probability then connect it to conditional expectation through there.
# Definition 2
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $X$ be a [[Discrete Random Variable]] on $\Omega$ with [[Support of a Random Element]] $\{k_{n}\}_{n} \subset \mathbb{R}$. Let $Y$ 
 
# Other Outlinks
- [[Extended L1 Functions]]
- [[Sigma Algebra induced by Random Element]]