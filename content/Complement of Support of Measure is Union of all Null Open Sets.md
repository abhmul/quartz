---

title: "Complement of Support of Measure is Union of all Null Open Sets"

---
# Statement
Let $(X, \mathcal{B}(X), \mu)$ be a [[Borel Measure Space]] with [[Borel Measure]] $\mu$. Then
$$\text{supp} (\mu)^{C} = \{U \subset X : U \text{ is open}, \mu(U) = 0\}$$

## Proof
Denote $\mathcal{N}_{x} := \{U \subset X : U \text{ is a neighborhood of }x \in X\}$ . By definition of [[Support of a Measure]], we know that
$$\text{supp}(\mu) = \{x \in X : \forall U \in \mathcal{N}_{x}, \mu(U) > 0\}.$$
Then
$$\begin{align*}
\text{supp}(\mu)^{C} &= \{x \in X : \exists U \in \mathcal{N}_{x}, \mu(U) = 0\}\\
&\subset \bigcup\limits \{U \subset X : U \text{ is open}, \mu(U) = 0\}\\
&= \{x \in X : U \text{ is open}, \mu(U) = 0, x \in U\}\\
&= \{x \in X : U \in \mathcal{N}_{x}, \mu(U) = 0\}\\
&\subset \{x \in X : \exists U \in \mathcal{N}_{x}, \mu(U) = 0\}\\
&= \text{supp}(\mu)^{C},
\end{align*}$$
so
$$\text{supp} (\mu)^{C} = \{U \subset X : U \text{ is open}, \mu(U) = 0\}.$$
$\blacksquare$

## Remarks
1. This gives an alternate definition for [[Support of a Measure]]
# Other Outlinks
- [[Neighborhood of a Point]]
