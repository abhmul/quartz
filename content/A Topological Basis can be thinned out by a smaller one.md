---

title: "A Topological Basis can be thinned out by a smaller one"

---
# Statement
Let $X$ be a [[Topological Basis]] and let $\mathcal{M}$ be a [[Topological Basis]]. Then if $\mathcal{B}$ is another [[Topological Basis]] for $X$, there exists $\mathcal{B}' \subset \mathcal{B}$ so that
1. $\mathcal{B}'$ is a [[Topological Basis]] for $X$.
2. $|\mathcal{B}'| \leq \max\limits(|\mathcal{M}|, \aleph_{0})$

## Proof
Construct [[Index Set]] $I = \{(M_{1}, M_{2}) : M_{1}, M_{2} \in \mathcal{M}, \exists B \in \mathcal{B} \text{ so that } M_{1} \subset B \subset M_{2}\}$. Using [[Axiom of Choice]], choose $B_{\alpha}$ for $\alpha \in I$ so that 
$$\alpha_{1} \subset B_{\alpha}\subset \alpha_{2}$$
and call this [[Set]] $\mathcal{B}'$. Since $I \subset \mathcal{M} \times  \mathcal{M}$, we have $|\mathcal{B}'| = |I| \leq |\mathcal{M}|^{2} \leq \max\limits(|\mathcal{M}|, \aleph_{0})$.

Now we must show $\mathcal{B}'$ is a [[Topological Basis]]. Let $U \subset X$ be [[Open]]. Then, because $\mathcal{M}$ is a [[Topological Basis]], there exists $\{M_x\}_{x \in U} \subset \mathcal{M}$ s.t. $\bigcup\limits_{x \in U} M_{x} = U$.  Because each $M_x$ is [[Open]], there exists $B \in \mathcal{B}$ so that $x \in B \subset M_{x}$. Since $B$ is [[Open]], there is a $M' \in \mathcal{M}$ so that $x \in M' \subset B$. Thus $\alpha := (M', M_{x}) \in I$ so there is a $B_{\alpha} \in \mathcal{B}'$ so that $x \in M' \subset B_{\alpha} \subset M_x$. Denote this $B_{\alpha}=: B_{x}$. Then $$\bigcup\limits_{x \in U} B_{x} = U$$ because for each $x \in U$, $x \in B_{x}$ and $B_{x} \subset M_{x} \subset U$. Thus $\mathcal{B}'$ is a [[Topological Basis]]. $\blacksquare$


## Encounters
1. https://math.stackexchange.com/a/2348694/706719

## Remarks
1. This could be tightend up even further to assert that $\mathcal{B}'$ will be a [[Finite Set|finite]] if $\mathcal{M}$ is.

# Other Outlinks
- [[Cardinal Arithmetic]]
- [[Countable]]