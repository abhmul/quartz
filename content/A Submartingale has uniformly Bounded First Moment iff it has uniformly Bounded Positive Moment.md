---

title: "A Submartingale has uniformly Bounded First Moment iff it has uniformly Bounded Positive Moment"

---
# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] . Let $(X_{n})_{n \geq 1}$ be a [[Discrete-Time Process|discrete-time]] [[Submartingale]] wrt [[Discrete-Time Filtration]] $\mathcal{F}_{*} := (\mathcal{F}_{n} \subset \mathcal{B})_{n \in \mathbb{N}}$ . Then $\sup\limits_{n \geq 1} \mathbb{E}(X_{n})^{+} < \infty$ [[If and Only If]] $\sup\limits_{n \geq 1} \mathbb{E}|X_{n}| < \infty$.

## Proof
($\Rightarrow$): Because $(X_{n})_{n \geq 1}$ is a [[Submartingale]] and [[Submartingales have Non-Decreasing Expectation]], $\forall n \geq 1$,
$$\begin{align*}
&\mathbb{E}(X_{n}) \geq \mathbb{E}(X_{1})\\
\Rightarrow&\mathbb{E}(X_{n})^{+} - \mathbb{E}(X_{n})^{-} \geq \mathbb{E}(X_{1})\\
\Rightarrow&\mathbb{E}(X_{n})^{+} - \mathbb{E}(X_{1}) \geq \mathbb{E}(X_{n})^{-} \\
\Rightarrow&\infty > \sup\limits_{n \geq 1} \mathbb{E}(X_{n})^{+} - \mathbb{E}(X_{1}) \geq \sup\limits_{n \geq 1} \mathbb{E}(X_{n})^{-}
\end{align*}$$

Thus,
$$
\begin{align*}
\sup\limits_{n \geq 1} \mathbb{E}|X_{n}| &= \sup\limits_{n \geq 1} (\mathbb{E}(X_{n})^{+} + \mathbb{E}(X_{n})^{-})\\
&\leq \sup\limits_{n \geq 1} (\mathbb{E}(X_{n})^{+}) + \sup\limits_{n \geq 1} (\mathbb{E}(X_{n})^{-})\\
&< \infty 
\end{align*}
$$
$\checkmark$

($\Leftarrow$): This follows because
$$\infty > \sup\limits_{n \geq 1} \mathbb{E}|X_{n}| \geq \sup\limits_{n \geq 1} (\mathbb{E}(X_{n})^{+} + \mathbb{E}(X_{n})^{-}) \geq \sup\limits_{n \geq 1} \mathbb{E}(X_{n})^{+}$$
$\checkmark$ $\blacksquare$