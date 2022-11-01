---

title: "Sigma Algebra produced by a Function"

---
# Statement
Let $(X, \mathcal{M})$ be a [[Measure Space]], $Y$ a [[Set]] and $f : X \to Y$ a [[Function]]. Then
$$\sigma^{*}(f) = \{E \subset Y : f^{-1}(E) \in \mathcal{M}\}$$
is a [[Sigma Algebra]]. It is called the [[Sigma Algebra produced by a Function]].

## Proof
We check the definition of a [[Sigma Algebra]]:
1. $f^{-1}(Y) = X \in \mathcal{M}$ because $\mathcal{M}$ is a [[Sigma Algebra]]. Therefore $Y \in \sigma^{*}(f)$.
2. Suppose $E \in \sigma^{*}(f)$. Because $f^{-1}(E^{C}) = f^{-1}(E)^{C} \in \mathcal{M}$, we have that $E^{C} \in \sigma^{*}(f)$.
3. Suppose $({E}_{n})_{n=1}^{\infty} \subset \sigma^{*}(f)$. Then $f^{-1}(\bigcup\limits_{n=1}^{\infty} E_{n}) = \bigcup\limits_{n=1}^{\infty} f^{-1}(E_{n}) \in \mathcal{M}$. Therefore, $\bigcup\limits_{n=1}^{\infty} E_{n} \in \sigma^{*}(f)$

Therefore $\sigma^{*}(f)$ is a [[Sigma Algebra]] on $Y$. $\blacksquare$

## Remarks
1. $f$ is by construction $(\mathcal{M}, \sigma^{*}(f))$-[[Measureable Function|measureable]].


# Other Outlinks
1. [[Axiom Schema of Specification]]
2. [[Function Preimage preserves Elementary Set Operations]]