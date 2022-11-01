---

title: "Constant Function is a Stopping Time"

---
# Statement
Let $\mathcal{F} = \{\mathcal{B}_{n} : n \in \mathbb{N}\}$ be a [[Discrete-Time Filtration]] over $\Omega$, $k \in \bar{\mathbb{N}}$, and let $\nu : \Omega \to \bar{\mathbb{N}}$ be defined as $\nu(\omega) = k$ for all $\omega \in \Omega$. Then $\nu$ is a [[Stopping Time]].

## Proof
We simply verify the definition of a [[Stopping Time]]. Let $n \in \mathbb{N}$. Observe that $$[\nu = n] = \begin{cases} \emptyset &\text{if }n \neq k\\ \Omega &\text{otherwise}\end{cases}$$
All [[Sigma Algebra]]s on $\Omega$ contain $\Omega$ and $\emptyset$ (by definition), so certainly $[\nu = n] \in \mathcal{B}_{n}$. $\blacksquare$