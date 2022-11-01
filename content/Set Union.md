---

title: "Set Union"

---
# Definition 1
Let $A$, $B$ be [[Set]]s. Then $A \cup B := \{x : x \in A \vee x \in B\}$.

## Proof of Existence
By [[Axiom of Pairing]], we can make the [[Set]] $\{A, B\}$. Then, by [[Axiom of Union]] we have 
$$\begin{align*}
\bigcup\limits_{} \{A, B\} &= \{x : \exists D \in \{A, B\} (x \in D)\}\\
&=\{x : x \in A \vee x \in B\}
\end{align*}$$
$\blacksquare$

# Definition 3
Let $\mathcal{A}$ be a [[Set|collection]] of [[Set]]s. Then we define $$\bigcup\limits_{A \in \mathcal{A}} A := \bigcup\limits_{} \mathcal{A}$$
Existence follows directly from the [[Axiom of Union]].


# Encounters
- [[Enderton - Elements of Set Theory]]
- [Lian - Fundamentals of ZFC](https://drive.google.com/file/d/1HqqHQIMNTcFwY3icnuvhq57-52ZNQhIi/view?usp=sharing)