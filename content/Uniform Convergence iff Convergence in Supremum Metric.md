---

title: "Components Converge iff Convergence in Product Metric Space"

---
# Statement
Let $(M_{i}, d_{i})_{i \in I}$ be [[Metric Space]]s with [[Index Set]] $I$ and let $M = \prod\limits_{i \in I}^{}  M_{i}$ be the [[Product Metric Space]] with [[Supremum Metric]]. Let $(x^{(n)})_{n=1}^{\infty} \subset M$ and let $x \in M$. Then $x^{(n)} \to x$ [[If and Only If]] $x^{(n)}_{i} \to x_{i}$ [[Uniform Convergence|uniformly]] for all $i \in I$.

## Proof
($\Rightarrow$): Let $\epsilon > 0$. Since $x^{(n)} \to x$, there exists a $N \in \mathbb{N}$ so that for all $n \geq N$, $\sup\limits_{i \in I}d_{i}(x^{(n)}_{i}, x_{i}) < \epsilon$. Therefore, for all $i \in I$, $d_{i}(x^{(n)}_{i}, x_{i}) < \epsilon$. Thus $x^{(n)}_{i} \to x_{i}$ for all $i \in I$. $\checkmark$

$(\Leftarrow)$: Let $\epsilon > 0$. There exists $N \in \mathbb{N}$ so for all $n \geq N$ and $i \in I$, $d_{i}(x^{(n)}_{i}, x_{i}) < \epsilon$. Thus $\sup\limits_{i \in I}d_{i}(x^{(n)}_{i}, x_{i}) < \epsilon$ for all $n \geq N$. Therefore $x^{(n)} \to x$. $\checkmark$ $\blacksquare$