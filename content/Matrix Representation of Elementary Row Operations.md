---

title: "Matrix Representation of Elementary Row Operations"

---
# Statement
Let $F$ be a [[Field]] and let  $m \in \mathbb{N}$.. All [[Elementary Row Operation]]s of $\text{Row} F^{m \times \cdot}$ can be represented as elements of $F^{m \times m}$. The representations are
1. *Row scaling* row $r \in [m]$ by $c \in F$can be represented as $$R_{ij} = \begin{cases} 1  & \text{if } i = j \neq r  \\
c  & \text{if } i=j=r \\
0  & \text{otherwise} \end{cases}$$
2. *Row adding* row $r \in [m]$ scaled by $c \in F$ to row $s \in [m]$ can be represented as $$R_{ij} = \begin{cases} 1  & \text{if } i = j \\
c  & \text{if } i=s, j=r \\
0  & \text{otherwise} \end{cases}$$
3. *Row swapping* row $r \in [m]$ with row $s \in [m]$ can be represented as $$R_{ij} = \begin{cases} 1  & \text{if } i = j \neq r, s \\
1  & \text{if } i=s, j=r \\
1  & \text{if } i=r, j=s \\
0  &  \text{otherwise} \end{cases}$$
Application of these [[Elementary Row Operation]]s can be represented by [[Matrix Multiplication]].

## Proof
[[TODO]], the proof is simple, just apply each one and show they give the desired result.