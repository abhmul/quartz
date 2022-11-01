---

title: "Correspondence of Partition Sets means Partitions are the same"

---
# Statement
Let $X$ be a [[Set]] and let $\mathcal{P}, \mathcal{R}$ be two [[Partition]]s of $X$. If for each $P \in \mathcal{P}$ there exists $R \in \mathcal{R}$ s.t. $P = R$, then $\mathcal{P} = \mathcal{R}$.

## Proof
First note that $\mathcal{P} \subset \mathcal{R}$. To see this, observe that for each $P \in \mathcal{P}$, we can find $R \in \mathcal{R}$ so $P = R$. Therefore $P \in \mathcal{R}$.

Next, to see $\mathcal{R} \subset \mathcal{P}$, Suppose $R \in \mathcal{R}$. Becuase $\mathcal{P}$ is a [[Partition]], there exists $P \in \mathcal{P}$ so that $P \cap R \neq \emptyset$. Now this $P$ has some $R' \in \mathcal{R}$ so that $P = R'$.  But then $$R' \cap R = P \cap R \neq \emptyset,$$ so by definition of a [[Partition]], $R' = R$. Therefore $P = R$. Thus, $R \in \mathcal{P}$. $\blacksquare$