---

title: "Regular Conditional Distribution"

---
# Definition
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]], $X: (\Omega, \mathcal{B}) \to (S, \mathcal{S})$ be a [[Random Element]], and $\mathcal{G} \subset \mathcal{B}$ be a [[Sub-Sigma Algebra]]. $\mu: \Omega \times \mathcal{S} \to [0,1]$ is a [[Regular Conditional Distribution]] for $X$ given $\mathcal{G}$ if
1. For each $A \in \mathcal{S}$, $\omega \mapsto \mu(\omega, A)$ is $\mathbb{E}(\mathbb{1}_{X \in A} | \mathcal{G})$ [[Almost Surely]]
2. $A \mapsto \mu(\omega, A)$ is a [[Probability Measure]] on $(S, \mathcal{S})$ for $\omega \in \Omega$ $\mathbb{P}$-[[Almost Surely]].

## Properties
1. [[If Space is a Standard Probability Space, then a Regular Conditional Distribution exists and is Almost Surely Unique]]
# Other Outlinks 
- [[Conditional Probability]]