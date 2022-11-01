---
title: "Right Continuous Inverse"
---

# Definition
Let $F: \mathbb{R} \to \mathbb{R}$ be a [[Distribution Function]]. The [[Right Continuous Inverse]] of $F$ is defined

$$F^{\rightarrow}(x) = \inf \{s \in \mathbb{R} : F(s) > x\}$$
## Properties
1. $F^{\rightarrow}$ is [[Non-Decreasing Function]].

	**Proof**: Let $A_{x} = \{s \in \mathbb{R} : F(s) > x\}$. Suppose $y \leq x$. Then for all $s \in A_{x}$, we have that $s > x \geq y$ so $s \in A_{y}$. Thus, $A_{x} \subset A_{y}$. Since [[Infimums are Non-Increasing Set Functions]], we have that $F^{\rightarrow}(y) \leq F^{\rightarrow}(x)$. $\blacksquare$
2. $F^{\rightarrow}$ is [[Right-Continuous]].

	**Proof**: [[TODO]] 
3. $\lim\limits_{t \uparrow x} F^{\rightarrow}(t) = F^{\leftarrow}(x)$

	**Proof**: [[TODO]] 

# Other Outlinks
- [[Real Numbers]]
- [[Left Function Limit]]
- [[Set]]