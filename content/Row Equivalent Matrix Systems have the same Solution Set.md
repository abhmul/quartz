---

title: "Row Equivalent Matrix Systems have the same Solution Set"

---
# Statement
Let $F$ be a [[Field]], let $m,n \in \mathbb{N}$ and let $A \mathbf{x} = \mathbf{b}$ and $B \mathbf{x} = \mathbf{c}$ be two [[Row Equivalent Matrix Systems]]s. Then 
$$\{\mathbf{x} \in F^{n} : A \mathbf{x} = \mathbf{b}\} = \{\mathbf{y} \in F^{n} : B \mathbf{y} = \mathbf{c}\}.$$
That is, the two [[Matrix Equation System]]s have the same [[Solution Set]].

## Proof
Since $\begin{pmatrix}A &\Big| &\mathbf{b}\end{pmatrix} \sim_{R} \begin{pmatrix}B &\Big| &\mathbf{c}\end{pmatrix}$, there exists $e_{1}, \dots, e_{k} \in \text{Row}F^{m \times \cdot}$ so that 
$$e_{1} \circ \cdots \circ e_{k}(\begin{pmatrix}A &\Big| &\mathbf{b}\end{pmatrix}) = \begin{pmatrix}B &\Big| &\mathbf{c}\end{pmatrix}.$$
Since [[Matrix Representation of Elementary Row Operations|row operations can be represented as matrices]], we can rewrite this chain of [[Function Composition]] as
$$E_{1}\cdots E_{k} \begin{pmatrix}A &\Big| &\mathbf{b}\end{pmatrix} = \begin{pmatrix}B &\Big| &\mathbf{c}\end{pmatrix},$$
where $E_{i}$ is the [[Matrix Representation of Elementary Row Operations|matrix representation]] of $e_{i}$ for $i \in [k]$. Since [[Matrix Multiplication Distributes over Columns]] we have that 
$$\begin{align*}
E_{1} \cdots E_{k} \mathbf{b} &= \mathbf{c}\\
E_{1} \cdots E_{k} A &= B.
\end{align*}$$
Now suppose $\mathbf{x} \in F^{n}$ so that $A \mathbf{x} = \mathbf{b}$. Then
$$\mathbf{c} = E_{1} \cdots E_{k} \mathbf{b} = E_{1} \cdots E_{k} A = B$$
so $\mathbf{x} \in \{\mathbf{y} \in F^{n} : B \mathbf{y} = \mathbf{0}\}$ and 
$$\{\mathbf{x} \in F^{n} : A \mathbf{x} = \mathbf{b}\} \subset \{\mathbf{y} \in F^{n} : B \mathbf{y} = \mathbf{c}\}.$$
But since $\begin{pmatrix}A &\Big| &\mathbf{b}\end{pmatrix} \sim_{R} \begin{pmatrix}B &\Big| &\mathbf{c}\end{pmatrix}$ means $\begin{pmatrix}B &\Big| &\mathbf{c}\end{pmatrix} \sim_{R} \begin{pmatrix}A &\Big| &\mathbf{b}\end{pmatrix}$,  the same argument gives us that
$$\{\mathbf{x} \in F^{n} : A \mathbf{x} = \mathbf{b}\} \supset \{\mathbf{y} \in F^{n} : B \mathbf{y} = \mathbf{c}\}.$$
Therefore
$$\{\mathbf{x} \in F^{n} : A \mathbf{x} = \mathbf{b}\} = \{\mathbf{y} \in F^{n} : B \mathbf{y} = \mathbf{c}\}.$$
$\blacksquare$

## Remarks
1. [[TODO]] this could be simplified by looking at [[Matrix Inverse|invertible]] [[Matrix|matrices]] as a [[Group]]. Then establish that [[Elementary Row Operation]]s are just invertible matrices.
# Other Outlinks
- [[Elementary Row Operation]]
- [[Row Equivalent Matrices]]
-