---

title: "Formulas are Finite"

---
# Statement
Let $\mathcal{L}$ be a [[Language]] and let $\mathcal{W}$ be the [[Set]] of $\mathcal{L}$-[[Formula]]s. Each $\phi \in \mathcal{W}$ is a [[Finite Set|Finite]] [[String]].

## Proof 1
This is a slick proof courtesy of [[Nick Hanson]].

Consider the [[Set]] of [[Finite Set|finite]] [[Formula]]s, $\mathcal{W}'$. This [[Set]] exists by [[Axiom Schema of Specification]] (since we constructed a superset in [[The Formula Set is the Union of Formula Sets of all Complexities]]). Observe that $\mathcal{W}'$ is closed under the defining properties of the [[Formula]] [[Set]] $\mathcal{W}$ (since [[Terms are Finite]]). Since $\mathcal{W}$ is the [[Set Intersection|smallest]] such set, $\mathcal{W} \subset \mathcal{W}'$. Thus each $\phi \in \mathcal{W}$ is [[Finite Set|finite]].

## Remarks
1. See remark (2) in [[Formula]].
2. Related to [[Terms are Finite]]
