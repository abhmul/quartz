---
title: "Cross-Entropy"
---

# Definition
Let $(X, Y, n)$ be a [[Classification Problem]]. Then the [[Cross-Entropy]] of a [[Soft Classifier]] $g$ is
$$\begin{align*}
CE(g) &= \mathbb{E}\Big[-\sum\limits_{y \in [n]} 1_{Y=y} \log g(X)_{y} \Big]
\end{align*}$$

## Remarks
1. We can rewrite the [[Cross-Entropy]] in terms of [[Conditional Entropy]] and [[Kullback–Leibler Divergence]]: $$\begin{align*}
CE(g) &= \mathbb{E}\Big[-\sum\limits_{y \in [n]} 1_{Y=y} \log g(X)_{y} \Big]\\
&=-\sum\limits_{y \in [n]} \mathbb{E} \Big[ 1_{Y=y} \log g(X)_{y} \Big] &\text{(Linearity)}\\
&=-\sum\limits_{y \in [n]} \mathbb{E} \Big[ \mathbb{E}\big[ 1_{Y=y} \log g(X)_{y} | X \big] \Big] &\text{(Smoothing)}\\
&=-\sum\limits_{y \in [n]} \mathbb{E} \Big[ \mathbb{E}\big[ 1_{Y=y} | X \big] \log g(X)_{y} \Big] &(g(X) \text{ is }Y-\text{measureable})\\
&=-\sum\limits_{y \in [n]} \mathbb{E} \Big[ \mathbb{P}(Y=y|X) \log g(X)_{y} \Big]\\
&=-\sum\limits_{y \in [n]} \mathbb{E} \Big[ \mathbb{P}(Y=y|X) \log \big( \frac{g(X)_{y}}{\mathbb{P}(Y=y|X)} \mathbb{P}(Y=y|X) \big) \Big]\\
&=-\sum\limits_{y \in [n]} \mathbb{E} \Big[ \mathbb{P}(Y=y|X) \log \mathbb{P}(Y=y|X) + \mathbb{P}(Y=y|X) \log \big( \frac{g(X)_{y}}{\mathbb{P}(Y=y|X)} \big) \Big]\\
&=\mathbb{E}\Big[ -\sum\limits_{y \in [n]} \mathbb{P}(Y=y|X) \log \mathbb{P}(Y=y|X) \Big] + \mathbb{E}\Big[ -\sum\limits_{y \in [n]} \mathbb{P}(Y=y|X) \log \big( \frac{g(X)_{y}}{\mathbb{P}(Y=y|X)} \big) \Big]\\
&=\mathbb{H}(Y|X) + \mathbb{E}\Big[D_{KL}(\mathbb{P}(Y|X) || g(X) ) \Big]
\end{align*}$$
	The only term here that depends on $g$ is the [[Kullback–Leibler Divergence]] term.

# Other Outlinks
- [[Smoothing]]
- [[Linearity of Expectation]]
- [[Conditional Probability]]
- [[Conditional Expectation]]
- [[Measureable Function]]