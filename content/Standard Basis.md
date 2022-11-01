---

title: "Standard Basis"

---
# Definition
Let $F$ be a [[Field]] and let $n \in \mathbb{N}$. Denote $\epsilon_{i} = (0, \dots, 0, 1, 0, \dots, 0) \in F^{n}$ to be the element of all $0$'s except for a $1$ in the $i$th position for some $i \in [n]$. The [[Standard Basis]] is the set:
$$S = \{\epsilon_{i}\}_{i=1}^{n}$$
## Remarks
### The [[Standard Basis]] is a [[Vector Space Basis]] for $F^{n}$
$S$ [[Subspace Span|spans]] $F^{n}$: for any $\mathbf{x} = (x_{1}, \dots, x_{n}) \in F^{n}$, we have that
$$x_{1} \epsilon_{1} + \cdots + x_{n} \epsilon_{n} = \mathbf{x}.$$
[[The Subspace Span is the Set of all Linear Combinations]], so $\text{span} S \supset F^{n}$. But, $\text{span} S \subset F^{n}$ by definition, so we must have that $\text{span} S = F^{n}$. $\checkmark$

$S$ is [[Linearly Independent]]: Suppose $c_{1}, \dots, c_{n} \in F$ and that 
$$c_{1} \epsilon_{1} + \cdots  + c_{n} \epsilon_{n} = \mathbf{0}.$$
But 
$$c_{1} \epsilon_{1} + \cdots  + c_{n} \epsilon_{n} = (c_{1}, \dots, c_{n}) = \mathbf{0} = (0, \dots, 0),$$
so $c_{1} = \cdots = c_{n} = 0$, and we have that $S$ is [[Linearly Independent]]. $\checkmark$ $\blacksquare$