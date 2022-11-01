---

title: "Formula"

---
# Definition
The [[Set]] of $\mathcal{L}$-[[Formula|formula]]s is the [[Set Intersection|smallest set]] $\mathcal{W}$ that satisfies the following properties
1. If $\phi$ is an [[Atomic Language Formula|atomic]] $\mathcal{L}$-formula, then $\phi \in \mathcal{W}$.
2. If $\phi \in \mathcal{W}$, then $\neg \phi \in \mathcal{W}$.
3. If $\phi, \psi \in \mathcal{W}$, then $(\phi \wedge \psi) \in \mathcal{W}$ and $(\phi \vee \psi) \in \mathcal{W}$.
4. If $\phi \in \mathcal{W}$ and $v$ is a [[Variable Symbol]], then $\exists v \phi \in \mathcal{W}$ and $\forall v \phi \in \mathcal{W}$.

## Remarks
1. Similar to [[The Term Set is the Union of Term Sets of all Complexities]], we have that [[The Formula Set is the Union of Formula Sets of all Complexities]]. The proof is almost identical.
2. [[Formula]]s are [[Finite Set|finite]] strings (because [[Term]]s are also [[Finite Set|finite]]). This means they only include finitely many [[Variable Symbol]]s
3. We also use the abbreviation $\phi  \rightarrow \psi$ for $\neg \phi \vee \psi$ and $\phi \leftrightarrow \psi$ for $(\phi \rightarrow \psi) \wedge (\psi \rightarrow \phi)$.