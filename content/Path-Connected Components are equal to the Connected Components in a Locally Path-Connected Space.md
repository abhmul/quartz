---

title: "Path-Connected Components are equal to the Connected Components in a Locally Path-Connected Space"

---
# Statement
Let $X$ be a [[Topological Space]] that is [[Locally Path-Connected]]. Then the [[Set|collection]] $\mathcal{P} := \{P \subset X : P \text{ is a path-component of }X\}$ is equal to $\mathcal{C} := \{C \subset X : C \text{ is a connected component of }X\}$.

## Proof
If $X = \emptyset$, then $\mathcal{P} = \emptyset = \mathcal{C}$.

Otherwise, assume $X$ is [[Nonempty]]. We claim that for each $C \in \mathcal{C}$ there exists $P \in \mathcal{P}$ s.t. $C = P$. Then by [[Correspondence of Partition Sets means Partitions are the same]], we have that $\mathcal{P} = \mathcal{C}$.

To verify the claim, let $C \in \mathcal{C}$. Because  [[Path-Connected Components Partition the Space]], for each $x \in C$, there is a $P_{x} \in \mathcal{P}$ so that $x \in P_{x}$.  Because [[Path-Connected implies Connected]], [[Every Connected Set is contained in a single Component]], and [[Connected Components Partition the Space]] we know $P_{x} \subset C$ for all $x \in C$. 

Pick some $y \in C$. Because [[Path-Connected implies Connected]], [[Every Connected Set is contained in a single Component]], and [[Connected Components Partition the Space]] we know $P_{y} \subset C$. Denote $R := \bigcup\limits_{P \in \mathcal{P} \setminus \{P_{y}\}} P$. $R = P_{y} ^{C}$ because [[Path-Connected Components Partition the Space]]. Since [[Path-Connected Components of Locally Path-Connected Spaces are Open]], both $R$ and $P_{y}$ are [[Open]]. Thus $R$ and $P_{y}$ [[Connected|disconnect]]  $C$. Since $C$ is [[Connected]],  and because $C \cap P_{y} \neq \emptyset$. we have that $P_{y} \subset C$. Therefore, $P_{y} = C$. $\blacksquare$