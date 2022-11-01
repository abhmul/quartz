---

title: "Stopping Time"

---
# Definition
Suppose $\{\mathcal{B}_{n} : n \in \mathbb{N} \}$ is a [[Discrete-Time Filtration]] on $\Omega$. Then a [[Function]] $\nu : \Omega \to \bar{\mathbb{N}}$ is a [[Stopping Time]] if
$$[\nu = n] \in \mathcal{B}_{n}, \forall n \in \mathbb{N}$$
## Remarks
1. [[Strategy Corresponding to a Stopping Time]]
2. $\nu$ can be $\infty$. In that case, $\nu$ represents the case that we never stop.
3. [[Equivalent Conditions for being a Stopping Time]]
4. [[Stopping Times are Measureable with respect to the Borel Sigma Algebra on the Order Topology of the Extended Naturals]]

### Deciding not to stop
Observe that
$$[\nu = \infty] = \bigcap\limits_{n \in \mathbb{N}} [\nu \neq n]^{C} = \left(\bigcup\limits_{n \in \mathbb{N}} [\nu = n]\right)^{C} \in \mathcal{B}_\infty$$
since $[\nu = n] \in \mathcal{B}_{n} \subset \mathcal{B}_\infty$ $\forall n \in \mathbb{N}$. Thus, our defining property can be extended to $\bar{\mathbb{N}}$.

## Properties
1. [[Constant Function is a Stopping Time]]
2. [[Equivalent Conditions for being a Stopping Time]]
3. [[Extrema of Stopping Times are Stopping Times]]
4. [[Limits of Monotone Sequences of Stopping Times are Stopping Times]]
5. [[Sums of Stopping Times are Stopping Times]]

# Definition 2
[[TODO]] - this could probably be reworked for general [[Stopping Time]]s by allowing the [[Function Image|image]] of the stopping time to be a [[Total Ordering]], then applying [[Compactification]] on the [[Order Topology]]. For now, I'll leave as a discrete construct. If need be, I can change the name of this to "Discrete Stopping Time" then rewire the dependent pages.

# Other Outlinks
- [[Natural Numbers]]
- [[Extended Natural Numbers]]
