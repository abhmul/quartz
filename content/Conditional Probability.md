---
title: "Conditional Probability"
---

[[TODO]] - need to rope in [[Regular Conditional Distribution]]. This page can be redefined in terms of [[Regular Conditional Distribution]] of [[Identity Function]].

# Definition 1
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $A \in \mathcal{B}$ be an [[Event]]. Let $\mathcal{G} \subset \mathcal{B}$ be a sub-[[Sigma Algebra]]. Then the [[Conditional Probability]] of $A$ given $\mathcal{G}$ is
$$\mathbb{P}(A|\mathcal{G}) = \mathbb{E}(1_{A}|\mathcal{G})$$

Similarly to [[Conditional Expectation]], if $Y$ is a [[Random Variable]] on $\Omega$ then
$$\mathbb{P}(A|Y) = \mathbb{P}(A|\sigma(Y))$$
and if $B \in \mathcal{B}$ then
$$\mathbb{P}(A|B) = \mathbb{P}(A|1_{B})(\omega)$$
for (any) $\omega \in B$.

# Definition 2
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $A, B \in \mathcal{B}$ be [[Event]]s such that $\mathbb{P}(B) \neq 0$. Then the [[Conditional Probability]] of $A$ given $B$ is
$$\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$


# Remarks
1. Since [[Indicator Functions on Measureable Sets are in L+]] we know $1_{A} \in L^{+}(\mathcal{B}) \subset \bar{L^{1}}(\mathcal{B})$, and using [[Conditional Expectation]] makes sense in our definition.
2. We can also write the two auxiliary definitions in Definition 1 as $$\mathbb{P}(A|Y) = \mathbb{E}(1_{A}|Y)$$ and $$\mathbb{P}(A|B) = \mathbb{E}(1_{A}|B)$$
3. We should check that Definition 1 naturally leads to Definition 2:

	**Proof**: Suppose $A, B \in \mathcal{B}$ so that $\mathbb{P}(B) \neq 0$. Then $$\mathbb{P}(A|B) = \mathbb{E}(1_{A}|B) = \frac{\mathbb{E}(1_{B}1_{A})}{\mathbb{P}(B)} = \frac{\mathbb{E}(1_{B \cap A})}{\mathbb{P}(B)} = \frac{\mathbb{P}(B \cap A)}{\mathbb{P}(B)}$$where the second equality follows because [[Conditional Expectation with respect to a Set is Integral divided by Probability]]. $\blacksquare$

	Thus, we can use whichever definition is more convenient.
4. Suppose $B \in \mathcal{B}$ so that $\mathbb{P}(B) \neq 0$. Then $(\Omega, \mathcal{B}, \mathbb{P}(\cdot | B))$ is a [[Probability Space]] on $\Omega$.
	
	**Proof**: All we need do is check $\mathbb{P}(\cdot|B)$ is a valid [[Probability Measure]]. We will rely on the fact that $\mathbb{P}$ is a probability measure
	1. If $A \in \mathcal{B}$, $\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)} \in [0,1]$ since $A \cap B \subset B$ so $0 \leq \mathbb{P}( A \cap B) \leq \mathbb{P}(B)$. $\checkmark$
	2. $\mathbb{P}(\Omega|B) = \frac{\mathbb{P}(\Omega \cap B)}{\mathbb{P}(B)} =  \frac{\mathbb{P}(B)}{\mathbb{P}(B)} = 1$. $\checkmark$
	3. Suppose $(A_{n})_{n=1}^{\infty} \subset \mathcal{B}$ are [[Mutually Disjoint]] [[Event]]s. Then $$\mathbb{P}(\bigsqcup\limits_{n \in \mathbb{N}}A_{n}|B) = \frac{\mathbb{P}\Big( \big(\bigsqcup\limits_{n \in \mathbb{N}}A_{n} \big) \cap B \Big)}{\mathbb{P}(B)} =  \frac{\mathbb{P}\Big( \bigsqcup\limits_{n \in \mathbb{N}}(A_{n} \cap B) \Big)}{\mathbb{P}(B)} = \sum\limits_{n=1}^{\infty} \frac{\mathbb{P}(A_{n} \cap B)}{\mathbb{P}(B)} = \sum\limits_{n=1}^{\infty} \mathbb{P}(A|B)$$
		$\checkmark$
	
	Thus $\mathbb{P}(\cdot | B)$ is a [[Probability Measure]]. $\blacksquare$

1. I used to think about [[Conditional Expectation]] as just an [[Expectation]] taken with the [[Conditional Probability]]s. Here, however we've taken [[Conditional Expectation]] to be more fundamental. My old way of thinking about this is still valid, as I show in [[TODO]]

# Other Outlinks
- [[Extended L1 Functions]]
- [[Null Set]]
- [[Product of Indicator Functions is Intersection]]
- [[Sigma Algebra induced by Random Element]]