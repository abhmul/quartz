---

title: "Row Equivalent Homogenous Matrix Systems have the same Solution Set"

---
# Statement
Let $F$ be a [[Field]], let $m,n \in \mathbb{N}$ and let $A \mathbf{x} = \mathbf{0}$ and $B \mathbf{x} = \mathbf{0}$ be two [[Homogenous Linear System|homogenous]] [[Matrix Equation System]]s. If $A \sim_{R} B$, then 
$$\{\mathbf{x} \in F^{n} : A \mathbf{x} = \mathbf{0}\} = \{\mathbf{y} \in F^{n} : B \mathbf{y} = \mathbf{0}\}.$$
That is, the two [[Matrix Equation System]]s have the same [[Solution Set]].

## Proof
Since $A \sim_{R} B$, there exists $e_{1}, \dots, e_{k} \in \text{Row}F^{m \times n}$ so that 
$$e_{1} \circ \cdots \circ e_{k}(A) = B.$$
Sincee [[Matrix Representation of Elementary Row Operations|row operations can be represented as matrices]], we can rewrite this chain of [[Function Composition]] as
$$E_{1}\cdots E_{k} A = B,$$
[[Matrix Multiplication is a Linear Function]] and [[Linear Operators preserve 0]] so $E_{1} \cdots E_{k} \mathbf{0} = \mathbf{0}$. Thus, since [[Matrix Multiplication Distributes over Columns]], we have that
$$\begin{pmatrix}A &\Big| &\mathbf{0}\end{pmatrix} \sim_{R} \begin{pmatrix}B &\Big| &\mathbf{0}\end{pmatrix}.$$
Recalling that [[Row Equivalent Matrix Systems have the same Solution Set]] completes the proof.
$\blacksquare$
# Other Outlinks
- [[A Linear Equation System is Homogenous iff its constants are 0]]
- [[Matrix Equation Systems are Linear Systems]]
- [[Row Equivalent Matrix Systems]]
- [[Row Equivalent Matrices]]