---

title: "Row Reduced Echelon Matrix"

---
# Definition 1
Let $F$ be a [[Field]] and let $m, n \in \mathbb{N}$. Then $R \in F^{m \times n}$ is a [[Row Reduced Echelon Matrix]] if 
1. $R$ is a [[Row Reduced Matrix]],
2. If $R_{i \cdot} = \mathbf{0}$ for $i \in [m]$, then $\not\exists k  > i$ so that $R_{k \cdot} \neq \mathbf{0}$.
3. Let $r = \max\limits \{i \in [m] : R_{i \cdot} \neq \mathbf{0}\}$. Then for $k_{i} = \min\limits\{j \in [n] : R_{ij} \neq 0\}$, we have that $k_{1} < \cdots < k_{r}$.

 ## Examples
 1. The [[Identity Matrix]].
 2. $$\begin{pmatrix}1 & 0 &  1 \\ 0 & 1 & 2 \end{pmatrix}$$
 3. $$\begin{pmatrix}1 & 3 &  0 & 2 \\ 0 & 0 & 1 & 3 \\ 0  & 0 & 0 & 0 \end{pmatrix}$$

## Nonexamples
1. $$\begin{pmatrix}0 & 0 & 1 & 3  \\ 0  & 0 & 0 & 0  \\ 1 & 3 &  0 & 2 \end{pmatrix}$$
	This is a [[Row Reduced Matrix]], but it violates (2) at row 2 and (3) between row 1 and row 3




# Other Outlinks
- [[Natural Numbers]]
- [[Matrix]]
- [[Set]]