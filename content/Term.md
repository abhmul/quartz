---

title: "Term"

---
# Definition
The [[Set]] $\mathcal{T}$ of $\mathcal{L}$-[[Term]]s is the [[Set Intersection|smallest set]] such that the following properties hold:
1. $c \in \mathcal{T}$ for each $c \in \mathcal{C}$
2. $\{v_{i} : i \in \mathbb{N}\} \subset \mathcal{T}$, where each $v_{i}$ is a distinct [[Variable Symbol]] for each $i \in \mathbb{N}$.
3. If $t_{1}, \dots, t_{n_{f}} \in \mathcal{T}$, then $f(t_{1}, \dots, t_{n_{f}}) \in \mathcal{T}$.

## Remarks
1. Note that the 3rd property makes sense when we interpret it with a [[Language Structure]], since the inputs to the [[Function]] are either
	1. A [[Constant Symbol]]
	2. A [[Variable Symbol]]
	3. The output of another [[Function]].
2. [[Term]]s are [[Finite Set|finite]] strings. Thus, they can only include [[Finite Set|finitely]] many [[Variable Symbol]]s.

# Other Outlinks
- [[Language]]