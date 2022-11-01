---

title: "A Set is a Basis iff it is a Maximal Linearly Independent Set"

---
# Statement
Let $V$ be a [[Vector Space]] Then $S \subset V$ is a [[Vector Space Basis]] for $V$ [[If and Only If]] it is a [[Maximal]] [[Linearly Independent]] subset of $V$. That is, there does not exist any [[Linearly Independent]] $R \subset V$ so that $S \subsetneq R$.

## Proof
($\Leftarrow$) Suppose not. Since $S$ is [[Linearly Independent]], we must have that $\text{span} S \subsetneq V$. But then there exists $\mathbf{v} \in V \setminus \text{span} S$. Consider $R:= S \cup \{\mathbf{v}\}$. By [[Growing a Linearly Independent Set]], we have that $R$ is [[Linearly Independent]], [[Proof by Contradiction|contradicting]] our assumption that $S$ is a [[Maximal]] [[Linearly Independent]] subset of $V$ $\unicode{x21af}$. Therefore $\text{span} S = V$ and $S$ is a [[Vector Space Basis]] for $V$. $\checkmark$

($\Rightarrow$) Let $\mathbf{v} \in V \setminus S$. Let $R \subset V$ is such that $R \supset S \cup \{\mathbf{v}\} \supsetneq S$. Since $S$ is a [[Vector Space Basis]] for $V$, we have that $\mathbf{v} \in \text{span} S$. Because [[The Subspace Span is the Set of all Linear Combinations]], there exists $c_{1}, \dots, c_{n} \in F$, $\mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in S$ for some $n \in \mathbb{Z}_{\geq 0}$ so that
$$\begin{align*}
&\mathbf{v} = c_{1} \mathbf{a}_{1} + \cdots + c_{n} \mathbf{a}_{n}\\
\Rightarrow &\mathbf{0} = c_{1} \mathbf{a}_{1} + \cdots + c_{n} \mathbf{a}_{n} - \mathbf{v},
\end{align*}$$
so $R$ is [[Linearly Dependent]]. Since $\mathbf{v}$ was arbitrary, $S$ must be [[Maximal]]. $\checkmark$ $\blacksquare$

## Remarks
1. Note that we account for $S = \emptyset$ in the $(\Rightarrow)$ direction by letting $n \in \mathbb{Z}_{\geq 0}$.

# Other Outlinks
- [[Subspace Span]]
- [[Set]]