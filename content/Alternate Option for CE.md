---

title: "Alternate Option for CE"

---
Consider the following setup:

1. [[Probability Space]] $(\Omega, \mathcal{F}, \mathbb{P})$ 
2. [[Random Variable]] $U: \Omega \to \{0, 1\}^{k}$ with [[Uniform Distribution]].
3. Measureable Functions 
	1. Encoder $f: \{0, 1\}^{k} \to \{0,1\}^{n}$
	2. Noise Function $q: \{0,1\}^{n} \times \Omega \to \mathbb{R}^{n}$ 
	3. Likelihood Function $l: \mathbb{R}^{n} \to [0,1]^{k}$. That is $l(\mathbf{y})_{i} = \mathbb{P}(U_{i} = 1|Y=\mathbf{y})$.
	4. Generic soft decoder $g: [n] \to [0,1]^{k}$. $g$ returns a vector of [[Probability Mass Function]]s on $\{0, 1\}$.
	%%5. Hard thresholder $h: [0,1]^{k} \to \{0, 1\}^{k}$, where $h(x)_{i} = \begin{cases} 1 &\text{if }x_{i} \geq 0.5\\ 0 &\text{otherwise} \end{cases}$%%
4. Denote [[Random Variable]]s
	1. $X = f \circ U$. This is the encoded value.
	2. $Y(\omega) = q(X(\omega), \omega)$. This is the noisy value
	3. $L = l \circ Y$. This a random variable of the likelihood for $U_{i}=1$ conditioned on $Y$.
	4. $R = g \circ Y$. This is a random variable of the soft decoded value conditioned on $Y$.
	6.  $\hat{U} \sim (\{0, 1\}^{k}, L)$. This is a random variable representing a decoded value sampled from the likelihood.
	7. $\hat{V}  \sim (\{0, 1\}^{k}, L)$. This is a random variable representing a decoded value sampled using the soft decoded value.

Recall the following definitions

> **Definition 1**: The [[Block Error Rate]] of an encoder $f$, soft decoder $g$ given some noise model $q$ is 
> $$BLER(f, g|q) = \mathbb{E}\big[ 1_{\hat{V} \neq U} \big]$$

> **Definition 2**: The [[Bit Error Rate]] of an encoder $f$, soft decoder $g$ given some noise model $q$ is 
> $$BER(f, g|q) = \mathbb{E}\big[ \frac{1}{k} \sum\limits_{i=1}^{k} 1_{\hat{V}_{i} \neq U_{i}} \big]$$

> **Definition 3**: The [[Binary Cross-Entropy]] of an encoder $f$, soft decoder $g$ given some noise model $q$ is
> $$BCE(f, g|q) = \mathbb{E}\Big[-\frac{1}{k} \sum\limits_{i=1}^{k} 1_{U_{i} = 1} \log g(Y)_{i} + 1_{U_{i} = 0} \log (1 - g(Y)_{i}) \Big]$$


Let $r(u) = \mathbb{E}(g(Y)|U=u)$. Then

> **Definition 3**: The *Modified BCE* of an encoder $f$, soft decoder $g$ given some noise model $q$ is
> $$BCE'(f, g|q) = \mathbb{E}\Big[-\frac{1}{k} \sum\limits_{i=1}^{k} 1_{U_{i} = 1} \log r(U)_{i} + 1_{U_{i} = 0} \log (1- r(U)_{i}) \Big]$$

Recall that we can write
$$\begin{align*}
BER(f, g|q) &= \mathbb{E}\big[ \frac{1}{k} \sum\limits_{i=1}^{k} 1_{\hat{V}_{i} \neq U_{i}} \big]\\
&=\mathbb{E}\big[ \frac{1}{k} \sum\limits_{i=1}^{k} 1_{U_{i} = 1}1_{\hat{V}_{i}=0} + 1_{U_{i} = 0}1_{\hat{V}_{i}=1} \big]\\
&=\mathbb{E}\Bigg[ \frac{1}{k} \sum\limits_{i=1}^{k} 1_{U_{i} = 1} \mathbb{E}(1_{\hat{V}_{i}=0}|U) + 1_{U_{i} = 0}\mathbb{E}(1_{\hat{V}_{i}=1}|U) \Bigg]\\
&=\mathbb{E}\Bigg[ \frac{1}{k} \sum\limits_{i=1}^{k} 1_{U_{i} = 1} \mathbb{E}(\mathbb{E}(1_{\hat{V}_{i}=0}|Y)|U) + 1_{U_{i} = 0}\mathbb{E}(\mathbb{E}(1_{\hat{V}_{i}=1}|Y)|U) \Bigg]\\
&=\mathbb{E}\Bigg[ \frac{1}{k} \sum\limits_{i=1}^{k} 1_{U_{i} = 1} \mathbb{E}(1 - g(Y)_{i}|U) + 1_{U_{i} = 0}\mathbb{E}(g(Y)_{i}|U) \Bigg]\\
&=\mathbb{E}\Bigg[ \frac{1}{k} \sum\limits_{i=1}^{k} 1_{U_{i} = 1} \mathbb{E}(1 - g(Y)_{i}|U) + 1_{U_{i} = 0}\mathbb{E}(g(Y)_{i}|U) \Bigg]\\
&=\mathbb{E}\Bigg[ \frac{1}{k} \sum\limits_{i=1}^{k} 1_{U_{i} = 1} (1 - r(U)_{i}) + 1_{U_{i} = 0}r(U)_{i} \Bigg]\\
\end{align*}$$

[[TODO]]: Prove this: Recall that [[Random Bayes Classifier minimizes Risk|random bayes classifer]] minimizes $BER$ and that $l$ induces [[Random Bayes Classifer]]. So choosing $g=l$ minimizes $BER$. [[TODO]] (does choosing $g = l$...

No the issue is that we also have to choose the [[Coding Encoder]]. I don't think these are the same because it is susceptible to the same issue as with [[Counterexample showing that optimizing BLER is not the same as optimization CE]]. The cost functions weight $[0,1]$ differently and the sum will allow me to take advantage of this.

First note that $g(Y) = \omega \mapsto g(q(f(U(\omega)), \omega))$, so given $U=u$, we get $r(u) = \mathbb{E}[\omega \mapsto g(q(f(u), \omega))]$z. Letting 