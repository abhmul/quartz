---

title: "A Linearly Dependent Set contains a vector in the Span of the others"

---
# Statement
Let $V$ be a [[Vector Space]] on [[Field]] $F$ and let $S \subset V$ be [[Linearly Dependent]]. Then there exists $\mathbf{v} \in S$ so that $\mathbf{v} \in \text{span} (S \setminus \{v\})$.

## Proof
Since $S$ is [[Linearly Dependent]], there exist distinct $\mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in S$, $c_{1}, \dots, c_{n} \in F$ for some $n \in \mathbb{N}$ so that 1. $\exists i  \in [n]$ $c_{i}\neq 0$
2. $c_{1} \mathbf{a}_{1} + \cdots + c_{n} \mathbf{a}_{n} = \mathbf{0}$

If $n=1$, then $c_{1} \neq 0$, do we must have that $\mathbf{a}_{1} = \mathbf{0}$. Then $\mathbf{a}_{1} \in \text{span} \emptyset \subset \text{span} (S \setminus \{\mathbf{a}_1\})$ since $\emptyset \subset S \setminus \{\mathbf{a}_{1}\}$ and [[Span is Monotonic]].

If $n > 1$, then [[Without Loss of Generality]], let $c_{1} \neq 0$ (by [[Commutativity]]). Then

$$\begin{align*}
&c_{1} \mathbf{a}_{1} + \cdots + c_{n} \mathbf{a}_{n} = \mathbf{0}\\
\Rightarrow &c_{1} \mathbf{a}_{1} = -c_{2} \mathbf{a}_{2} - \cdots - c_{n} \mathbf{a}_{n}\\
\Rightarrow & \mathbf{a}_{1} = -c_{1}^{-1}c_{2} \mathbf{a}_{2} - \cdots - c_{1}^{-1}c_{n} \mathbf{a}_{n}.
\end{align*}$$
Since [[The Subspace Span is the Set of all Linear Combinations]], we have that $\mathbf{a}_{1} \in \text{span} (S \setminus \{\mathbf{a}_1\})$. $\blacksquare$

# Other Outlinks
- [[Subspace Span]]