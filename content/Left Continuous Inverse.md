---
title: "Left Continuous Inverse"
---

# Definition
Let $F: \mathbb{R} \to \mathbb{R}$ be a [[Distribution Function]]. The [[Left Continuous Inverse]] of $F$ is defined

$$F^{\leftarrow}(x) = \inf\{s \in \mathbb{R} : F(s) \geq x\}$$

# Properties
1. For fixed $x \in \mathbb{R}$, write $A = \{s \in \mathbb{R} : F(s) \geq x\}$. Then $A$ is [[Closed]]. Thus, $F^{\leftarrow}(x) \in A$ when $F^{\leftarrow}(x) \in \mathbb{R}$ since [[There Exists a Sequence Converging to Extremum]].

	**Proof**: Recall that [[A Set is Closed in a Metric Space iff it contains all its Sequential Limits]]. Let $(s_{n}) \subset A$ be a [[Sequence]]that [[Sequence Convergence|converges]] to $t \in \mathbb{R}$.  By definition of $A$
	$$F(s_{n}) \geq x$$
	Recall that [[Every Sequence on the Reals contains a Monotone Subsequence]]. Let this [[Subsequence]] be $(s_{n_{k}})$. [[Every Subsequence of a Convergent Sequence converges to the same Limit]], so $s_{n_{k}} \to t$. Now consider the following two cases:
	1. $(s_{n_{k}})$ is [[Non-Decreasing Function]]: Then, because [[Monotone Sequences converge to their Extremum]], we know $s_{n_{k}} \to \sup\{s_{n_{k}}\} = t$. Thus $t \geq s_{n_{1}} \in A$ (by definition of [[Supremum]]). Since $F$ is [[Non-Decreasing Function]], we have that $$F(t) \geq F(s_{n_{1}}) \geq x$$ and $t \in A$.
	2. $(s_{n_{k}})$ is [[Non-Increasing Function]]: Then we know $s_{n_{k}} \to \inf\{s_{n_{k}}\} = t$. Since $F$ is [[Right-Continuous]] and $(s_{n_{k}}) \subset [t, \infty)$, we know that $F(s_{n_{k}}) \to F(t)$. Since $F(s_{n_{k}}) \geq x$ $\forall k \in \mathbb{N}$, then by the [[Order Limit Theorem]]$$F(t) \geq x$$ and thus $t \in A$.
	
	Since $(s_{n})$ was arbitrary, we have that $A$ is [[Closed]]. $\blacksquare$
2. $F^{\leftarrow}$ is [[Non-Decreasing Function]].

	**Proof**: Let $A_{x}= \{s \in \mathbb{R} : F(s) \geq x\}$. Suppose $y \leq x$. Then if $s \in A_x$, we have that
	$$F(s) \geq x \geq y$$ and thus $s \in A_{y}$. Therefore $A_{x} \subset A_{y}$. Since [[Infimums are Non-Increasing Set Functions]] we see that $F^{\leftarrow}(x) = \inf A_{x} \geq \inf A_{y} = F^{\leftarrow}(y)$, proving that $F^{\leftarrow}$ is [[Non-Decreasing Function]]. $\blacksquare$
	
3. $F^{\leftarrow}$ is [[Left-Continuous]].

	**Proof**: Let $x \in \mathbb{R}$. Let $A_{x}$ be defined as in (2). First we claim that
	$$\bigcap_{\epsilon>0} A_{x - \epsilon} = A_{x}$$
	To see this, first observe that since $A_{x} \subset A_{x-\epsilon}$ $\forall \epsilon > 0$ (as shown in (2)), we see that
	$$\bigcap_{\epsilon>0} A_{x - \epsilon} \supset A_{x}$$
	On the other hand, suppose $s \in A_{x - \epsilon}$ for all $\epsilon > 0$. Then $F(s) \geq x - \epsilon$ for all $\epsilon > 0$. By the [[Epsilon Principle]], we have that $F(s) \geq x$ and $s \in A_{x}$. Thus
	$$\bigcap_{\epsilon>0} A_{x - \epsilon} \subset A_{x}$$
	Putting those two directions together we get that 
	$$\bigcap_{\epsilon>0} A_{x - \epsilon} = A_{x}$$
	so their [[Infimum]]s are also the same. Now we claim that
	$$\inf\bigcap_{\epsilon>0} A_{x - \epsilon} = \lim\limits_{\epsilon \downarrow 0}\inf A_{x - \epsilon}$$
	To see this, first recall from (2) that $\inf A_{x-\epsilon} \leq \inf A_{x}$ for all $\epsilon > 0$ . Thus, by the [[Order Limit Theorem]], 
	$$\lim\limits_{\epsilon \downarrow  0} \inf A_{x-\epsilon} \leq \inf A_{x} = \inf\bigcap_{\epsilon>0} A_{x - \epsilon}$$
	Now on the other hand, if 
	$$\lim\limits_{\epsilon \downarrow  0} \inf A_{x-\epsilon} < \inf\bigcap_{\epsilon>0} A_{x - \epsilon}$$
	Then there exists $y \in \mathbb{R}$ s.t. 
	$$\lim\limits_{\epsilon \downarrow  0} \inf A_{x-\epsilon} < y < \inf\bigcap_{\epsilon>0} A_{x - \epsilon}$$
	Since [[Infimums are Non-Increasing Set Functions]], we have that $y > \inf A_{x-\epsilon}$ for all $\epsilon > 0$ (otherwise the limit would exceed $y$ and never return to fall below $y$). However, since $y < \inf\bigcap_{\epsilon>0} A_{x - \epsilon}$, there exists $z \in \mathbb{R}$ s.t. $y < z < \inf\bigcap_{\epsilon>0} A_{x - \epsilon}$ and by definition of [[Infimum]], $z < \bigcap_{\epsilon>0} A_{x - \epsilon}$. Thus there must be some $\epsilon > 0$ s.t. $z < A_{x - \epsilon}$ (otherwise, there is always an element at or below $z$; recall $A_{x-\epsilon}$ is a [[Non-Increasing Function]] [[Sequence]] of [[Set]]s). But then $y < z \leq \inf A_{x - \epsilon}$, contradicting above. Therefore
	$$F^{\leftarrow}(x) = \inf A_{x} = \inf\bigcap_{\epsilon>0} A_{x - \epsilon} = \lim\limits_{\epsilon \downarrow 0}\inf A_{x - \epsilon} = \lim\limits_{y \uparrow x} F^{\leftarrow}(y)$$
	and $F^{\leftarrow}$ is [[Left-Continuous]]. $\blacksquare$

# Other Outlinks
- [[Real Numbers]]
- [[Set Intersection]]

# Encounters
1. [[Resnick - A Probability Path]] - Ch unknown, pg unknown (I think ch 2)
	