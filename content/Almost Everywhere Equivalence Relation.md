---

title: "Almost Everywhere Equivalence Relation"

---
# Statement
Let $(X, \mathcal{M}, \mu)$ and $(Y, \mathcal{N}, \nu)$ be [[Measure Space]]s. Define the relation $\sim$ on $\mathcal{L}^{0}$ as $f \sim g$ for $f,g \in \mathcal{L}^{0}$ if $\{x \in X : f(x) \neq g(x)\}$ is a $\mu$-[[Null Set]]. Then $\sim$ is an [[Equivalence Relation]].

We define $L^{0} := \mathcal{L}^{0} / \sim$.

## Proof
1. If $f \in \mathcal{L}^{0}$, then $\{x \in X : f(x) \neq f(x)\} = \emptyset$. Since $\mu(\emptyset) = 0$, $f \sim f$. $\checkmark$
2. If $f,g \in \mathcal{L}^{0}$, then $\{x \in X : f(x) \neq g(x)\} = \{x \in X : g(x) \neq f(x)\}$. Thus $f \sim g \Rightarrow g \sim f$. $\checkmark$
3. Suppose $f,g,h \in \mathcal{L}^{0}$ and $f \sim g$ and $g \sim h$. Then $\{x \in X : f(x) \neq g(x)\}$ and $\{x \in X : g(x) \neq h(x)\}$ are both [[Null Set]]s. Note that if for $x \in X$, we have $f(x) \neq h(x)$, then we must have one of $f(x) \neq g(x)$ or $g(x) \neq h(x)$. Otherwise $f(x) = g(x) = h(x)$. Thus $$\{x \in X : f(x) \neq h(x)\} \subset \{x \in X : f(x) \neq g(x)\} \cup \{x \in X : g(x) \neq h(x)\}.$$ Since [[Counable Union of Null Sets is Null]] and by [[Monotonicity of Measures]], we see $f \sim  h$. $\checkmark$ $\blacksquare$