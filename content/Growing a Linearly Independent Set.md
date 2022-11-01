---

title: "Growing a Linearly Independent Set"

---
# Statement
Let $V$ be a [[Vector Space]] over [[Field]] $F$ and let $S \subset V$ be [[Linearly Independent]]. Suppose $\mathbf{v} \in V$, but $\mathbf{v} \not\in \text{span} S$. Then $S \cup \{\mathbf{v}\}$ is [[Linearly Independent]].

## Proof
Suppose not. Then there exists $n \in \mathbb{N}$ and [[Linearly Dependent]] $\{\mathbf{a}_{1}, \dots, \mathbf{a}_{n}\} \subset S \cup \{\mathbf{v}\}$. We must have some $\mathbf{a}_{i} = \mathbf{v}$  for $i \in [n]$, since otherwise $S$ would not be [[Linearly Independent]]. [[Without Loss of Generality|WLOG]] let $\mathbf{a}_{n} = \mathbf{v}$. Then we have nontrivial $c_{i} \in F$ for $i \in F$ so that
$$c_{1} \mathbf{a}_{1} + \cdots c_{n-1} \mathbf{a}_{n-1} + c_{n} \mathbf{v} = \mathbf{0}$$
If $c_{n} = 0$, then $\{\mathbf{a}_{1}, \dots, \mathbf{a}_{n-1}\} \subset S$ is [[Linearly Dependent]] contradicting the [[Linearly Independent|independence]] of $S$. Therefore $c_{n} \neq 0$. Then we have that
$$\mathbf{v} = c_{n}^{-1} c_{1} \mathbf{a}_{1} + \cdots + c_{n}^{-1} c_{n-1} \mathbf{a}_{n-1}$$
and $\mathbf{v} \in \text{span} S$ $\unicode{x21af}$. 

Therefore $S \cup \{\mathbf{v}\}$ is [[Linearly Independent]]. $\blacksquare$

## Remarks
1. This gives us the following process for growing a [[Linearly Independent]] [[Set]] on some set $R$:
	1. Start with $S = \emptyset$;
	2. While $R \setminus \text{span} S \neq \emptyset$:
		1. $S  \leftarrow S \cup \{\mathbf{v}\}$ for arbitrary $\mathbf{v} \in R$.
	
	If this process terminates, then we must have $S$ is a [[Maximal]] [[Linearly Independent]] set on $R$. Otherwise, by our theorem [[Growing a Linearly Independent Set]], the algorithm would not have terminated, giving us a [[Proof by Contradiction|contradiction]]. In particular, if $R$ is a [[Vector Space]], then $S$ must be a [[Vector Space Basis]] for $R$ since [[A Set is a Basis iff it is a Maximal Linearly Independent Set]].