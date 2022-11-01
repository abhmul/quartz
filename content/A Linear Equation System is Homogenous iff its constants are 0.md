---

title: "A Linear Equation System is Homogenous iff its constants are 0"

---
# Statement
Let $V, W$ be [[Vector Space]]s over the same [[Field]] $F$. Consider the [[Linear Equation System]]
$$T_{\alpha}(\mathbf{x}) = \mathbf{b}_{\alpha} \text{ }\forall \alpha \in A$$
Then this system is a [[Homogenous Linear System]] [[If and Only If]] $\mathbf{b}_{\alpha} = \mathbf{0} \in W$ $\forall \alpha \in A$.

## Proof
 [[TODO]] - cleanup, but idea is good
$(\Rightarrow)$ $S$ is [[Solution Set]] and it is a [[Vector Subspace]] of $V$. Then $\mathbf{x} + \mathbf{y} \in S$ and $\forall \alpha \in A$
$$\begin{align*}
\mathbf{b}_{\alpha} &= T_{\alpha}(\mathbf{x} + \mathbf{y})\\
&=T_\alpha(\mathbf{x}) + T_{\alpha}(\mathbf{y})\\
&=\mathbf{b}_{\alpha}+ \mathbf{b}_\alpha\\
\Rightarrow \mathbf{0} &= \mathbf{b}_{\alpha}
\end{align*}$$
$\checkmark$

$(\Leftarrow)$: Establish that $S$ is a [[Vector Subspace]] by [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]]. $\checkmark$