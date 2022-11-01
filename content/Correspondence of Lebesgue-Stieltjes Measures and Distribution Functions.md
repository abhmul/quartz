---
title: "Correspondence of Lebesgue-Stieltjes Measures and Distribution Functions"
---

# Statement
If $F: \mathbb{R} \to \mathbb{R}$ is a [[Distribution Function]], then there is a unique [[Lebesgue-Stieltjes Measure]] $\mu_{F}$ on $\mathbb{R}$ such that $\mu_{F}((a,b]) = F(b) - F(a)$ for all $b > a \in \mathbb{R}$. If $G$ is another such [[Function]], then $F - G$ is a constant.

[[Converse|Conversely]], if $\mu$ is a [[Lebesgue-Stieltjes Measure]] and we define

$$F(x) = 
\begin{cases} 
-\mu((x, 0]) & x < 0 \\
0 & x = 0 \\
\mu((0, x]) & x > 0 \\
\end{cases}
$$
then $F$ is a [[Distribution Function]] and $\mu_{F}=\mu$.

# Proof
[[TODO]] 

# Proof 2 (Informal)
We can define the following [[Category]]s:
1. Let $\mu$ a be a [[Lebesgue-Stieltjes Measure]] on $\mathbb{R}$. Then construct the [[Category]] with
	1. [[Object]]s: elements of $\mathbb{R}$.
	2. [[Morphism]]s: Let $a, b \in \mathbb{R}$. The [[Morphism]] from $a$ to $b$ is
		1. If $a < b$, then the morphism is $\mu((a, b])$.
		2. If $a = b$, then the morphism is $\mu(\emptyset) = 0$.
		3. If $b < a$, then the morphism is $-\mu((b, a])$.

	  Then [[Composition]] of [[Morphism]]s [[Commuting Transforms|commutes]] because [[Measure]]s are $\sigma$-additive. That is if we have $a, b, c \in \mathbb{R}$, then composing their morphisms by addition gets us the morphism from $a$ to $c$. Because $\mu$ is a [[Lebesgue-Stieltjes Measure]], we have that each morphism is finite.
2. Let $F$ be a [[Distribution Function]]. Then construct the [[Category]] with
	1. [[Object]]s: elements of $\mathbb{R}$.
	2. [[Morphism]]s: Let $a, b \in \mathbb{R}$. The [[Morphism]] from $a$ to $b$ is $F(b) - F(a)$. This obviously composes as addition. 

We can [[Natural Transformation|naturally transform]] from one to the other. The [[Non-Decreasing Function]] monotonicity of $F$ ensures that $\mu$ is non-negative on all sets. [[Caratheodory's Theorem]] allows us to take the [[Category]] of $\mu$ to a unique [[Complete Measure]] (since $\mu$ will be [[Sigma-Finite Measure]]).

# Remarks
1. Observe that $G$ must be a [[Distribution Function]] since the [[Set]] of [[Distribution Function]]s is closed under addition of constants.

# Encounters
1. [[Folland - Real Analysis]] - pg 35

# Other Outlinks
- [[Real Numbers]]
- [[Sigma Additive]]