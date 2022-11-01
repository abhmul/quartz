---
title: "Conditional Expectation with respect to a Set is Integral divided by Probability"
---

# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $X$ be a [[Random Variable]] in $\bar{L^{1}}(\mathcal{B})$. Suppose $B \in \mathcal{B}$ so that $\mathbb{P}(B) \neq 0$. Then 

$$\mathbb{E}(X|B) = \frac{1}{\mathbb{P}(B)} \int\limits_{B} X d \mathbb{P}(\omega) = \frac{\mathbb{E}(1_{B} X)}{\mathbb{P}(B)}$$
## Proof
Recall that $\mathbb{E}(X|B) = \mathbb{E}(X|1_{B})(\omega)$ for any $\omega \in B$. So we are really checking that 
$$\mathbb{E}(X|1_{B})(\omega) = 
	\begin{cases} 
		\frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} &\text{if } \omega \in B\\
		\frac{\mathbb{E}(1_{B^{C}}X)}{\mathbb{P}(B^{C})} &\text{if } \omega \in B^{C}
	\end{cases} 
= \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} 1_{B} + \frac{\mathbb{E}(1_{B^{C}}X)}{\mathbb{P}(B^{C})} 1_{B^{C}}$$
All we need to do is check our candidate for $\mathbb{E}(X|1_{B})$ satisfies the definition of [[Conditional Expectation]]. That is, we must check that for all [[Set]]s in $\sigma(1_{B}) = \{\emptyset, B, B^{C}, \Omega\}$ we satisfy the integral criterion of [[Conditional Expectation]]. To see this is indeed the case observe that
1. $$\int\limits_{\emptyset} \Big( \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} 1_{B} + \frac{\mathbb{E}(1_{B^{C}}X)}{\mathbb{P}(B^{C})} 1_{B^{C}} \Big) d \mathbb{P}(\omega) = 0 = \int\limits_{\emptyset} X d \mathbb{P}(\omega) \text{ }\checkmark$$
2. $$\begin{align*}
\int\limits_{B} \Big( \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} 1_{B} + \frac{\mathbb{E}(1_{B^{C}}X)}{\mathbb{P}(B^{C})} 1_{B^{C}} \Big) d \mathbb{P}(\omega) &= \int\limits \Big( \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} 1_{B} 1_{B} + \frac{\mathbb{E}(1_{B^{C}}X)}{\mathbb{P}(B^{C})} 1_{B^{C}}  1_{B} \Big) d \mathbb{P}(\omega)\\\\
&= \int\limits \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} 1_{B} d \mathbb{P}(\omega)\\
&= \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} \mathbb{P}(B)\\
&=\mathbb{E}(1_{B}X)\\
&=\int\limits_{B} X d \mathbb{P}(\omega) \checkmark
\end{align*}$$
3. $B^{C}$ works almost exactly the same as $B$.
4. $$\begin{align*}
\int\limits_{\Omega} \Big( \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} 1_{B} + \frac{\mathbb{E}(1_{B^{C}}X)}{\mathbb{P}(B^{C})} 1_{B^{C}} \Big) d \mathbb{P}(\omega) &= \int\limits_{B} \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)} d \mathbb{P}(\omega) + \int\limits_{B^{C}} \frac{\mathbb{E}(1_{B^{C}}X)}{\mathbb{P}(B^{C})} d \mathbb{P}(\omega) \\
&=\int\limits_{B} X d \mathbb{P}(\omega) + \int\limits_{B^{C}} X d \mathbb{P}(\omega) &\text{by (2) and (3)}\\
&= \int\limits_{\Omega} X d \mathbb{P}(\omega) \checkmark
\end{align*}$$

Therefore our candidate for $\mathbb{E}(X|1_{B})$ is indeed the [[Conditional Expectation]] and we have (with $\omega \in B$)
$$\mathbb{E}(X|B) = \mathbb{E}(X|1_{B})(\omega) = \frac{\mathbb{E}(1_{B}X)}{\mathbb{P}(B)}$$
$\blacksquare$

# Other Outlinks
- [[Sigma Algebra induced by an Indicator Function]]
- [[Integration of Simple Functions]]
- [[Integration is Linear]]