---

title: "Hamming Distance"

---
# Definition
Let $H_{n} = \{0, 1\}^{n}$ be the $n$-dimensional [[Hypercube]]. The [[Hamming Distance]] $d: H_{n} \to_{\geq 0}$ is the [[Distance Function]]

$$d(x, y) := |\{i : x_{i} \neq y_{i}\}| = \sum\limits_{i \in \mathbb{N}} x_{i} \oplus y_{i}$$

## The [[Hamming Distance]] is a [[Distance Function]]
### Proof
We check that [[Hamming Distance]] satisfies the [[Distance Function]] axioms.
1. Observe that $d(x, x) = |\{i : x_{i} \neq x_{i}\}| = |\emptyset| = 0$ for all $x \in H_{n}$. Further if $x \neq y$, then there exists $i \in [n]$ so that $x_{i} \neq y_{i}$ and $d(x, y) \geq 1$. $\checkmark$
2. Consider $x, y \in H_{n}$. $d(x, y) = |\{i : x_{i} \neq y_{i}\}| = |\{i : y_{i} \neq x_{i}\}| = d(y, x)$. $\checkmark$
3. Consider $x, y, z \in H_{n}$. Then if $x_{i} = y_{i} = z_{i}$ for $i \in [n]$, we know $x_{i} = z_{i}$. Thus, if $x_{i} \neq z_{i}$, then either $x_{i} \neq y_{i}$ or $y_{i} \neq z_{i}$ for some $i  \in [n]$. Thus 
4. $$\begin{align*}
d(x, z) &= |\{i : x_{i} \neq z_{i}\}|\\
&\leq|\{i : x_{i} \neq y_{i}\} \cup \{i : y_{i} \neq z_{i}\}|\\
&\leq|\{i : x_{i} \neq y_{i}\}| + | \{i : y_{i} \neq z_{i}\}|\\
&=d(x, y) + d(y, z).
\end{align*}$$ $\checkmark$

Thus, the [[Hamming Distance]] is a [[Distance Function]]. $\blacksquare$