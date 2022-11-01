---

title: "Connected Components Partition the Space"

---
# Statement
Suppose $X$ is a [[Topological Space]]. Then the [[Set|collection]] 
$$\mathcal{C} := \{C \subset X : C \text{ is a nonempty connected component}\}$$ is a [[Partition]] of $X$.

## Proof
We must show 
1. $\emptyset \not\in \mathcal{C}$
2. $C \cap C' \neq \emptyset \Rightarrow C = C'$ for $C, C' \in \mathcal{C}$
3. $\bigcup\limits_{C \in \mathcal{C}} C = X$

(1) follows from our construction of $\mathcal{C}$. For (2), note that if $C \cap C' \neq \emptyset$, then by [[If Connected Sets share a point, then their Union is Connected]], $C \cup C'$ is [[Connected]]. $C \cup C' \supset C, C'$ so $C = C \cup C' = C'$ because both $C$ and $C'$ are [[Connected Component]]s.

For (3), let $x \in X$ be arbitrary. Then consider $\mathcal{C}_{x} = \{D \subset X : x \in D, D \text{ is connected}\}$. By [[If Connected Sets share a point, then their Union is Connected]], $C_{x} := \bigcup\limits_{D \in \mathcal{C}_{x}} D$ is [[Connected]]. If there were some [[Connected]] $E \supset C_{x}$, then $x \in E$ so $E \in \mathcal{C}_{x}$ making $E \subset C_{x}$, so $E = C_{x}$. Thus $C_{x}$ is a [[Connected Component]] containing $x \in X$. Thus taking $\bigcup\limits_{x \in X} C_{x} = X$ shows (3) and completes the proof $\blacksquare$.