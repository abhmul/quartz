---

title: "Closure of Open Unit Ball is Closed Unit Ball"

---
# Statement
Let $X$ be a [[Normed Vector Space]]. Then $\text{cl}B(X) = \overline{B(X)}$.

## Proof
[[Closure of Open Ball is a subset of Closed Ball]] so $\text{cl}B(X) \subset \overline{B(X)}$. To see the other direction, note that for $x \in X$ so that $||x|| = 1$, we can construct a [[Sequence]] $x_{n} \to x$ from $B(X)$ by picking $x_{n} = (1-\frac{1}{n})x$. Since $||x_{n}|| = (1-\frac{1}{n})||x|| = \left(1-\frac{1}{n}\right)< 1$, $x_{n} \in B(X)$ as we desired. Then, $||x_{n} - x|| = \frac{1}{n}||x|| = \frac{1}{n} \to 0$, so $x_{n} \to x$. Because [[Closure of a Set in a Metric Space is all its Sequential Limits]], $x \in \text{cl}B(X)$. $\blacksquare$

# Other Outlinks
- [[Closure]]
- [[Closed Unit Ball]]
- [[Open Unit Ball]]