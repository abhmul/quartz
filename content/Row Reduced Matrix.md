---

title: "Row Reduced Matrix"

---
# Definition
Let $F$ be a [[Field]] and let $m, n \in \mathbb{N}$. Then we say $R \in F^{m \times n}$ is a [[Row Reduced Matrix]] if
1. $\forall i \in [m]$, the leading nonzero entry of $R_{i \cdot}$ is $1$. That is, for $j = \min\limits\{j' \in [n] : R_{ij'} \neq 0\}$, $R_{ij} = 1$. This is vacuously true if $\{j' \in [n] : R_{ij'} \neq 0\} = \emptyset$.
2. $\forall j \in [n]$, if $R_{\cdot j}$ contains the leading nonzero entry of some row, then all other entries of $R_{\cdot j} = 0$. This is, if $\exists i \in [m]$ so that $j =  \min\limits\{j' \in [n] : R_{ij'} \neq 0\}$, then $R_{kj} = 0$ $\forall k \neq i$.

## Examples
1. The [[Identity Matrix]] 
	$$I_{ij} = \delta_{ij} = \begin{cases} 1  & \text{if } i = 1 \\
 0  & \text{otherwise}\end{cases}$$
2.  $$\begin{pmatrix}1 & 0 &  1 \\ 0 & 1 & 2 \end{pmatrix}$$
3. $$\begin{pmatrix}0 & 0 & 1 & 3  \\ 0  & 0 & 0 & 0  \\ 1 & 3 &  0 & 2 \end{pmatrix}$$
## Nonexamples
1. $$\begin{pmatrix} 1  & -1 & 0 \\ 0  & 1  & 0\end{pmatrix}$$
	This matrix violates the 2nd defining property on column 2.
2. $$\begin{pmatrix} 1  & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2\end{pmatrix}$$
	This matrix violates the 1st defining property on row 3.