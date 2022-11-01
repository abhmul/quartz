---
title: "Bayes Classifier"
---

# Definition
Let $(X, Y, n)$ be a [[Classification Problem]]. The [[Bayes Classifier]] is a [[Classifier]] $f: \mathcal{D} \to [n]$ so that for $x \in \mathcal{D}$

$$f(x) = \arg\min_{y \in [n]} \mathbb{P}(Y=y|X=x)$$