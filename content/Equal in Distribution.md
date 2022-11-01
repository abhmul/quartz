---
title: "Equal in Distribution"
---

# Definition
Let $X, Y$ be [[Random Variable]]s and let $F_{X}, F_{Y}: \mathbb{R} \to \mathbb{R}$ be their respective [[Probability Distribution Function]]s. Then $X \overset{\text{d}}{=} Y$ ($X, Y$ are [[Equal in Distribution]]), if $F_{X}$ = $F_{Y}$.

# Properties
1. If two [[Random Variable]]s are [[Equal in Distribution]], then their induced [[Induced Probability Measure]]s on $\mathbb{R}$ must be the same because of the [[Correspondence of Lebesgue-Stieltjes Measures and Distribution Functions]].
2. Suppose $X \overset{d}{=} Y$. Overload $F_{X} = F = F_{Y}$ as both the [[Distribution Function]]s and induced [[Induced Probability Measure]]s for $X, Y$ respectively. Then for some [[Borel Measureable Function]] $h: \mathbb{R} \to \mathbb{R}$, we have that

	$$\int\limits_{A} h(x)F_{X}(dx) = \int\limits_{A} h(x)F(dx) = \int\limits_{A} h(y)F_{Y}(dy)$$
	In particular $\forall k \in \mathbb{N}$
	$$\mathbb{E}|X|^{k} = \mathbb{E}|Y|^{k}$$
	That is, $X$ has the same [[Moment]]s as $Y$.
