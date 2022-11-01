---
title: "Sequence Convergence"
---

# Definition 1
Let $(X, \tau)$ be a [[Topological Space]] and let $(x_n) \subset X$. We say $x_{n}$ converges to $x \in X$ if $\forall V \in \tau$ so that $x \in V$, there exists $N \in \mathbb{N}$ so that $x_{n} \in V$ $\forall n \geq N$. If we have convergence, we write

$$\lim\limits_{n \to \infty} x_{n} = x$$
or 
$$x_{n} \to x \text{ (as } n \to \infty)$$

# Definition 2
Let $(M, d)$ be a [[Metric Space]] and let $(x_n) \subset M$. We say $x_{n}$ converges to $x \in X$ if $\forall \epsilon > 0$ there exists $N > 0$ s.t. $d(x_{n}, x) < \epsilon$ for all $n \geq N$.

# Properties
1. Definition 1 is true [[If and Only If]] Definition 2 is as well on the [[Metric Topology]] of $M$:
	
	**Proof** 
	$(\Rightarrow)$: Suppose Definition 1 holds and $x_{n} \to x \in M$. Let $\epsilon > 0$. Since $B_\epsilon(x)$ is [[Open]] in $M$, there exists $N \in \mathbb{N}$ so that for all $n \geq N$ we have that $x_{n} \in B_{\epsilon}(x)$. By definition of $B_{\epsilon}(x)$, this means $d(x_{n}, x) < \epsilon$ $\checkmark$.
	
	($\Leftarrow$): Suppose Definition 2 holds and $x_{n} \to x \in M$. Let $V \in \tau$ contain $x$. Since [[A Set is Open in the Metric Topology iff it contains a Ball around each Point]], we know there exists $\epsilon > 0$ so that $B_{\epsilon}(x) \subset V$. By Definition 2, there exists $N \in \mathbb{N}$ so that for all $n \geq N$, $d(x_{n}, x) < \epsilon$. In other words, $x_{n} \in B_{\epsilon}(x)$ and thus $x_{n} \in V$. $\checkmark$ $\blacksquare$

	[[TODO]] This could probably reduced to single line about the relationship between sequence convergence and a [[Topological Basis]].


# Other Outlinks
- [[Open Ball]]