---

title: "A Subset of a Vector Space is a Subspace iff it contains all its Linear Combinations"

---
# Statement
$W$ is a [[Vector Subspace]] of $V$ [[If and Only If]] $\forall n \in \mathbb{Z}_{\geq 0}$, $x_{1}, \dots x_{n} \in W$, $c_{1}, \dots, c_{n} \in F$, $c_{1} x_{1} + \cdots + c_{n} x_{n} \in W$.

## Proof
$(\Rightarrow)$ This follows from the definiton of a [[Vector Subspace]], all the necessary operations stay within the [[Vector Subspace]]. $\checkmark$

($\Leftarrow$) Let $n = 2$ and choose $x_{1}, x_{2} \in W$ and $c \in F$. Then, $c x_{1} + 1 * x_{2}$ is a valid [[Linear Combination]] and is thus in $W$. Since [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]], we have that $W$ is a [[Vector Subspace]]. $\checkmark$ $\blacksquare$