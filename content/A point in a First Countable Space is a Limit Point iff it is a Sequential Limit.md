---
title: "A point in a First Countable Space is a Limit Point iff it is a Sequential Limit"
---

# Statement
Suppose $(X, \tau)$ is a [[First Countable Space]] and let $S \subset X$. Then $\bar{S} = \{x :  \exists (x_n) \subset S \text{ s.t. } x_{n} \to x\}$. That is, $x \in X$ is a [[Limit Point]] of $S$ [[If and Only If]] it is a [[Sequence Convergence|sequential limit]] of a [[Sequence]] in $S$.

## Proof
Denote $T = \{x :  \exists (x_n) \subset S \text{ s.t. } x_{n} \to x\}$. 

Because we know [[Sequential Limits are Limit Points of the Sequence]], we know for each $x \in T$, there exists $\{x_n\}_{n=1}^{\infty} \subset S$ so that $x$ is a [[Limit Point]] of $\{x_{n}\}$. Since [[Limit Points of a subset are Limit Points of the original Set]], $x$ is also a [[Limit Point]] of $S$ and $\bar{S} \supset T$. $\checkmark$

On the other hand, suppose $x \in \bar{S}$. Since $X$ is a [[First Countable Space]], there is some [[Countable]] [[Neighborhood Basis]] $\mathcal{B}_{x} \subset \tau$ of $x$. Enumerate $\mathcal{B}_{x} = \{B_n\}_{n=1}^{\infty}$. Construct $(x_{n})$ [[Induction|inductively]] in the following way:
1. Set $A_{1} = B_{1}$. Since $B_{1}$ is [[Open]] and $x \in B_{1}$, there exists $x_{1} \in A_{1} \cap S$.
2. Set $A_{2} = B_{2} \cap A_{1}$. Since $B_{2}$ is [[Open]] and [[Topological Space|topological spaces are closed under finite set intersections]], $A_{2}$ is [[Open]]. Since $x \in A_{1}$ and $x \in B_{2}$, we see $x \in A_{2}$. Thus, as $x$ is a [[Limit Point]], there exists $x_{2} \in A_{2} \cap S$.
3. Continue in this fashion...

Now we show $(x_{n})$ [[Sequence Convergence|converges]] to $x$. Suppose $U \subset X$ [[Open]] so that $x \in U$. Then there exists $N \in \mathbb{N}$ so that $B_{N} \subset U$ since $\mathcal{B}_{x}$ is a [[Neighborhood Basis]] of $x$. By construction, $A_{n} \subset B_{N}$ for all $n \geq N$. Since $x_{n} \in A_{n}$ by construction, we have that for all $n \geq N$, 
$$x_{n} \in A_{n} \subset B_{N} \subset U$$
and $(x_{n}) \to x$. Thus $x \in T$ and $\bar{S} \subset T$. $\checkmark$

Therefore $\bar{S} = T$. $\blacksquare$
