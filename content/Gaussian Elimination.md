---

title: "Gaussian Elimination"

---
# Statement
Let $F$ be a [[Field]] and let $m,n \in \mathbb{N}$. There exists an [[Algorithm]] that maps any $A \in F^{m \times n}$ to a [[Row Reduced Echelon Matrix]] only through the use of [[Elementary Row Operation]]s. This algorithm is known as [[Gaussian Elimination]].

## Proof
Consider the following [[Algorithm]]

> **Name**: *RREF*
> **Input**: $F$ [[Field]], $m, n \in \mathbb{N}$, $A \in F^{m \times n}$
> **Output**: $R \in F^{m \times n}$ so that $A \sim_{R} R$ and $R$ is a [[Row Reduced Echelon Matrix]].
> 1. Copy $A$ to $R$
> 3. For $i=1$ to $m$: `\\ create a row-reduced matrix`
> 	2. if $R_{i \cdot } = \mathbf{0}$:
> 		2. Continue;
> 	3. $j = \min\limits \{r \in [n] : R_{ir} \neq 0\}$;
> 	4. $R_{i \cdot}  \leftarrow R_{ij}^{-1} R_{i \cdot}$;
> 	7. For $i'=1$ to $m$:
> 		1. $R_{i' \cdot}  \leftarrow R_{i' \cdot} + (-R_{rj} R_{i \cdot})$;
> 3. $S  \leftarrow \{i \in [m] : R_{i \cdot} \neq \mathbf{0}\}$;
> 4. For $i \in S$:
> 	1. $k_{i}  \leftarrow \min\limits \{r \in [n] : R_{ir} \neq 0\}$;
> 5. $r = 1$;
> 6. While $S \neq \emptyset$:  `\\ Make it row-reduced echelon`
> 	1. $i  \leftarrow \text{argmin}\{k_{s} : s \in S \}$;
> 	2. Swap $R_{r \cdot}$ with $R_{i \cdot}$;
> 	3. $S  \leftarrow S \setminus \{i\}$;
> 	4. $r  \leftarrow r + 1$;
> 8. Return $R$;

To show this algorithm is correct we need to show
1. it terminates,
2. It only transforms $R$ by [[Elementary Row Operation]]s
3. It returns a [[Row Reduced Echelon Matrix]].

To that end:

### Algorithm terminates
[[TODO]]

### Algorithm only transforms $R$ by [[Elementary Row Operation]]s
[[TODO]]

### Algorithm returns a [[Row Reduced Echelon Matrix]]
[[TODO]]