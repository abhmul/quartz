---

title: "Compact Spaces are Complete"

---
# Statement 1
Let $(K, \leq)$ be a [[Total Ordering]] equipped with the [[Order Topology]] that is [[Compact]]. Then it is a [[Complete Ordering]].

## Proof 1
Let $A \subset K$ be [[Nonempty]] and [[Upper Bound|bounded from above]]. Consider $A$ as a [[Order-Preserving Function|monotone]] [[Net]], $(a_{a})_{a \in A} = A$. Because $K$ is [[Compact]] and [[A Set is Compact iff all Nets have a Convergent Subnet]], we know there exists a [[Cofinal Subset]] $S \subset A$ so that $(b_{b})_{b \in S}$ is a [[Net Convergence|convergent]] [[Subnet]]. It is [[Order-Preserving Function|montone]] because its parent is. Because [[Order-Preserving Nets Converge to their Supremum]], we know $b_{b} \to \sup\limits_{b \in S} b_{b} = \sup\limits S$. Because [[Supremum of a Cofinal Subset is the Supremum of the Set]], it follows that $\sup\limits S = \sup\limits A$ and $\sup\limits A$ exists. $\blacksquare$

## Proof 2
We prove by [[Contraposition]]. Suppose there exists an $A \subset K$ [[Nonempty]] and [[Upper Bound|bounded from above]] so that $\sup\limits A$ does not exist. Then, letting $U = \{b \in X : b > a \text{ } \forall a \in A\}$,
$$\{(\leftarrow, a) : a \in A\} \cup U$$
forms a [[Set Cover]] of $K$. This follows because for $x \in K$, either there exists $a \in A$ so that $a > x$ or there does not. In the former case, $x \in (\leftarrow, a)$. In the latter case, $x$ is an [[Upper Bound]] of $A$, and since $\sup\limits A$ does not exist, we cannot have $x = a$ for any $a \in A$. Thus $x \in U$. $U$ is also [[Open]] since for any $b \in U$, there exists $c \in U$ so that $c < b$ and $(c, \rightarrow) \subset U$. The $c \in U$ exists because $b$ is an [[Upper Bound]] that is not a [[Supremum]]. Thus our [[Set Cover]] is an [[Open Cover]].

We claim that our [[Open Cover]] cannot be reduced to a [[Finite Set|finite]] [[Open Subcover]]. If it could, then we would have some $a_{1}, \dots, a_{n}$ (for some $n \in \mathbb{N}$) so that $\{(\leftarrow, a_{i}) : i \in [n]\} \cup U$ is an [[Open Cover]] of $K$. Since $A \cap U = \emptyset$, we must have $A \subset \bigcup\limits_{i = 1}^{n} (\leftarrow, a_{i}) = (\leftarrow, \max\limits_{i \in [n]} a_{i})$. But then $M = \max\limits(a_{1}, \dots, a_{n})$ is an [[Upper Bound]] of $A$ and $M \in A$ by construction. So $M = \sup\limits A$ $\unicode{x21af}$.

So we have that $K$ cannot be [[Compact]]. $\blacksquare$

# Other Outlinks
- [[Supremum]]
- [[Open Ray]]
- [[Natural Numbers]]