---

title: "Continuous Functions Preserve Compactness"

---
# Statement
Let $K, Y$ be [[Topological Space]]s and suppose $K$ is [[Compact]]. Let $f: K \to Y$ be a [[Continuous Function]]. Then $f(K)$ is [[Compact]].

## Proof
Let $\{V_{i}\}_{i \in I}$ be a [[Open Cover]] of $f(K)$. Then, because $f$ is [[Continuous Function|continuous]], $\{f^{-1}(V_{i})\}_{i \in I}$ is a [[Set|collection]] of [[Open]] sets in $K$. Furthermore, because $\{V_{i}\}_{i \in I}$ is an [[Open Cover]] of $f(K)$, 
$$K \subset f^{-1}(f(K)) \subset f^{-1}(\bigcup\limits_{i \in I} V_{i}) = \bigcup\limits_{i \in I}f^{-1}(V_{i}),$$
so $\{f^{-1}(V_{i})\}_{i \in I}$ is an [[Open Cover]] of $K$. Since $K$ is [[Compact]], we can reduce to a [[Finite Set|finite]] [[Open Subcover]] of $K$, $\{f^{-1}(V_{i_{j}})\}_{j \in [n]}$ for some $n \in \mathbb{N}$. Then
$$f(K)) \subset f ( \bigcup\limits_{j \in [n]} f^{-1} (V_{i_{j}}) )= \bigcup\limits_{j \in [n]}f(f^{-1}(V_{i_{j}})) = \bigcup\limits_{j \in [n]} V_{i_{j}}.$$
Since $\{V_{i}\}_{i \in I}$ was an arbitrary [[Open Cover]], and we reduced it to [[Finite Set|finite]] [[Open Subcover]] of $f(K)$, we see that $f(K)$ is [[Compact]]. $\blacksquare$

# Other Outlinks
- [[Function Preimage]]
- [[Function Preimage preserves Elementary Set Operations]]
- [[Function Image preserves Set Union]]
- [[Natural Numbers]]