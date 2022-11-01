---
title: "Vector Space"
---

# Definition
Suppose $V$ is a [[Nonempty]] [[Set]], $F$ is a [[Field]], and $+: V \times V \to V$ and $*: F \times V \to V$ are [[Operation]]s. Then $(V, F, +, *)$ is a [[Vector Space]] if
1. $(V, +)$ is an [[Abelian Group]]:
	1. [[Additive Identity]]: There exists $\mathbf{0} \in V$ so that for all $v \in V$ we have that $\mathbf{0} + v = v$
	2. [[Associativity]] of $+$: For all $x,y,z \in V$, $(x + y) + z = x + (y + z)$
	3. [[Commutativity]] of $+$: For all $x, y \in V$, $x + y = y + x$ 
	4. [[Additive Inverse]]s: If $x \in V$, then there exists $-x \in V$ so that $x + (-x) = \mathbf{0}$
2. Compatibility with [[Scalar Multiplication]] ($*$):
	1. [[Multiplicative Identity]]: For all $v \in V$ we have that $1 * v = v$ (where $1$ is the [[Multiplicative Identity]] of $F$).
	2. [[Associativity]]: For all $c,d \in F$, $v \in V$, we have that $(cd)*v = c*(d*v)$
	3. [[Distributivity]] of $*$ over $+$: For all $u, v \in V$ and $c \in F$, $c*(u + v) = c*u + c*v$
	4. [[Distributivity]] of $*$ over $+_{F}$: For all $u \in V$ and $c, d \in F$, $(c +_{F} d) * u = c * u + d * u$

## Examples
1. [[Functions to a Field form a Vector Space]]
2. [[N-tuples over a Field form a Vector Space]]

### n-tuples


## Properties
### 1. Scalar multiplication by $0$ is $\mathbf{0}$
Suppose $v \in V$. Then $0v = \mathbf{0}$.
#### Proof
$$\begin{align*}
&0v = (0 + 0)v = 0v + 0v\\
&\Rightarrow \mathbf{0} = 0v.
\end{align*}$$
$\blacksquare$

### 2. Scalar multiplication with $\mathbf{0}$ is $\mathbf{0}$
Suppose $c \in F$. Then $c \mathbf{0} = \mathbf{0}$.

#### Proof
$$\begin{align*}
c \mathbf{0} &= c (\mathbf{0} + \mathbf{0}) = c \mathbf{0} + c \mathbf{0}\\
\Rightarrow &\mathbf{0} = c \mathbf{0}
\end{align*}$$
$\blacksquare$

### 3. If scalar product is $\mathbf{0}$, then either scalar is $0$ or vector is $\mathbf{0}$
Suppose $v \in V$, $c \in F$ and that $cv = \mathbf{0}$. Then either $c = 0$ or $v = \mathbf{0}$.
#### Proof
If $c = 0$, then we are done (by (1) above). Otherwise, $c$ has [[Multiplicative Inverse]] $c^{-1}$. Then
$$\begin{align*}
v = 1v = (c^{-1}c)v = c^{-1}(cv) = c^{-1} \mathbf{0} = \mathbf{0}.\\
\end{align*}$$
$\blacksquare$

### ![[Scalar product with -1 is additive inverse in vector spaces]]
