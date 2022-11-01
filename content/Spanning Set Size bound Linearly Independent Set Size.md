---

title: "Spanning Set Size bound Linearly Independent Set Size"

---
# Statement
Let $V$ be a [[Vector Space]] over [[Field]] $F$ that is [[Spanning Set|spanned by]] $R \subset V$ and denote $|R| = \infty \in \bar{\mathbb{N}}$ if $R$ is an [[Infinite Set]]. Then if $S$ is [[Linearly Independent]] in $V$, $|S| \leq |R|$. 

## Proof
First note that if $|R| = \infty$, then this is trivially true since all $S \subset V$ are such that $|S| \leq \infty$. $\checkmark$

Now suppose $|R| = n \in \mathbb{N}$. Suppose $m \in \mathbb{N}$ so that $m > n$ and let $S \subset V$ be s.t. $|S| \geq m$. We will show that $S$ must be [[Linearly Dependent]]. We write $S' = \{\mathbf{a}_{1}, \dots, \mathbf{a}_{m}\} \subset S$ for distinct $\mathbf{a}_{1}, \dots, \mathbf{a}_{m}$. Suppose $c_{1}, \dots, c_{m} \in F$ so that
$$c_{1} \mathbf{a}_{1} + \cdots + c_{m} \mathbf{a}_{m} = \mathbf{0}.$$
Since $\mathbf{b}_{1}, \dots, \mathbf{b}_{n}$ [[Subspace Span|span]] $V$, there must exist $(d_{ij} \in F)_{i \in [n], j \in [m]}$ so that
$$\mathbf{a}_{j} = \sum\limits_{i=1}^{n} d_{ij} \mathbf{b}_{i}$$
Thus, we get
$$\begin{align*}
\mathbf{0} &= \sum\limits_{j=1}^{m} \sum\limits_{i=1}^{n} c_{j} d_{ij} \mathbf{b}_{i} \\
&= \mathbf{b}_{1} \sum\limits_{j=1}^{m}  c_{j} d_{1j} + \cdots + \mathbf{b}_{n} \sum\limits_{j=1}^{m}  c_{j} d_{nj} \tag{1}
\end{align*} $$
Now note that, if we were to have that 
$$\sum\limits_{j=1}^{m}  c_{j} d_{ij} = 0 \text{ } \forall i \in [n] \tag{2}$$
then (1) will hold. We show that non-trivial $c_{1}, \dots, c_{m} \in F$ exist. Rewriting the [[Equation System]] as
$$D \mathbf{c} = \mathbf{0}$$
where $D \in F^{n \times m}$ is defined as $D_{ij} = d_{ij}$ for $i \in [n], j \in [m]$, and $\mathbf{c} \in F^{m}$ is defined as $\mathbf{c}_{j} = c_{j}$ for $j \in [m]$. This is a [[Homogenous Linear System|homogenous]] [[Matrix Equation System]]. Since $n < m$, we know [[Short Homogenous Matrix Systems have nontrivial solutions|there exists a nontrivial solution]] $\mathbf{c}^{*}$. Therefore $S'$ is [[Linearly Dependent]], making $S$ [[Linearly Dependent]].

By [[Contraposition]], we have that any [[Linearly Independent]] $S \subset V$ is s.t. $|S| \leq n$. $\checkmark$ $\blacksquare$

## Remarks
1. I wonder if there is a way to do this without invoking [[Matrix Equation System]]s. We already have the relationships
	- [[A Set is a Basis iff it is a Maximal Linearly Independent Set]]
	- [[A Set is a Basis iff it is a Minimal Spanning Set]]
	
	but these do not relate the size of **one** spanning set to **all** linearly independent sets.
# Other Outlinks
- [[Counting Measure]]
- [[Natural Numbers]]
- [[Extended Natural Numbers]]