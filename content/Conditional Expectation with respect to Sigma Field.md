---

title: "Conditional Expectation with respect to Sigma Field"

---
# Definition
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $X$ be a [[Random Variable]] in $L^{1}(\mathcal{B})$. Let $\mathcal{G} \subset \mathcal{B}$ be a [[Sub-Sigma Algebra]]. Then the [[Conditional Expectation]] of $X$ (denoted $\mathbb{E}[X | \mathcal{G}]$) with respect to $\mathcal{G}$ is a  [[Random Variable]] such that
1. $\mathbb{E}[X|\mathcal{G}] \in \mathcal{G}$
2. $\forall A \in \mathcal{G}$, $$\int\limits_{A} \mathbb{E}[X|\mathcal{G}] d \mathbb{P}(\omega) = \int\limits_{A} X d \mathbb{P}(\omega).$$
## Properties
1. [[Conditional Expectation Exists and is Almost Surely Unique]]
2. [[TODO]]