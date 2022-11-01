---
title: "The Induced Sigma Algebra of a Borel Function is Finite iff it is Simple"
---

# Statement
Let $X$ be a [[Set]]. Suppose $f: X \to \mathbb{R}$. Then $\sigma(f)$ with respect to $\mathcal{B}(\mathbb{R})$ is a [[Finite Set]] [[If and Only If]] $f$ is a [[Simple Function]].

## Proof
$(\Rightarrow)$: Suppose $f$ is not [[Simple Function|simple]]. Then $f(X)$ is an [[Infinite Set]]. Since [[Singletons are Closed in the Real Numbers]], they are in $\mathcal{B}(\mathbb{R})$. In other words, $\{y\} \in \mathcal{B}(\mathbb{R})$ for all $y \in f(X)$. Since $y \in f(X)$, we have that $f^{-1}(\{y\}) \neq \emptyset$. On the other hand for $y, z \in f(X)$ so that $y \neq z$, we have $f^{-1}(\{y\}) \cap f^{-1}(\{z\}) = f^{-1}(\{y\} \cap \{z\}) = f^{-1}(\emptyset) = \emptyset$, so each of our [[Function Preimage|preimages]] are [[Nonempty]] [[Disjoint Sets]] (and are thus distinct).  Therefore, we have infinitely many distinct sets in $\sigma(f)$. $\checkmark$

($\Leftarrow$): [[A Simple Function Induces a Finite Sigma Algebra]]. $\checkmark$ $\blacksquare$

# Other Outlinks
- [[Borel Sigma Algebra]]
- [[Real Numbers]]
- [[Set Intersection]]