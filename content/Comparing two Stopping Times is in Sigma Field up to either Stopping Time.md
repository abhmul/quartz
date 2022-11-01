---

title: "Comparing two Stopping Times is in Sigma Field up to either Stopping Time"

---
# Statement
Let $\mathcal{F} = \{\mathcal{B}_{n} : n \in \mathbb{N}\}$ be a [[Discrete-Time Filtration]] over $\Omega$ and let $\nu, \nu' : \Omega \to \bar{\mathbb{N}}$ be [[Stopping Time]]s on $\mathcal{F}$. Then the following statements hold
1. $[\nu < \nu'] \in \mathcal{B}_{\nu}\cap  \mathcal{B}_{\nu'}$
2. $[\nu = \nu'] \in \mathcal{B}_{\nu}\cap  \mathcal{B}_{\nu'}$
3. $[\nu \leq \nu'] \in \mathcal{B}_{\nu}\cap  \mathcal{B}_{\nu'}$

## Proof
We show the following sequence of results
1. $[\nu < \nu'] \in \mathcal{B}_{\nu}$
2. $[\nu = \nu'] \in \mathcal{B}_\nu$

Then we have the following implications
1. $[\nu \leq \nu'] \in \mathcal{B}_{\nu}$ since $[\nu < \nu'] \cup [\nu = \nu'] = [\nu \leq \nu']$ and $\mathcal{B}_\nu$ is a [[Sigma Algebra]].
2. $[\nu < \nu'] = [\nu \geq \nu']^{C} = [\nu' \leq \nu]^{C} \in \mathcal{B}_{\nu'}$ since $[\nu' \leq \nu] \in \mathcal{B}_{\nu'}$ by implication (1) and $\mathcal{B}_{\nu'}$ is a [[Sigma Algebra]]. This establishes statement (1). $\checkmark$
3. $[\nu = \nu'] = \mathcal{B}_{\nu'}$ by symmetry and result (2). This establishes statement (2). $\checkmark$
4. $[\nu \leq \nu'] \in \mathcal{B}_{\nu'}$ since $[\nu \leq \nu'] = [\nu' < \nu]^{C} \in \mathcal{B}_{\nu'}$ by statement (1) and because $\mathcal{B}_{\nu'}$ is a [[Sigma Algebra]]. This establishes statement (3). $\checkmark$

Now to establish results (1) and (2). Observe that for $n \in \mathbb{N}$
$$[\nu < \nu'] \cap [\nu = n] = [n < \nu'] \in \mathcal{B}_{n}$$ by condition (3) in [[Equivalent Conditions for being a Stopping Time]]. Thus $[\nu < \nu'] \in \mathcal{B}_{\nu}$. $\checkmark$

Next, observe that for $n \in \mathbb{N}$
$$[\nu = \nu'] \cap [\nu = n] = [n = \nu'] \in \mathcal{B}_{n}$$
by definition of a [[Stopping Time]]. Thus $[\nu = \nu'] \in \mathcal{B}_{\nu}$. $\checkmark$.

This completes the proof. $\blacksquare$

# Other Outlinks
- [[Natural Numbers]]
- [[Extended Natural Numbers]]