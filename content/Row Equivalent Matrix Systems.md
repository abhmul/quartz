---

title: "Row Equivalent Matrix Systems"

---
# Definition
Let $F$ be a [[Field]]. Let $m, n \in  \mathbb{N}$, let $A, B \in F^{m \times n}$, and let $\mathbf{b}, \mathbf{c} \in F^{m \times 1}$. Then we say the [[Matrix Equation System]]s
$$\begin{align*}
A \mathbf{x} &= \mathbf{b} \tag{1} \\
B \mathbf{x} &= \mathbf{c} \tag{2}
\end{align*}$$are [[Row Equivalent Matrix Systems]] if 
$$\begin{pmatrix}A &\Big| &\mathbf{b}\end{pmatrix} \sim_{R} \begin{pmatrix}B &\Big| &\mathbf{c}\end{pmatrix}$$
where $(A| \mathbf{b}) \in F^{m \times n+1}$ represents the columnwise concatenation of $A$ and $\mathbf{b}$.

# Other Outlinks
- [[Row Equivalent Matrices]]