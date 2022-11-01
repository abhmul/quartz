---

title: "A Set is a Basis iff it is a Minimal Spanning Set"

---
# Statement
Let $V$ be a [[Vector Space]] over [[Field]] $F$. Then $S \subset V$ is a [[Vector Space Basis]] [[If and Only If]] it is a [[Minimal]] [[Spanning Set|spanning]] subset of $V$. That is, there does not exist any [[Spanning Set|spanning]] $R \subset V$ so that $R \subsetneq S$.

## Proof
($\Leftarrow$) We know $S$ is a [[Minimal]] [[Spanning Set|spanning]] subset of $V$. Suppose it is not a [[Vector Space Basis]] of $V$. Since $\text{span} S = V$, we must have that $S$ is [[Linearly Dependent]]. Then, because [[A Linearly Dependent Set contains a vector in the Span of the others]], $\exists \mathbf{v} \in S$ so that $\mathbf{v} \in \text{span} R$ for $R = S \setminus \mathbf{v}$. Then we have that $\text{span} R \supset S$, so, because [[The Span of subset of a Span is also a subset of that Span]]
$$V \supset \text{span} R \supset \text{span} S = V$$
and $\text{span} R = V$. But that would mean $S$ is not [[Minimal]] $\unicode{x21af}$. Therefore $S$ is a [[Vector Space Basis]] for $V$. $\checkmark$

($\Rightarrow$) We know $S$ is a [[Vector Space Basis]]. If $S = \emptyset$, then it is [[Minimal]]. Otherwise, suppose $S \neq \emptyset$. Let $\mathbf{v} \in S$ and consider $R \subset S \setminus \{\mathbf{v}\} \subsetneq S$. Suppose $R$ was a [[Vector Space Basis]] for $V$ as well. Then $\mathbf{v} \in \text{span} R = V$, so because [[The Subspace Span is the Set of all Linear Combinations]], there exists $c_{1}, \dots, c_{n} \in F$, $\mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in R$ for some $n \in \mathbb{Z}_{\geq 0}$ so that
$$\begin{align*}
&\mathbf{v} = c_{1} \mathbf{a}_{1} + \cdots + c_{n} \mathbf{a}_{n}\\
\Rightarrow &\mathbf{0} = c_{1} \mathbf{a}_{1} + \cdots + c_{n} \mathbf{a}_{n} - \mathbf{v},
\end{align*}$$
so $R$ is [[Linearly Dependent]]. Since $\mathbf{v}$ was arbitrary, $S$ must be [[Minimal]]. $\checkmark$ $\blacksquare$

# Other Outlinks
- [[Subspace Span]]
- [[Proof by Contradiction]]
- [[Set]]
