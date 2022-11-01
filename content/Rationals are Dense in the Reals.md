---

title: "Rationals are Dense in the Reals"

---
# Statement 1
$\mathbb{Q}$ is a [[Dense]] subset of $\mathbb{R}$.

## Proof 1
Recalling the [[Sequence Completion Construction of the Reals]], every $x \in \mathbb{R}$ is defined as a an [[Equivalence Relation]] over [[Cauchy Sequence]]s in $\mathbb{Q}$, where elements of $\mathbb{Q}$ are identified with constant sequences. The space is endowed with the [[Limsup Norm]]. Let $x \in \mathbb{R}$ be identified by the [[Sequence]] $({x}_{n})_{n=1}^{\infty} \subset \mathbb{Q}$. This [[Sequence]] precisely gives us a [[Sequence]] of $\mathbb{Q} \subset \mathbb{R}$ that converges to $x$. Thus, because [[Closure of a Set in a Metric Space is all its Sequential Limits]], $\text{cl}\mathbb{Q} = \mathbb{R}$ and $\mathbb{Q}$ is [[Dense]].

[[TODO]] 
- [ ] Complete [[Sequence Completion Construction of the Reals]]

## Proof 2
[[TODO]]
- [ ] by [[Dedekind Cut Construction of the Reals]].

# Statement 2
$\mathbb{Q}^{n}$ is a [[Dense]] subset of $\mathbb{R}^{n}$ for $n \in \mathbb{N}$

## Proof
Use Statement 1 and apply [[Product of Dense Sets is Dense]]. $\blacksquare$

# Statement 3
$\mathbb{Q}^{\kappa}$ is a [[Dense]] subset of $\mathbb{R}^{\kappa}$ for any [[Set Cardinality|cardinal]] $\kappa$.

## Proof 
Use Statement 1 and apply [[Product of Dense Sets is Dense]]. $\blacksquare$