---
title: "Information Space"
---

# Definition
Suppose $\Omega$ is a [[Set]] with [[Sigma Algebra]] $\mathcal{M}$. Suppose $\mu$ is a [[Measure]] on $\mathcal{M}$. Consider the set $$\mathcal{R} =\{(A, B) \in  \mathcal{M} \times \mathcal{M}: \mu(A) \in \mathbb{R} \text{ or } \mu(A) \neq \mu(B) \}$$ and mapping $\imath: \mathcal{R} \to [-\infty, \infty]$ defined as
$$\imath(A||B) := \imath(A, B) = \log \frac{1}{\mu(A)} - \log \frac{1}{\mu(B)}$$
Then $(\Omega, )$

## Properties
1. $\imath(A||A) = 0$
2. $imath$


I really want a space that captures what it means to gain information from learning about an event that allows for cases where probability distributions do not apply (like [[Uniform Distribution]] over all of $\mathbb{R}$).

I also want this way of assigning information quantities to not depend on scaling of the underlying mass distribution. I was thinking that relative information could help with that since it would not be affected by scaling (relative measures of surprisal).

Another way to think about is in terms of conditionals. If I knew the true value was on some finite measure set $A$, then this information quantity would determine a probability distribution on $A$. 

Consider the [[Thought Experiment]] where person $A$ places a $x \in \mathbb{R}$ into a hat, then asks $B$ to 
- Guess what number it is?
- Guess what interval $[n, n+1)$ for $n \in \mathbb{N}$ that is is in?
- $A$ successively reveals what intervals its in and asks $B$ to update guesses.

I think its easier to start with the 3rd case. Some possibilities
1. $A$ first tells $B$ $x \in [0, \infty)$, then $A$ tells $B$ that $x \in [-1, \infty)$. The second piece of information does not provide any new information given the first. Here $S_{2} = [-1, \infty)$ gives us no new information when we know that $x \in S_{1} = [0, \infty)$
2. $A$ tells $B$:
	1. $x \in S_{1} = [0, \infty)$
	2. $x \in S_{2} = (-\infty, 1]$

	$S_{2}$ gives $B$ additional information allowing $B$ to conclude that $x \in [0, 1] = S_{1} \cap S_{2}$.
3. $A$ tells $B$:
	1. $x \in S_{1} = [0, \infty)$
	2. $x \in S_{2} = (-\infty, -1]$

	Here we have a contradiction, so we might imagine that $B$ receives an indeterminate information update. Or we could also say that $x \in \emptyset$.

Lets keep track of the evolution of the [[Sigma Algebra]] representing my knowledge about $x$ as we go. At the beginning $\mathcal{B}_{0} = \{\emptyset, \mathbb{R}\}$.
1. Case 1:
	1. $\mathcal{B}_{1} = \{\emptyset, [0, \infty)\}$... This is not really making sense


What I really want to formalize is this statement that, only knowing that $x \in \mathbb{R}$, I should give equal preference to any hypothesis about the value of $x$.

I think a generalized [[Kullback–Leibler Divergence]] works here. That is, given some prior [[Measure]] $\mu$, and some updated [[Measure]] $\nu$ s.t. $\nu << \mu$ all on $X$, we say 
$$D_{KL}(\nu || \mu) = \int\limits_{X} \log \left(\frac{d\nu}{d \mu}\right) d \nu = \int\limits_{X} \log \left(\frac{d\nu}{d \mu}\right) \frac{d\nu}{d \mu} d \mu$$
If we assume our prior is $\mu = \lambda$, then in case
1. 
	1. $D_{KL}(\nu_{1}||\mu) = \int\limits_X$ ... This doesn't work out nicely unless things are rescaled to be probability distributions.
2. 