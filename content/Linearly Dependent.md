---

title: "Linearly Dependent"

---
# Definition 1
Let $V$ be a [[Vector Space]] on [[Field]] $F$. Let $S \subset V$. $S$ is [[Linearly Dependent]] if there exists a [[Finite Set|finite]] subset $\{\mathbf{a}_{i}\}_{i=1}^{n}$ for some $n \in \mathbb{N}$ and constants $c_{1}, \dots, c_{n} \in F$ so that
1. $c_{1} \mathbf{a}_{1} + \cdots + c_{n} \mathbf{a}_{n} = \mathbf{0}$
2. $\exists i  \in [n]$ so that $c_{i} \neq 0$

# Definition 2
Let $V$ be a [[Vector Space]] on [[Field]] $F$. Let $\mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in V$ for some $n \in \mathbb{N}$. $\mathbf{a}_{1}, \dots, \mathbf{a}_{n}$ are [[Linearly Dependent]] if there exist constants $c_{1}, \dots, c_{n} \in F$ so that
1. $c_{1} \mathbf{a}_{1} + \cdots + c_{n} \mathbf{a}_{n} = \mathbf{0}$
2. $\exists i  \in [n]$ so that $c_{i} \neq 0$

## Remarks
- We call the appropriate constants nontrivial, in that just setting them all to $0$ is the trivial choice.
- In defiition 2, our vectors may be the same. If $\mathbf{a}_{i} = \mathbf{a}_{j}$ for some $i, j \in [n]$, $i \neq j$, then $\mathbf{a}_{i} + (-1)\mathbf{a}_{j} = \mathbf{0}$.