---

title: "Differential Entropy of Uniform Random Variable"

---
# Statement
Let $X \sim \text{Unif}[a, b]$ for some $a < b \in \mathbb{R}$. Then $$\mathbb{H}(X) = \log(b - a)$$

## Proof
Recall that the [[Probability Density Function of the Continuous Uniform Distribution]] is $f_{X} = \frac{1}{b-a} \mathbb{1}_{[a, b]}$. Then $$\begin{align*}
\log f_{X} &= \log \frac{1}{b-a} + \log \mathbb{1}_{[a,b]}\\
&=-\log(b-a) + \log \mathbb{1}_{[a,b]}
\end{align*}$$
Thus 
$$\begin{align*}
f_{X} \log f_{X} &= \frac{1}{b-a} \mathbb{1}_{[a, b]} \Big[-\log(b-a) + \log \mathbb{1}_{[a,b]} \Big]\\
&= -\frac{\log(b-a)}{b-a} \mathbb{1}_{[a, b]} +  \frac{1}{b-a} \mathbb{1}_{[a, b]} \log \mathbb{1}_{[a,b]}\\
&-\frac{\log(b-a)}{b-a} \mathbb{1}_{[a, b]}\\
&=-\log(b-a) f_{X}
\end{align*}$$
since $\mathbb{1}_{[a,b]}\log \mathbb{1}_{[a,b]} = 0$. Thus,
$$\begin{align*}
\mathbb{H}(X) &= -\int\limits_{-\infty}^{\infty} f_{X}(x) \log (f_{X}(x))dx \\
&= -\int\limits_{-\infty}^{\infty} f_{X}(x)-\log(b-a) f_{X}(x)dx\\
&=\log(b-a)
\end{align*}$$


# Other Outlinks
- [[Continuous Uniform Distribution]]
- [[Real Numbers]]