---

title: "If small sets on one measure are also small on another measure then it is absolutely continuous wrt the other"

---
# Statement
Let $(X, \mathcal{M})$ be a [[Measure Space]] and let $\mu, \nu$ be two [[Measure]]s on this space so that $\forall \epsilon > 0$, $\exists \delta > 0$ so that $\forall A \in \mathcal{M}$ so that $\mu(A) < \delta$, we have that $\nu(A) < \epsilon$. Then $\nu << \mu$.

[[TODO]] generalize to [[Signed Measure]]s and [[Complex Measure]]s

## Proof
 Let $A \in \mathcal{M}$ be such that $\mu(A) = 0$. We wish to show $\nu(A) = 0$ as well. Let $\epsilon > 0$. Then for any choice of $\delta > 0$, we have that $\delta > \mu(A)$. Thus $\nu(A) < \epsilon$. This holds for arbitrary $\epsilon > 0$ so by the [[Epsilon Principle]], $\nu(A) = 0$ and we have that $\mu >> \nu$. $\blacksquare$