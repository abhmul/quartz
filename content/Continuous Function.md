---
title: "Continuous Function"
---

# Definition 1
Let $(X, \tau), (Y, \rho)$ be [[Topological Space]]s and let $f: X \to Y$ be a [[Function]]. Then $f$ is a [[Continuous Function]] if $\forall V \in \rho$
$$f^{-1}(V) \in \tau$$
## Remarks
1. Sometimes we refer to the [[Set]] of [[Continuous Function]]s as $C(X, Y)$. If $Y$ is omitted, it is usually understood to be $\mathbb{R}$. 
2. We may also refer to the [[Set]] as $C^{0}(X)$ if we are working in the context of [[Differentiation]]

## Properties
1. [[A Function is Continuous iff it preserves Net Convergence]]
2. [[A Function is Continuous iff it takes Basis Sets back to Open Sets]]
3. [[A Function is Continuous iff it takes Closed Sets back to Closed Sets]]
4. [[Continuous Functions Preserve Connectedness]]
5. [[Continuous Functions Preserve Compactness]]
6. [[Continuous Functions Preserve Limit Points]]
7. [[Continuous Functions Preserve Sequence Limits]]
8. [[Continuous Functions to Hausdorff Spaces are Determined on Dense Sets]]

# Definition 2
Let $(X, d_{X})$, $(Y, d_{Y})$ be [[Metric Space]]s. Then a [[Function]] $f: X \to Y$ is a [[Continuous Function]] if for all [[Sequence Convergence|convergent sequences]] $x_{n} \to x$ in $X$, $f(x_{n}) \to f(x)$.

# [[TODO]]
- [ ] Connect together all the different criteria defining [[Continuous Function]]s over
	- [x] [[Metric Space]]s
	- [ ] [[Hausdorff]], [[First Countable Space]]s


# Other Outlinks
- [[Function Preimage]]