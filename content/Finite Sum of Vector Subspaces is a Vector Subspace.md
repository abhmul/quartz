---

title: "Finite Sum of Vector Subspaces is a Vector Subspace"

---
# Statement
Let $V$ be a [[Vector Space]] over [[Field]] $F$ and suppose $W_{1}, \dots, W_{n} \subset V$ are [[Vector Subspace]]s of $V$ for some $n \in \mathbb{N}$. Then
$$\sum\limits_{i=1}^{n} W_{i} := \{\sum\limits_{i=1}^{n}\mathbf{x}_{i} : \mathbf{x}_{i} \in W_{i} \text{ for } i \in [n]\}$$
is a [[Vector Subspace]] of $V$.

## Proof
Let $\mathbf{a}, \mathbf{b} \in \sum\limits_{i=1}^{n} W_{i}$ and let $c \in F$. Then there exists $\mathbf{x}_{i}, \mathbf{y}_{i} \in W_{i}$ for $i in  [n]$
so that
$$\begin{align*}
\mathbf{a} &= \mathbf{x}_{1} + \cdots + \mathbf{x}_{n}\\
\mathbf{b} &= \mathbf{y}_{1} + \cdots + \mathbf{y}_{n}.
\end{align*}$$
Observe that
$$\begin{align*}
c \mathbf{a} + \mathbf{b} &= c (\mathbf{x}_{1} + \cdots + \mathbf{x}_{n}) + \mathbf{y}_{1} + \cdots + \mathbf{y}_{n}\\
&=(c \mathbf{x}_{1}  + \mathbf{y}_{1}) + \cdots + (c \mathbf{x}_{n} + \mathbf{y}_{n}).
\end{align*}$$
We know that $c \mathbf{x}_{i} + \mathbf{y}_{i} \in W_{i}$ for each $i \in [n]$ because [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]]. Thus, by definition, we have that $c \mathbf{a} + \mathbf{b} \in \sum\limits_{i=1}^{n} W_{i}$. Because [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]], $\sum\limits_{i=1}^{n} W_{i}$ is a [[Vector Subspace]] of $V$. $\blacksquare$