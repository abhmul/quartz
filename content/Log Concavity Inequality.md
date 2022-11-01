---

title: "Log Concavity Inequality"

---
# Statement
Let $a, b > 0$ and let $0 \leq \lambda \leq 1$. Then the following inequality holds
$$a^{\lambda}b^{1-\lambda}  \leq \lambda a + (1-\lambda) b$$
with equality [[If and Only If]] $\lambda = 0$ or $1$, or $a=b$.

## Proof
By [[Strict Concavity of Log]], 
$$\begin{align*}
&\lambda \log a + (1-\lambda) \log b \leq \log (\lambda a + (1-\lambda)b)\\
\Rightarrow& \log (a^{\lambda} b^{1-\lambda}) \leq \log(\lambda a + (1-\lambda) b)\\
\Rightarrow& a^{\lambda}b^{1-\lambda}  \leq \lambda a + (1-\lambda) b
\end{align*}$$
because the [[Exponential is Non-decreasing]].

Equality certainly holds if $\lambda = 0,1$ since the inequality reduces to either $a \leq a$ or $b \leq b$. If $a=b$ then the inequality reduces to $a \leq a$. The other direction follows from [[Strict Concavity of Log]] and the definition of a [[Strictly Convex Function]]. It states that if $\lambda \in (0,1)$ and $a \neq b$, then the inequality is strict. Thus, by [[Contraposition]], if equality holds, then either $\lambda \in \{0,1\}$ or $a=b$. $\blacksquare$

