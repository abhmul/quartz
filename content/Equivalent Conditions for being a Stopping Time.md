---

title: "Equivalent Conditions for being a Stopping Time"

---
# Statement
Suppose $\{\mathcal{B}_{n} : n \in \mathbb{N} \}$ is a [[Discrete-Time Filtration]] on $\Omega$. Let $\nu : \Omega \to \bar{\mathbb{N}}$. [[The following are Equivalent]]:
1.  $\nu$ is a [[Stopping Time]]. 
2. $[\nu \leq n] \in \mathcal{B}_{n}, \forall n \in \mathbb{N}$
3. $[\nu > n] \in \mathcal{B}_{n}, \forall n \in \mathbb{N}$

## Proof
$(1) \Rightarrow (2)$: We have for $n \in \mathbb{N}$ 
$$[\nu \leq n] = \bigcup\limits_{m \leq n}[\nu =m] \in \mathcal{B}_{n}$$
since $[\nu = m] \in \mathcal{B}_{m} \subset \mathcal{B}_{n}$ $\forall m \leq n$. $\checkmark$

$(2) \Rightarrow (3)$: Let $n \in \mathbb{N}$. Since $[\nu \leq n] \in \mathcal{B}_{n}$, we know by definition of [[Sigma Algebra]] that $[\nu > n] = [\nu \leq n]^{C} \in \mathcal{B}_{n}$. $\checkmark$

$(3) \Rightarrow (1)$: Let $n \in \mathbb{N}$. Since $[\nu > n] \in \mathcal{B}_{n}$ and because $\mathcal{B}_{n}$ forms a [[Filtration]], we have that
$$[\nu = n] =  [\nu > n-1] \cap ([\nu > n])^{C} \in \mathcal{B}_{n},$$
where $[\nu > 0] = \Omega$. $\checkmark$

$\blacksquare$

## Remarks
1. Condition (3) is the same as saying $[\nu \geq n+1] \in \mathcal{B}_{n}$ $\forall n \in \mathbb{N}$.

# Encounters
1. [[Resnick - A Probability Path]] Sect 10.7 pg 365
2. [[Durret - Probability Theory and Examples]] pg 220 Sect 4.2
# Other Outlinks
- [[Function]]