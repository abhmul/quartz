---

title: "Zero Subspace has Dimension 0"

---
# Statement
Let $V$ be a [[Vector Space]]. Then $\dim \{\mathbf{0}\} = 0$ for $\mathbf{0} \in V$.

## Proof
Recall that [[The Empty Set is Linearly Independent]] and 
$$\text{span} \emptyset  = \bigcap\limits\{W \subset V : S \subset W, W \text{ is a subspace of V}\} = \{\mathbf{0}\},$$since every [[Vector Subspace]] of $V$ is a superset of $\emptyset$ and $\{\mathbf{0}\}$ is a [[Vector Subspace]] of every [[Vector Subspace]] of $V$. Thus $\emptyset$ is a [[Vector Space Basis]] for $\{\mathbf{0}\}$ and $\dim \{\mathbf{0}\} = |\emptyset| = 0$. $\blacksquare$

# Other Outlinks
- [[Subspace Span]]