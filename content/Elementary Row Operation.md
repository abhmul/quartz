---

title: "Elementary Row Operation"

---
# Definition
Let $F$ be a [[Field]] and let  $m \in \mathbb{N}$. Let $F^{m \times \cdot} = \bigcup\limits_{n \in  \mathbb{N}} F^{m \times n}$. An [[Elementary Row Operation]] is one of the following 3 types of [[Function]]s on $F^{m \times \cdot}$:
1. Let $c \in F \setminus \{0\}$ and $r \in [m]$. Then $e: F^{m \times \cdot} \to F^{m \times \cdot}$ defined as $$e(A)_{ij} = \begin{cases} A_{ij} & \text{if } i \neq r  \\
cA_{rj}  & \text{if } i = r  \\
\end{cases}$$ is an [[Elementary Row Operation]] (known as a *row scaling*)
2. Let $c \in F$ and $r, s \in [m]$. Then $e: F^{m \times \cdot} \to F^{m \times \cdot}$ defined as $$e(A)_{ij} = \begin{cases} A_{ij} & \text{if } i \neq r  \\
A_{rj} + cA_{sj}  & \text{if } i = r  \\
\end{cases}$$ is an [[Elementary Row Operation]] (known as a *row addition*).
3. Let $c \in F$ and $r, s \in [m]$. Then $e: F^{m \times \cdot} \to F^{m \times \cdot}$ defined as $$e(A)_{ij} = \begin{cases} A_{ij} & \text{if } i \neq r, i \neq s  \\
A_{sj}  & \text{if } i = r   \\
A_{rj}  & \text{if } i = s
\end{cases}$$ is an [[Elementary Row Operation]] (known as a *row swap*).

## Remarks
1. [[Matrix Representation of Elementary Row Operations]]
2. We represent the [[Set]] of [[Elementary Row Operation]]s on $F^{m \times \cdot}$ as $\text{Row}F^{m \times \cdot}$.
3. [[TODO]] this has some relationship to [[Group]]s. However, I can't really talk about [[Matrix Inverse]]s without setting up details on [[Vector Space Basis]]. I need some details about [[Matrix Equation System]]s to establish that.
