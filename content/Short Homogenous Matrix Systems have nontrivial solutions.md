---

title: "Short Homogenous Matrix Systems have nontrivial solutions"

---
# Statement
Let $F$ be a [[Field]] and let $m < n \in \mathbb{N}$. Suppose $A \in F^{m \times n}$ defines the [[Homogenous Linear System|homogenous]] [[Matrix Equation System]]
$$A \mathbf{x} = \mathbf{0}$$
Then there exists $\mathbf{x} \neq \mathbf{0}$ in the [[Solution Set]].

## Proof
Let $R$ be a [[Every Matrix is Row Equivalent to a Row Reduced Echelon Matrix|row equivalent RREF matrix]]. Let $S = \{j \in [n] : R_{\cdot j} \text{ contains no leading nonzero entry}\}$. Since $m < n$, $S \neq \emptyset$. Let $\mathbf{x}_{j} = 1$ $\forall j \in S$ . For all $i \not\in S$, there must be some row $r \in [m]$ of $R$ that has a leading $1$ at $R_{ri}$. Set $\mathbf{x}_{i} = -\sum\limits_{j \in S} R_{rj}$. Then observe that for each row $r \in [m]$ either
1. $R_{r \cdot} = \mathbf{0}$, in which case $R_{r \cdot} \mathbf{x} = 0$.
2. $R_{r \cdot} \neq \mathbf{0}$, in which case it has a leading $1$. Since the only nonzero entries of $R_{r \cdot}$ can be $j \in S$, we must have that $R_{r \cdot} \mathbf{x} = 0$ by construction of $\mathbf{x}$.

Therefore $R \mathbf{x} = \mathbf{0}$. Since [[Row Equivalent Homogenous Matrix Systems have the same Solution Set]], we must have that $A \mathbf{x} = \mathbf{0}$ as well. $\blacksquare$

# Other Outlinks
- [[A Linear Equation System is Homogenous iff its constants are 0]]
- [[Matrix Equation Systems are Linear Systems]]