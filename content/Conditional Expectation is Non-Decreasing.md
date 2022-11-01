---

title: "Conditional Expectation is Non-Decreasing"

---
# Statement
Let $(\Omega, \mathcal{G}, \mathbb{P})$ be a [[Probability Space]] and let $\mathcal{B} \subset \mathcal{G}$ be a sub-[[Sigma Algebra]] of $\mathcal{G}$. Suppose $X_{1}, X_{2} \in \mathcal{G}$ so that $X_{1} \leq X_{2}$. Then [[Almost Surely]]
$$\mathbb{E}(X_{1} | \mathcal{B}) \leq \mathbb{E}(X_{2} | \mathcal{B})$$
## Proof
Recall that [[A Measureable Function is less than or equal to another iff all its integrals are less than or equal to the others]]. Therefore, $\forall A \in \mathcal{B}$, by definition of [[Conditional Expectation with respect to Sigma Field]]:
$$\int\limits_{A} \mathbb{E}(X_{1} | \mathcal{B}) d \mathbb{P} = \int\limits_{A} X_{1} d \mathbb{P} \leq \int\limits_{A} X_{2} d \mathbb{P} = \int\limits_{A} \mathbb{E}(X_{2} | \mathcal{B}).$$
Then, again because [[A Measureable Function is less than or equal to another iff all its integrals are less than or equal to the others]], we have that
$$\mathbb{E}(X_{1} | \mathcal{B}) \leq \mathbb{E}(X_{2} | \mathcal{B})$$
[[Almost Surely]]. $\blacksquare$
