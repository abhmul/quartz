---

title: "The Span of subset of a Span is also a subset of that Span"

---
# Statement
Let $V$ be a [[Vector Space]] and let $S, R \subset V$ so that $\text{span} R \supset S$. Then $\text{span} R \supset \text{span} S$.

## Proof
This follows because every [[Vector Subspace]] of $V$ containing $R$ also contains $S$. Therefore we have
$$\{W \subset V : S \subset W, W \text{ is a subspace of V}\} \supset \{W \subset V : R \subset W, W \text{ is a subspace of V}\}.$$
Then
$$\begin{align*}
\text{span} S &= \bigcap\limits\{W \subset V : S \subset W, W \text{ is a subspace of V}\}\\
&\subset \bigcap\limits\{W \subset V : R \subset W, W \text{ is a subspace of V}\} & \text{ (fewer sets in the intersection)}\\
&=\text{span} R
\end{align*}$$
establishing the result. $\blacksquare$

# Other Outlinks
- [[Subspace Span]]