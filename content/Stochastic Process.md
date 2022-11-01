---

title: "Stochastic Process"

---
# Definition
Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a [[Probability Space]], let $(T, \leq)$ be a [[Total Ordering]], and let $(S, \Sigma)$ be a [[Measure Space]]. Then a [[Random Element]] $X : \Omega, \mathcal{A} \to S^{T}, \Sigma^{T}$, where $S^{T}$ is endowed with the [[Product Sigma Algebra]], is a [[Stochastic Process]].

## Remarks
1. A [[Stochastic Process]] can alternatively be written as a collection of [[Random Element]]s [[Index Set|indexed]] by $T$, $\{X_{t}: \Omega \to S\}_{t \in T}$. These two definitions are equivalent because [[A Function into the the Product Sigma Algebra is Measureable iff its components are Measureable]].
2. When referencing a [[Stochastic Process]], we often do not write the additional pieces of the definition and take them to have the desired properties granted by the definition implicitly
3. One might wonder what other options do we have for $T$ besides an [[Order Embedding]] into $\mathbb{R}$ or $\mathbb{Q}$, and what would such a [[Stochastic Process]] look like. Take a look at [[Total Orderings that cannot be Order Embedded into the Reals]]. An interesting [[Stochastic Process]] would be the one indexed by the [[Hyperreal Numbers]]. We could then talk about [[Infinitesmal]] increments in the [[Stochastic Process]].