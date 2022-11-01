---

title: "Every Open Subset of Locally Path-Connected Space is Locally Path-Connected"

---
# Statement
Let $X$ be a [[Topological Space]] that is [[Locally Path-Connected]]. Then if $U \subset X$ is [[Open]], it is [[Locally Path-Connected]].

## Proof
Since $X$ is [[Locally Path-Connected]], there exists a [[Topological Basis]] $\mathcal{B}$ for $X$ made up of [[Path-Connected]] subsets. Because $\mathcal{B}$ is a [[Topological Basis]], for each $U' \subset U$ [[Open]], there exist $\mathcal{B}_{U'}$ such that $\bigcup\limits_{B \in \mathcal{B}_{U'}}B = U'$.  Thus, taking $\bigcup\limits_{U' \subset U \text{ open}} \mathcal{B}_{U'}$ forms a [[Topological Basis]] for $U$. By construction, all elements of $\mathcal{B}_{U'}$ for each $U' \subset U$ [[Open]] are [[Path-Connected]], so $U$ is [[Locally Path-Connected]]. $\blacksquare$