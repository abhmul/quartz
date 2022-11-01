---
title: "Characteristic Function"
---

# Definition
Suppose $X$ is a [[Random Variable]] on [[Probability Space]] $(\Omega, \mathcal{M}, \mathbb{P})$. The [[Characteristic Function]] of $X$ is a function $\phi_{X}: \mathbb{R} \to \mathbb{C}$ defined as

$$\phi_{X}(t) = \mathbb{E}(e^{itX})$$

## Elementary Properties
1. $X$ is a [[Random Variable]]. $\phi_{X}(t)$ exists from all $t \in \mathbb{R}$. This follows because $|e^{itX}| = 1$. Thus, $\mathbb{E}(|e^{itX}|) = \mathbb{E}(1) = 1$ and $e^{itX} \in L^{1}(\Omega)$.
2. $X, Y$ are [[Independence|Independent]] [[Random Variable]]s. Then
	$$\begin{align*}
\phi_{X+Y}(t) &= \mathbb{E}(e^{it(X+Y)})\\
&=\mathbb{E}(e^{itX} e^{itY})\\
&=\mathbb{E}(e^{itX}) \mathbb{E}(e^{itY}) & \text{(Independence)}\\
&=\phi_{X}(t) \phi_{Y}(t)
\end{align*}$$
3. $X$ is a [[Random Variable]], $a, b \in \mathbb{R}$. Then
	$$\begin{align*}
\phi_{aX+b}(t) &= \mathbb{E}(e^{it(aX+b)})\\\\
&=\mathbb{E}(e^{itaX} e^{itb})\\
&=e^{itb}\mathbb{E}(e^{i(ta)X})\\
&=e^{itb} \phi_{X}(ta)
\end{align*}$$
4. $X$ is a [[Random Variable]]. Applying [[Euler's Formula]]

### Passing the [[Expectation]] into the [[Taylor Expansion of the Exponential]]

$X$ is a [[Random Variable]]. We would like to understand how we can apply the [[Taylor Expansion of the Exponential]] to our definition of a [[Characteristic Function]].
$$\begin{align*}
\phi_{X}(t) &= \mathbb{E}(e^{itX})\\
&=\mathbb{E}\left(1 + \sum\limits_{k=1}^{\infty} \frac{(itX)^{k}}{k!}\right)
\end{align*}$$
where the last equality makes sense because the [[Taylor Expansion of the Exponential has unbounded Radius of Convergence]]. However, it does not necessarily follow that we can "apply" [[Linearity of Expectation]] to the sum. For example, the example from [[Expectation does not always exist]] has characteristic function value for each $t \in \mathbb{R}$ by property (1), but passing the expectation through the [[Taylor Expansion of the Exponential|taylor expansion]] has no clear meaning.

However, with some more assumptions we can say more:

#### Existence of [[Moment Generating Function]]
Suppose $m_{X}(t) = \mathbb{E}(e^{tX})$ exists for some $t > 0$. Observe that 
$$\begin{align*}
e^{|tX|} &= 1 + \sum\limits_{k=1}^{\infty} \frac{|tX|^{k}}{k!} \\
&= 1 + \sum\limits_{k=1}^{\infty} \frac{|itX|^{k}}{k!}\\
&= 1 + \sum\limits_{k=1}^{n} \frac{|itX|^{k}}{k!}\\
&\geq \bigg| 1 + \sum\limits_{k=1}^{n} \frac{(itX)^{k}}{k!} \bigg| \\
\end{align*}$$
[[Existence of Moment Generating Functions imply Existence of Moments]], so [[TODO]].

$$\begin{align*}
&\mathbb{E}(e^{tX} 1_{X \geq 0}) \leq \mathbb{E}(e^{tX})\\
&\mathbb{E}(e^{-tX} 1_{X < 0}) \leq \mathbb{E}(e^{-tX})\\
&\mathbb{E}(e^{tX} 1_{X \geq 0}) + \mathbb{E}(e^{-tX} 1_{X < 0}) = \mathbb{E}(e^{t|X|}) \leq m_{X}(t) + m_{X}(-t)
\end{align*}$$




# Other Outlinks
- [[Complex Numbers]]
- [[Complex Integration]]
- [[Real Numbers]]
- [[L1 Integrable Functions]]
# Encounters
1. [[Resnick - A Probability Path]] - Ch 9
2. [[Revuz - Continuous Martingales and Brownian Motion]]