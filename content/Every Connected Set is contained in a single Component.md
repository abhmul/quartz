---

title: "Every Connected Set is contained in a single Component"

---
# Statement
Suppose $X$ is a [[Topological Space]] and $S \subset X$ is [[Connected]]. Then there exists a [[Connected Component]] $C \subset X$ s.t. $S \subset C$. If $S$ is [[Nonempty]], this [[Connected Component]] is unique.

## Proof
If $X = \emptyset$, then $\emptyset$ is a [[Connected Component]], and $S \subset X \subset \emptyset$.

Otherwise recall that [[Connected Components Partition the Space]], so let $\mathcal{C}$ be that [[Partition]] of $X$. Since $X$ is [[Nonempty]], $\mathcal{C}$ is [[Nonempty]]. If $S = \emptyset$ then any $C \in \mathcal{C}$ will do. Otherwise, suppose $S \neq \emptyset$. Then $\exists x \in S$. Since $\mathcal{C}$ is a [[Partition]], there exists unique $C_{x} \in \mathcal{C}$ so that $x \in C_{x}$. We claim $S \subset C_{x}$. Otherwise if $S \not\subset C_{x}$, because $x \in S \cap C_{x}$, $S \cup C_{x} \supsetneq C_{x}$ is [[Connected]] by [[If Connected Sets share a point, then their Union is Connected]] and $C_{x}$ is not [[Maximal]] $\unicode{x21af}$. So, by [[Proof by Contradiction|contradiction]], $S \subset C_{x}$. As noted above $C_{x}$ is the unique element of $\mathcal{C}$ containing $x$. So because $x \in S$, any other $C \in \mathcal{C}$ s.t. $S \subset C$ must also contain $x$, and must therefore be $C_{x}$. $\blacksquare$