---

title: "A Measureable Function is less than or equal to another iff all its integrals are less than or equal to the others"

---
# Statement
Let $(X, \mathcal{M}, \mu)$ be a [[Measure Space]] and let $f, g \in L^{1}(\mathcal{M})$. Then $f \leq g$ [[Almost Everywhere]] [[If and Only If]]
$$\int\limits_{A} f d \mu \leq \int\limits_{A} g d \mu$$
$\forall A \in \mathcal{M}$.

## Proof
$(\Rightarrow)$: Let $A \in \mathcal{M}$. If $f \leq g$, then $\mathbb{1}_{A}f \leq \mathbb{1}_{A}g$. By [[Integration is Non-Decreasing]], we get the result. $\checkmark$

$(\Leftarrow)$: Consider $A = [f > g] \in \mathcal{M}$. Observe that $\int\limits_{A} f - g =\int\limits_{A} f - \int\limits_{A} g \leq 0$. But $\forall x \in A$, $f(x) - g(x) > 0$, so $\int\limits_{A} f - g \geq 0$. Therefore $\int\limits_{A} f - g = 0$. Recall that [[Integration of a Nonnegative Function is 0 iff the Function is 0 Almost Everywhere]], so we must have that $\mathbb{1}_{A} (f - g) = 0$ [[Almost Everywhere]]. But $\forall x \in A$, $\mathbb{1}_{A} (f(x) - g(x)() > 0$, therefore $\mu(A) = 0$. Thus $f \leq g$ [[Almost Everywhere]]. $\blacksquare$

# Other Outlinks
- [[Borel Measureable Function]]
- [[L1 Integrable Functions]]
- [[Comparing two Measureable Functions is a Measureable Set]]