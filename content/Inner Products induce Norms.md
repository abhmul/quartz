# Statement
Suppose $X$ is an [[Inner Product Space]] with [[Inner Product]] $\langle \cdot, \cdot \rangle: X \to \mathbb{C}$. Then $||\cdot||: X \to \mathbb{R}_{\geq 0}$ defined as 
$$||\mathbf{x}|| = \sqrt{\langle \mathbf{x}, \mathbf{x} \rangle}$$
is a [[Norm]]. This makes $X$ a [[Normed Vector Space]] as well.

## Proof
We must simply show that $|| \cdot ||$ as defined has [[Codomain]] $\mathbb{R}_{\geq 0}$ and it satisfies the [[Norm]] axioms:
1. By [[Positive Definiteness]], $||\cdot||$ does indeed have [[Codomain]] $\mathbb{R}_{\geq 0}$
2. By [[Positive Definiteness]], $||\mathbf{x}|| = \langle \mathbf{x}, \mathbf{x} \rangle = \mathbf{0}$ [[If and Only If]] $\mathbf{x} = \mathbf{0}$.
3. Suppose $c \in \mathbb{C}$ and $\mathbf{x} \in X$. Then  $$||c \mathbf{x}|| ^ {2} = \langle c \mathbf{x}, c \mathbf{x} \rangle = c \overline{c} \langle \mathbf{x}, \mathbf{x} \rangle = |c|^{2} \langle \mathbf{x}, \mathbf{x} \rangle$$
	so $||c \mathbf{x}|| = |c| ||\mathbf{x}||$.
4. Suppose $\mathbf{x}, \mathbf{y} \in X$. Then $$\begin{align*}
||\mathbf{x} + \mathbf{y}|| &= \sqrt{\langle \mathbf{x} + \mathbf{y}, \mathbf{x} + \mathbf{y} \rangle}\\
&= \sqrt{\langle \mathbf{x}, \mathbf{x} \rangle + \langle \mathbf{x}, \mathbf{y} \rangle + \langle \mathbf{y}, \mathbf{x} \rangle + \langle \mathbf{y}, \mathbf{y} \rangle}\\
&=\sqrt{||\mathbf{x}||^{2} + 2 \text{Re}\langle \mathbf{x}, \mathbf{y} \rangle + ||\mathbf{y}||^{2}}\\
&\leq\sqrt{||\mathbf{x}||^{2} + 2 |\langle \mathbf{x}, \mathbf{y} \rangle| + ||\mathbf{y}||^{2}}\\
&\leq\sqrt{||\mathbf{x}||^{2} + 2 ||\mathbf{x}|| ||\mathbf{y}|| + ||\mathbf{y}||^{2}} &\text{(Cauchy Schwarz)}\\
&= ||\mathbf{x}|| + ||\mathbf{y}||
\end{align*}$$

Thus $||\cdot||$ is indeed a [[Norm]], making $X$ a [[Normed Vector Space]]. $\blacksquare$