---

title: "Closure of Open Ball is a subset of Closed Ball"

---
# Definition
Let $(X, d)$ be a [[Metric Space]]. Let $x \in M$ and let $\epsilon > 0$. Then $\text{cl}B_{\epsilon}(x) \subset \overline{B_{\epsilon}(x)}$.

## Proof
Recall [[Closure of a Set in a Metric Space is all its Sequential Limits]], so $x \in \text{cl} B(X)$ [[If and Only If]] there exists $({x}_{n})_{n=1}^{\infty} \subset B(X)$ so that $x_{n} \to x'$. Then, because [[Metrics are Continuous]] and [[Components Converge iff Sequence Converges in Finite Product Metric Spaces]], $d(x_{n}, x) \to d(x', x)$. Since $d(x_{n}, x) < \epsilon$ for all $n \in \mathbb{N}$, we have that $d(x', x) \leq \epsilon$ because of the [[Order Limit Theorem]]. Thus $\text{cl} B_\epsilon(x) \subset \{x' \in X : d(x, x') \leq \epsilon\} =: \overline{B_\epsilon(x)}$. $\blacksquare$

## Remarks
1. [[The Closure of an Open Ball is not always the Closed Ball]].

# Other Outlinks
- [[Closed Ball]]
- [[Closure]]
- [[Open Ball]]