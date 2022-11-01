---
title: "Closure of a Set is all its Limit Points"
---

# Statement
Let $X, \tau$ be a [[Topological Space]] and let $S \subset X$. Then $$\text{cl} S = \bar{S}$$

## Proof
First we show $\bar{S}$ is [[Closed]]. Because [[All points in a Set are Limit Points]], $\bar{S} \supset S$, so if we show $\bar{S}$ is [[Closed]], then $\bar{S} \supset \text{cl}S$. To see this, we will shoe $\bar{S}^{C}$ is [[Open]]. Suppose $y \in \bar{S}^{C}$. Then, by definition of $\bar{S}$, we know that there exists $U_{y} \in \tau$ s.t. $y \in U_{y}$ but $U_{y} \cap S = \emptyset$. Then
$$U = \bigcup\limits_{y \in \bar{S}}^{C} U_{y}$$
is [[Open]]. We see $U \supset \bar{S}^{C}$ since for $y \in \bar{S}^{C}$ there is a $U_{y}$ that contains it. To see $U \subset \bar{S}^{C}$, observe that if it weren't then it would contain some [[Limit Point]] $x$ of $S$. This means there is some $y \in \bar{S}^{C}$ so that $x \in U_{y}$. By definition of [[Limit Point]], we have that $U_{y} \cap S \neq \emptyset$, [[Proof by Contradiction|contradicting]] our assumption that $U_{y}  \cap S = \emptyset$. Thus $U = \bar{S}^{C}$ and $\bar{S}$ is [[Closed]]. 

Next we show every [[Closed]] set containing $S$ contains all of the [[Limit Point]]s of $S$. Suppose $K \supset S$ is [[Closed]]. Since $K$ is [[Closed]], $K^{C}$ is [[Open]]. Suppose there was some [[Limit Point]] $x$ of $S$ so that $x \not\in K$. Then $x \in K^{C}$. Thus, by definition of [[Limit Point]], $K^{C} \cap S \neq \emptyset$. But then $K^{C} \cap K \neq \emptyset$, giving us a [[Proof by Contradiction|contradiction]]. Thus $\bar{S} \subset K$. Since $K$ was arbitrary, we have that $\bar{S} \subset \text{cl}S$. 

Thus, we conclude that $\bar{S} = \text{cl}S$. $\blacksquare$

# Other Outlinks
- [[Closure]]
- [[Limit Point]]