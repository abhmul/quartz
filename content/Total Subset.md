---

title: "Total Subset"

---
# Definition
Let $(X, ||\cdot||)$ be a [[Normed Vector Space]]. We say $A \subset X$ is a [[Total Subset]] if $\text{cl}(\text{span}A) = X$. That is, $\text{span} A$ is [[Dense]] in $X$.

## Remarks
1. Since [[The Subspace Span is the Set of all Linear Combinations]], this means we can get arbitrarily close to any $x \in X$ using some [[Linear Combination]] from $A$. Equivalent conditions [[Dense|density on metric spaces]] shows that this is equivalent to $\text{span}A$ being [[Dense]], making $A$ a [[Total Subset]].
2. Extending (1), we can get a [[Sequence]] $({x}_{n})_{n=1}^{\infty} \subset \text{span}A$ so that $||x_{n} - x|| \to 0$. Then, we can take the [[Telescoping Sum]] $$x_{1} = \sum\limits_{n=2}^{\infty} x_{n} - x_{n-1} = x.$$since each $x_{n} \in \text{span}A$ for $n \in \mathbb{N}$, we can break it into a ([[Finite Set|finite]]) [[Linear Combination]] of elements from $A$. Together, this means we can write $x$ as an [[Infinite Linear Combination]] of elements from $A$. We can go the other direction by noting each [[Finite Set|finite]] [[Linear Combination]] from our [[Infinite Linear Combination]] is in $\text{span}A$. This means for each $x \in X$, we have a [[Sequence]] in $\text{span}A$ that [[Sequence Convergence|converges]] to $x$. Thus, by equivalent conditions on [[Dense|density on metric spaces]], $\text{span}A$ is [[Dense]] and $A$ is a [[Total Subset]].