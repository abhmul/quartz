---

title: "Continuous Open Maps transfer Bases"

---
# Statement
Let $X, Y$ be [[Topological Space]]s and let $X$ have [[Topological Basis]] $\mathcal{B}$. Suppose there exists [[Continuous Function|continuous]] [[Open Map]] $F:X \to Y$. Then $F(\mathcal{B}) := \{F(B) \subset Y : B \in \mathcal{B}\}$ is a [[Topological Basis]] for $Y$.

## Proof
First note $F(\mathcal{B})$ is a [[Set|collection]] of [[Open]] sets because $F$ is an [[Open Map]]. Let $U \subset Y$ be [[Open]]. Because $F$ is [[Continuous Function|continuous]], $F^{-1}(U)$ is [[Open]]. Thus there exists $\mathcal{B}_{U} \subset \mathcal{B}$ so that $\bigcup\limits_{B \in \mathcal{B}_{U}}B = F^{-1}(U)$. Then $\bigcup\limits_{B \in \mathcal{B}_{U}}F(B) = U$. Since $U$ was arbitrary, $F(\mathcal{B})$ is a [[Topological Basis]] for $Y$. $\blacksquare$