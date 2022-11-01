---

title: "Axiom Schema of Specification"

---
# [[Axiom Schema]]
Let $k \in \mathbb{N}$ and let $\phi$ be a [[Formula]] with [[Free Variable]]s among $x, t_{1}, \dots, t_{k}, c$. Then the [[Sentence]] $$\forall t_{1} \cdots \forall t_{k} \forall c \exists B \forall x [x \in B \Leftrightarrow (x \in c \wedge \phi(x, c, t_{1}, \dots, t_{k}))]$$
is an [[Axiom]] in [[ZF-Theory]]. 

## Remarks
1. This [[Axiom]] effectively allows us to take any subset of a [[Set]] using a finite [[Formula]].
2. This is often known as the "Subset Axiom". 
3. If $A$ is a [[Set]] and $\phi$ is a [[Formula]] with [[Free Variable]]s among $x, t_{1}, \dots, t_{k}, A$, then we often write our desired subset as $\{x \in A : \phi(x, A, t_{1}, \dots, t_{k})\}$.
4. If we instead want to take a definable subset of $\mathcal{P}(A)$, we can instead write $\{x \subset A : \phi(x, \mathcal{P}(A), A, t_{1}, \dots, t_{k})\}$, where $A$ can be treated as one of the extra [[Free Variable]]s of $\phi$.
