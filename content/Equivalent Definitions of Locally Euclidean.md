---

title: "Equivalent Definitions of Locally Euclidean"

---
# Statement
Let $M$ be a [[Topological Space]]. Then [[The following are Equivalent]]:
1. $M$ is [[Locally Euclidean]] of dimension $n$
2. For each $p \in M$, there exists a [[Coordinate Chart]] containing $p$ to $\mathbb{R}^{n}$
3. For each $p \in M$, there exists a [[Coordinate Chart]] containing $p$ to $B(\mathbb{R}^{n})$

## Proof
$(2) \Rightarrow (1)$: Since $\mathbb{R}^{n}$ is [[Open]] (by definition of a [[Topological Space]]), we have for each $p \in M$ an [[Open]] $U \ni p$ and [[Open]] $\hat{U} = \mathbb{R}^{n}$ that is [[Homeomorphism|homeomorphic]] to $U$. Thus $M$ is [[Locally Euclidean]] of dimension $n$. $\checkmark$

$(3) \Rightarrow (2)$: This follows because [[The Euclidean Open Unit Ball is Homeomorphic to the Euclidean Space]]. $\checkmark$

$(1) \Rightarrow (3)$: Let $p \in M$ and let $(U, \varphi)$ be a [[Coordinate Chart]] for $p$ to $\hat{U} \subset \mathbb{R}^{n}$. Such a [[Coordinate Chart]] exists because $M$ is [[Locally Euclidean]]. Let $\hat{p} := \varphi_{p}(p)$. Since $\hat{U} := \varphi_{p}(U_{p})$ is [[Open]] in $\mathbb{R}^{n}$, by definition of the [[Metric Topology]], there exists some radius $\epsilon > 0$ so $B_{\epsilon}(\hat{p}) \subset \hat{U}$. Since $\varphi_{p}$ is a [[Continuous Function]] (by definition of [[Homeomorphism]]), $B := \varphi_{p}^{-1}(B_{\epsilon}(\hat{p})) \subset M$ is [[Open]] and contains $p$. Thus, after noting that [[The Restriction of Homeomorphism is a Homeomorphism in the Subspace Topology]] we can construct [[Coordinate Chart]] $(B, \varphi_{p} {\big|}_{B})$ containing $p \in M$. Every [[Open Ball is Homeomorphic to the Open Unit Ball in the Euclidean Space]], so we can create a [[Coordinate Chart]] containing $p$ to the [[Open Unit Ball]] by [[Function Composition]]. Since $p \in M$ was arbitrary, we have established $(3)$. 
 $\checkmark$ $\blacksquare$

# Other Outlinks
- [[Euclidean Space]]
- [[Open Unit Ball]]