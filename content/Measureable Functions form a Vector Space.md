---

title: "Measureable Functions form a Vector Space"

---
# Definition
Let $(X, \mathcal{M}, \mu)$ be a [[Measure Space]] and let $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. Then $L^{0}(X, \mathbb{K})$ is a [[Vector Space]].


## Proof
First we need to show the [[Vector Space]] operations are well defined. Observe if $[f], [f'], [g], [g'] \in L^{0}$ and $c \in \mathbb{K}$, Suppose $[f] = [f']$ and $[g] = [g']$. then $c[f] + [g] = [cf + g]$ and $c[f'] + [g'] = [cf' + g']$ by definition. Let $A := [f \neq f']$ and $B := [g \neq g']$. By definition, $\mu(A) = 0 = \mu(B)$. Note that if $x \in A^{C} \cap B^{C}$ then $cf(x) + g(x) = cf'(x) + g'(x)$. Thus $A^{C} \cap B^{C} \subset [cf + g \neq cf' + g']^{C}$, giving us $$A \supset A \cap B \supset [cf + g \neq cf' + g'].$$By [[Monotonicity of Measures]], $0 = \mu(A) \geq \mu([cf + g \neq cf' + g']) \geq 0$ so $\mu([cf + g \neq cf' + g']) = 0$. Therefore $[cf + g] = [cf' + g']$.

The [[Vector Space]] [[Axiom]]s follow mostly from the observation that $\mathcal{L}^{0}$ is [[Vector Space]] as well. Indeed [[Functions to a Field form a Vector Space]], so we need only show $\mathcal{L}^{0}$ is a [[Vector Subspace]]. Because [[Measureability is preserved by Algebraic Operations]], $cf + g \in \mathcal{L}^{0}$ for $c \in \mathbb{K}$ and $f,g \in \mathcal{L}^{0}$, $\mathcal{L}^{0}$ is a [[Vector Space]]. From this we see
1. $(L^{0}, +)$ is an [[Abelian Group]]:
	1. [[Additive Identity]]: [[Constant Functions are Measureable]], so $[0] \in L^{0}$. Furthermore for $[f] \in L^{0}$, $[f] + [0] = [f+0] = [f]$. $\checkmark$
	2. [[Associativity]] of $+$: For all $[f],[g],[h] \in L^{0}$, $([f] + [g]) + [h] = [(f + g) + h] = [f + (g + h)] = [f] + ([g] + [h])$. $\checkmark$
	3. [[Commutativity]] of $+$: For all $[f], [g] \in L^{0}$, $[f] + [g] = [f + g] = [g + f] = [g] + [f]$ . $\checkmark$
	4. [[Additive Inverse]]s: If $[f] \in L^{0}$, then $[-f] \in L^{0}$ and $[f] + [-f] = [f-f] = [0]$
2. Compatibility with [[Scalar Multiplication]] ($*$):
	1. [[Multiplicative Identity]]: For all $[f] \in L^{0}$ we have that $1 * [f] = [1 * f] = [f]$ (where $1$ is the [[Multiplicative Identity]] of $\mathbb{K}$).
	2. [[Associativity]]: For all $c,d \in \mathbb{K}$, $[f] \in L^{0}$, we have that $(cd)*[f] = [(cd) * f] = [c * (d * f)] c*(d*[f])$. $\checkmark$
	3. [[Distributivity]] of $*$ over $+$: For all $[f], [g] \in L^{0}$ and $c \in \mathbb{K}$, $c*([f] + [g]) = [c * (f + g)] = [cf + cg] = c[f] + c[g]$. $\checkmark$
	4. [[Distributivity]] of $*$ over $+_{F}$: For all $[f] \in L^{0}$ and $c, d \in \mathbb{K}$, $(c +_{\mathbb{K}} d) * [f] = [(c +_{\mathbb{K}} d) * f] = [cf + df] = c [f] + d [f]$

$\blacksquare$