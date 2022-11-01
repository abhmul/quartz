---

title: "Path-Components Partition the Space"

---
# Statement
Suppose $X$ is a [[Topological Space]]. Then the [[Set|collection]] 
$$\mathcal{P} := \{P \subset X : P \text{ is a nonempty path-connected component}\}$$ is a [[Partition]] of $X$.

## Proof
We must show 
1. $\emptyset \not\in \mathcal{P}$
2. $P \cap P' \neq \emptyset \Rightarrow P = P'$ for $P, P' \in \mathcal{P}$
3. $\bigcup\limits_{P \in \mathcal{P}} P = X$

(1) follows from our construction of $\mathcal{P}$. For (2), note that if $P \cap P' \neq \emptyset$, then by [[If Path-Connected Sets share a point, then their Union is Path-Connected]], $P \cup P'$ is [[Path-Connected]]. $P \cup P' \supset P, P'$ so $P = P \cup P' = P'$ because both $P$ and $P'$ are [[Path-Connected Component]]s.

For (3), let $x \in X$ be arbitrary. Then consider $\mathcal{P}_{x} = \{D \subset X : x \in D, D \text{ is path-connected}\}$. By [[If Path-Connected Sets share a point, then their Union is Path-Connected]], $P_{x} := \bigcup\limits_{D \in \mathcal{P}_{x}} D$ is [[Path-Connected]]. If there were some [[Path-Connected]] $E \supset P_{x}$, then $x \in E$ so $E \in \mathcal{P}_{x}$ making $E \subset P_{x}$, so $E = P_{x}$. Thus $P_{x}$ is a [[Path-Connected Component]] containing $x \in X$. Thus taking $\bigcup\limits_{x \in X} P_{x} = X$ shows (3) and completes the proof $\blacksquare$.