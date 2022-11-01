---

title: "Upcrossing Inequality"

---
# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]]. Let $(X_{n})_{n \geq 1}$ be a [[Discrete-Time Process|discrete-time]] [[Submartingale]] wrt [[Discrete-Time Filtration]] $\mathcal{F}_{*} := (\mathcal{F}_{n} \subset \mathcal{B})_{n \in \mathbb{N}}$. Then $\forall a < b \in \mathbb{R}$, 
$$(b-a)\mathbb{E}(U_{n}[a,b]) \leq \mathbb{E}(X_{n} - a)^{+} - \mathbb{E}(X_{1} - a)^{+}$$
## Proof
Let $(H_{n})_{n \geq 1}$ be the [[Upcrossing Strategy]] for $(X_{n})_{n \geq 1}$.

We let $Y_{n} = a + (X_{n} - a)^{+}$ for $n \geq 1$. Because of [[Submartingale Relations from Jensen]] and convexity of $(\cdot)^{+}$, we have that $(Y_{n})_{n \geq 1}$ is a [[Submartingale]]. The only difference between $X_{n}$ and $Y_{n}$ is that $Y_{n} = a$ when $X_{n} \leq a$ for all $n \geq 1$. Therefore $(Y_{n})_{n \geq 1}$ has a the same number of [[Complete Upcrossings]] as $(X_{n})_{n \in \mathbb{N}}$. Since $(Y_{n})_{n \geq 1}$ cannot dip below $a$, we have that
$$(b-a)U_{n}[a,b] \leq (H \cdot Y)_{n} = \sum\limits_{m=1}^{n} H_{m}(Y_{m} - Y_{m-1})$$
with $Y_{0} = 0$ as in the definition of [[Strategy|winnings]], since $H_{n} = 1$ [[If and Only If]] $Y_{n}$ is rising up to $b$ after a fall from above $b$ down to $a$ for $n \geq 2$. That is, we will include a $(b-a)$ for each upcrossing in the sum along with any extra that comes from breaking above $b$ and any remaining incomplete upcrossing. Furthermore, for $n \geq 1$
$$Y_{n} = \sum\limits_{m=1}^{n} Y_{m} - Y_{m-1} = \sum\limits_{m=1}^{n} (H_{m} - (1 - H_{m}))(Y_{m} - Y_{m-1}) = (H \cdot Y)_{n} + ((1-H) \cdot Y)_{n}$$
denote $K := 1-H$. Thus, $\mathbb{E}(Y_{n})= \mathbb{E}((H \cdot Y)_{n}) + \mathbb{E}((K \cdot Y)_{n})$. Since $K$ is just another [[Strategy]], [[Nonnegative Bounded Strategy on Submartingale is a Submartingale]] tells us that $((K \cdot Y)_{n})_{n \geq 1}$ is another [[Submartingale]]. Then, we have that $\mathbb{E}((K \cdot Y)_{n}) \geq \mathbb{E}((K \cdot Y)_{1})$ since [[Submartingales have Non-Decreasing Expectation]].  Note that $H_{1} = 0$ since all $N_{2k-1} \geq 1$ for $k \geq 1$. Thus 
$$(K \cdot Y)_{1} = Y_{1} - Y_{0} = Y_{1}.$$
Therefore, $\mathbb{E}(Y_{n}) - \mathbb{E}(Y_{1}) \geq \mathbb{E}(H \cdot Y)_{n}$. Putting it together with above, we get
$$(b-a)\mathbb{E}(U_{n}[a,b]) \leq \mathbb{E}((H \cdot Y)_{n}) \leq \mathbb{E}(Y_{n}) - \mathbb{E}(Y_{1})$$
Substituting our original expression for $Y_{n}$,
$$(b-a)\mathbb{E}(U_{n}[a,b]) \leq a + \mathbb{E}(X_{n} - a)^{+} - a - \mathbb{E}(X_{1} - a)^{+} = \mathbb{E}(X_{n} - a)^{+} - \mathbb{E}(X_{1} - a)^{+}$$
$\blacksquare$