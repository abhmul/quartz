---

title: "Slices of a Continuous Function are Continuous"

---
# Statement
Let $X,Y,Z$ be [[Topological Space]]s and suppose $F: X \times Y \to Z$ is a [[Continuous Function]]. Then $F_{x}$, is a [[Continuous Function]].

## Proof
Suppose $V \subset Z$ is [[Open]]. Then 
$$\begin{align*}
&y \in F_{x}^{-1}(V)\\
\Leftrightarrow& F(x, y) \in V\\
\Leftrightarrow&(x,y) \in F^{-1}(V)\\
\Leftrightarrow&(x,y) \in F^{-1}(V) \cap (\{x\} \times Y).\\
\Leftrightarrow&y \in \pi_{2}(F^{-1}(V) \cap (\{x\} \times Y)),
\end{align*}$$
so $F^{-1}_{x}(V) = \pi_{2}(F^{-1}(V) \cap (\{x\} \times Y))$. Since $F^{-1}(V)$ is [[Open]] in $X \times Y$ and [[Product of Finitely Many Proper Open Sets form a Basis for the Product Topology]], we know 
$$F^{-1}(V) = \bigcup\limits_{i \in I} U_{X,i} \times U_{Y,i}.$$
for [[Open]] sets $U_{X,i} \subset X$ and $U_{Y, i} \subset Y$ for $i \in I$. Then
$$\pi_{2}(F^{-1}(V) \cap (\{x\} \times Y)) = \pi_{2} ( \bigcup\limits_{i \in I} (U_{X,i} \times U_{Y,i} \cap \{x\} \times Y) = \pi_{2} ( \bigcup\limits_{i \in I} \{x\} \times U_{Y,i}) = \bigcup\limits_{i \in I} U_{Y,i},$$
which is [[Open]] in $Y$. $\blacksquare$

# Other Outlinks
- [[Function Slice]]
- [[Function Image]]
- [[Function Preimage]]
