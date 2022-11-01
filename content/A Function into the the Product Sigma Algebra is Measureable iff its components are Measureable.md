---

title: "A Function into the the Product Sigma Algebra is Measureable iff its components are Measureable"

---
# Statement
Let $(X, \mathcal{M})$, $(Y_{\alpha}, \mathcal{N}_\alpha)$ be [[Measure Space]]s for $\alpha \in A$. Let $Y = \prod\limits_{\alpha \in A} Y_\alpha$ and let $\mathcal{N} = \bigotimes\limits_{\alpha \in A} \mathcal{N}_\alpha$. Let $f : X \to Y$ and denote $f_{\alpha} := \pi_{\alpha} \circ f$, where $\pi_\alpha$ is the [[Projection Map]] for $\alpha \in A$. Then $f$ is $(\mathcal{M}, \mathcal{N})$-[[Measureable Function|measureable]] [[If and Only If]] $f_\alpha$ is $(\mathcal{M}, \mathcal{N}_\alpha)$-[[Measureable Function|measureable]] for every $\alpha \in A$.

## Proof
$(\Rightarrow)$: If $f$ is a [[Measureable Function]], then so is $f_{\alpha}$ since [[Projection Maps are Measureable Functions]] and [[Composition of Measureable Functions is Measureable]]. $\checkmark$

$(\Leftarrow)$: Recall that 
$$\bigotimes\limits_{\alpha \in A} \mathcal{N}_{\alpha}= \sigma(\mathcal{E} :=\{\pi_{\alpha}^{-1}(E) : \forall \alpha \in A, \forall E \in \mathcal{N}_\alpha\})$$
Then for every $E \in \mathcal{E}$, we have that $E = \prod\limits_{\beta \in A} E_{\beta}$ where there is some $\alpha \in A$ so that 
$$E_{\beta} = \begin{cases}  
E_{\alpha} \in \mathcal{N}_{\alpha} & \text{ if } \alpha = \beta \\
Y_{\beta}  & \text{ otherwise }
\end{cases}$$
for some $E_{\alpha} \in \mathcal{N}_{\alpha}$. Then 
$$\begin{align*}
f^{-1}(E) &= \bigcap\limits_{\beta  \in A} f_{\beta}^{-1}(E_{\beta})\\
&=f_{\alpha}^{-1}(E_\alpha)\\
&\in \mathcal{M}.
\end{align*}$$
Since [[A Function is Measureable iff Preimages of Generating Sets are in the Source Sigma-Algebra]], we have that $f$ is [[Measureable Function|measureable]]. $\checkmark$ $\blacksquare$

## Remarks
1. Indeed we can view the [[Product Sigma Algebra]] as the coarsest [[Sigma Algebra]] for which the [[Projection Map]]s are [[Measureable Function]]s.


# Other Outlinks
- [[Product Sigma Algebra]]
- [[Index Set]]
- [[Axiom Schema of Specification]]