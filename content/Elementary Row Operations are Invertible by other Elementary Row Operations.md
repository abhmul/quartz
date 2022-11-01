---

title: "Elementary Row Operations are Invertible by other Elementary Row Operations"

---
# Statement
Let $F$ be a [[Field]], let $m, n \in \mathbb{N}$,  $e \in \text{Row}F^{m \times \cdot}$. Then there exists $e' \in \text{Row}F^{m \times \cdot}$ of the same type so that $\forall A \in F^{m \times \cdot}$,
$$e'(e(A)) = A = e(e'(A))$$
## Proof
We will prove this case by case for the 3 different kinds of [[Elementary Row Operation]]s.

### *Row Scaling*
Let $e$ be the [[Elementary Row Operation]] that scales row $r \in [m]$ by $c \in F$. Observe  scaling row $r \in [m]$ by $c^{-1} \in F$ is also an [[Elementary Row Operation]]. Call it $e'$. Then
$$e'(e(A))_{ij} = \begin{cases}A_{ij}  & \text{if }i \neq r \\
c^{-1}c A_{rj}  & \text{if } i =r \end{cases} = A_{ij},$$
so $e'(e(A)) = A$. Because $c = (c^{-1})^{-1}$, the same argument tells us $e(e'(A)) = A$. $\checkmark$

### *Row Addition*
Let $e$ be the [[Elementary Row Operation]] that adds row $r \in [m]$ scaled by $c \in F$ to row $s \in [m]$. Observe that adding row $r \in [m]$ scaled by $-c \in F$ is another [[Elementary Row Operation]]. Call it $e'$. Then
$$e'(e(A))_{ij}= \begin{cases} A_{ij} & \text{if } i \neq r  \\
(A_{sj} + cA_{rj}) - cA_{rj}  & \text{if } i = s  \\
\end{cases} = A_{ij},$$
so $e'(e(A)) = A$. Since $c = -(-c)$, the same argument tells us $e(e'(A)) = A$. $\checkmark$

### *Row Swap*
Let $e$ be the [[Elementary Row Operation]] that swaps row $r \in [m]$ with row $s \in [m]$. Then if we apply $e$ to itself, we get
$$e(e(A))_{ij} = \begin{cases} A_{ij} & \text{if } i \neq r, i \neq s  \\
A_{rj}  & \text{if } i = r   \\
A_{sj}  & \text{if } i = s  \\
\end{cases} = A_{ij}$$
so $e(e(A)) = A$. $\checkmark$

$\blacksquare$

# Other Outlinks
- [[Elementary Row Operation]]
- [[Matrix]]
- [[Natural Numbers]]