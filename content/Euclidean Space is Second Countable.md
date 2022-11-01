---

title: "Euclidean Space is Second Countable"

---
# Statement
The [[Euclidean Space]] $\mathbb{R}^{n}$ (for $n \in \mathbb{N}$) is a [[Second Countable]] [[Topological Space]].

## Proof
Consider the collection
$$\mathcal{B} := \{B_{\delta}(x) : \delta \in \mathbb{Q}, x \in \mathbb{Q}^{n}\}$$
It is [[Countable]] ([[A Union of Countable Sets is Countable]], [[Rationals are Countable]], and [[Finite Products of Countable Sets dare Countable]]). It is a [[Set|collection]] of [[Open]] sets by definition of [[Metric Topology]].  Let $U \subset \mathbb{R}^{n}$ be [[Open]]. Consider $V := \bigcup\limits_{B \in \mathcal{B}, B \subset U} B$. By construction, $V \subset U$. We will show $V \supset U$. Let $x \in U$. By definition of [[Metric Topology]], there exists a $\delta \in \mathbb{R}_{>0}$ so that $B_{\delta}(x) \subset U$. Because the [[Rationals are Dense in the Reals]], there exists a $\delta' \in \mathbb{Q} \cap (0, \delta)$ (i.e. $0 < \delta' \leq \delta$). Again, because the [[Rationals are Dense in the Reals]], there exists an $x' \in \mathbb{Q}^{n} \cap B_{\delta'}(x)$. Therefore, $x \in B_{\delta'}(x') \subset V$. Since $x \in U$ was arbitrary, we have $V \supset U$.

Therefore $\mathcal{B}$ is a [[Topological Basis]] for $\mathbb{R}^{n}$, so $\mathbb{R}^{n}$ is [[Second Countable]]. $\blacksquare$

# Other Outlinks
- [[Real Numbers]]
- [[Rational Numbers]]
- [[Set Union]]
- 