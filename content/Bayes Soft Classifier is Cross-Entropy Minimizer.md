---
title: "Bayes Soft Classifier is Cross-Entropy Minimizer"
---

# Statement
Let $X, Y, n$ be a [[Classification Problem]]. Then the [[Likelihood Soft Classifier]] minimizes [[Cross-Entropy]]. It is the unique minimizer up to modifications on $\mathbb{P}$-[[Null Set]]s of $\mathcal{D}$.

## Proof
Recall that we can write [[Cross-Entropy]] as
$$CE(g) = \mathbb{H}(Y|X) + \mathbb{E}\Big[D_{KL}(\mathbb{P}(Y|X) || g(X) )$$

[[Gibb's Inequality]] tells us that $D_{KL}(\mathbb{P}(Y|X) || g(X) )$ is minimized precisely when $g(X) = \mathbb{P}(Y|X)$, which is the [[Likelihood Soft Classifier]]. $\blacksquare$