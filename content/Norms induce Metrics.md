# Statement
Suppose $X$ is a [[Normed Vector Space]] with [[Norm]] $||\cdot||: X \to \mathbb{R}_{\geq 0}$. Then $X$ is also a [[Metric Space]] when endowed with the [[Distance Function]]:
$$d(\mathbf{x}, \mathbf{y}) := ||\mathbf{x} - \mathbf{y}||.$$
## Proof
We need only establish that $d$ satisfies the axioms of a [[Distance Function]]:
1. Observe that $0 = d(\mathbf{x}, \mathbf{y}) = ||\mathbf{x} - \mathbf{y}||$ [[If and Only If]] $\mathbf{x} = \mathbf{y}$ by [[Non-Degeneracy]]. 
2. For any $\mathbf{x}, \mathbf{y} \in X$, $d(\mathbf{x}, \mathbf{y}) = ||\mathbf{x} - \mathbf{y}|| = |-1| ||\mathbf{y} - \mathbf{x}|| = ||\mathbf{y} - \mathbf{x}|| = d(\mathbf{y}, \mathbf{x})$
3. For any $\mathbf{x}, \mathbf{y}, \mathbf{z} \in X$,  $$\begin{align*}
d(\mathbf{x}, \mathbf{z}) &= ||\mathbf{x} - \mathbf{z}||\\
&= ||\mathbf{x} - \mathbf{y} + \mathbf{y} - \mathbf{z}||\\
&\leq ||\mathbf{x} - \mathbf{y}|| + ||\mathbf{y} - \mathbf{z}||\\
&=d(\mathbf{x}, \mathbf{y}) + d(\mathbf{y}, \mathbf{z})
\end{align*}$$
Thus $d$ is a [[Distance Function]] and $X$ is a [[Metric Space]].