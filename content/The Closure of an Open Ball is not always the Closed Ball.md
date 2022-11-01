---

title: "A Metric Space where the Closure of an Open Ball is not the Closed Ball"

---
# Counterexample
Consider $\mathbb{Z}$ equipped with the [[Discrete Metric]]. Then $\text{cl}B_{1}(0) \subsetneq \overline{B_{1}(0)}$.

## Proof
By definition of [[Open Ball]] and [[Closed Ball]]
$$B_{1}(0) = \{x \in \mathbb{Z} : d(0,x) < 1\} = \{0\}$$
and 
$$\overline{B_{1}(0)} = \{x \in \mathbb{Z} : d(0,x) \leq 1\} = \mathbb{Z}.$$
But since the [[Discrete Metric induces the Discrete Topology]], we know $B_{1}(0)$ is also [[Closed]]. Therefore $\text{cl}B_{1}(0) = B_{1}(0) \subsetneq \overline{B_{1}(0)}$. $\blacksquare$