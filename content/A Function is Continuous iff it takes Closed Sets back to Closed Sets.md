---

title: "A Function is Continuous iff it takes Closed Sets back to Closed Sets"

---
# Statement
Let $(X, \tau), (Y, \rho)$ be [[Topological Space]]s and let $f: X \to Y$ be a [[Function]]. Then $f$ is a [[Continuous Function]] [[If and Only If]] for all [[Closed]] $K \subset Y$, $f^{-1}(Y)$  is [[Closed]] in $X$.

## Proof
$(\Rightarrow)$: Suppose $f$ is a [[Continuous Function]]. Suppose $K \subset Y$ is [[Closed]]. Then, by definition $V:= K^{C}$ is [[Open]]. So $f^{-1}(V) = f^{-1}(K^{C}) = f^{-1}(K)^{C}$ is [[Open]], where the last equality follows from [[Function Preimage preserves Elementary Set Operations]]. Thus $(f^{-1}(K)^{C})^{C} = f^{-1}(K)$ is [[Closed]]. $\checkmark$

($\Leftarrow$): Let $V \subset Y$ be [[Open]]. Then, by definition, $V^{C}$ is [[Closed]] in $Y$. By assumption $f^{-1}(V^{C})$ is [[Closed]]. Because [[Function Preimage preserves Elementary Set Operations]], $$f^{-1}(V^{C}) = f^{-1}(V)^{C}$$ so $(f^{-1}(V)^{C})^{C} = f^{-1}(V)$ is [[Open]]. Thus $f$ is a [[Continuous Function]].

# Other Outlinks
- [[Function Preimage]]