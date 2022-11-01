---

title: "Directed Partial Ordering"

---
# Definition
Let $A$ be a [[Partial Ordering]]. We call $A$ a [[Directed Partial Ordering]] if $\forall \alpha, \beta \in A$ $\exists \gamma \in A$ s.t. $\alpha \leq \gamma$ and $\beta \leq \gamma$.

## Remarks
1. We are effectively trying to capture the idea that we can always find a "later" element in the [[Partial Ordering]] after any two elements.
2. All [[Total Ordering]]s are [[Directed Partial Ordering]]. Indeed for [[Total Ordering]] $(T, \leq)$, for $\alpha, \beta \in T$, we must either have $\alpha \leq \beta$ or $\beta \leq \alpha$. Then $\max\limits(\alpha, \beta) \in A$ and $\alpha \leq \max\limits(\alpha, \beta)$ and $\beta \leq \max\limits(\alpha, \beta)$.