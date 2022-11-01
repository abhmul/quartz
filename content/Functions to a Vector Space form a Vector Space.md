# Statement
Let $S$ be a [[Set]] and $V$ some [[Vector Space]] over [[Field]] $F$. Then $\mathcal{F} = \{f : S \to V\}$ is a [[Vector Space]] with
- $(f +_\mathcal{F} g)(x) = f(x) +_V g(x)$ for $x \in S$, $f,g \in \mathcal{F}$.
- $(c *_\mathcal{F} f)(x) = c *_{V} f(x)$ for $x \in S$, $c \in F$, $f \in \mathcal{F}$.
## Proof
We verify the definition of a [[Vector Space]]. Let $\mathbf{0}(x) = 0$ for all $x \in S$.
1. [[Abelian Group]]:
	1. $(\mathbf{0} +_\mathcal{F} f)(x) = 0 +_{V} f(x) = f(x)$ for $x \in S$. $\checkmark$
	2. Let $f, g, h \in \mathcal{F}$. Then $$\begin{align*}
	((f+_\mathcal{F} g) +_\mathcal{F} h)(x) &= (f +_\mathcal{F} g)(x) +_{V} h(x) \\
	&= f(x) +_{V} g(x) +_{V} h(x) \\
	&= f(x) +_{V} (g +_\mathcal{F} h)(x) \\
	&= (f +_\mathcal{F} (g +_\mathcal{F} h))(x).
	\end{align*}$$ $\checkmark$
	3. Let $f, g \in \mathcal{F}$. Then $$\begin{align*}
	(f +_\mathcal{F} g)(x) &= f(x) +_{V} g(x) \\
	&= g(x) +_{V} f(x) \\
	&= (g +_\mathcal{F} f)(x)
	\end{align*}$$ for $x \in S$. $\checkmark$
	4. Let $f \in \mathcal{F}$. Then $$\begin{align*}
	(f +_\mathcal{F} (-f))(x) &= f(x) -_{V} f(x) \\
	&= 0 \\
	&= \mathbf{0}(x)
	\end{align*}$$ for $x \in S$. $\checkmark$
1. Compatibility with [[Scalar Multiplication]], $f, g \in \mathcal{F}$:
	1. $(1*_\mathcal{F} f)(x) = 1 *_{V} f(x) = f(x)$ for $x \in S$. $\checkmark$
	2. $c_{1}, c_{2} \in F$ then $$\begin{align*}
	((c_{1} *_F c_{2}) *_\mathcal{F} f)(x) &= (c_{1}*_{F} c_{2}) *_{V}f(x) \\
	&= c_{1}*_{V}(c_{2} *_{V} f(x))\\
	&= c_{1}*_{V}(c_{2} *_\mathcal{F}f)(x) \\
	&= (c_{1} *_\mathcal{F} (c_{2} *_\mathcal{F} f))(x)
	\end{align*}$$ for $x \in S$. $\checkmark$
	3. $c \in F$, then $$\begin{align*}
	(c *_\mathcal{F} (f +_\mathcal{F} g))(x) &= c *_{V}(f+_\mathcal{F} g)(x)\\
	&=c *_{V}(f(x)+_{V} g(x)) \\
	&= c *_{V} f(x) +_{V} c *_{V}g(x) \\
	&= (c *_\mathcal{F} f)(x) +_{V} (c *_\mathcal{F} g)(x)\\
	&= (c *_\mathcal{F} f +_\mathcal{F} c *_\mathcal{F} g)(x)
	\end{align*}$$ for $x \in S$. $\checkmark$
	4. $c, d \in F$, then $$\begin{align*}
	((c +_{F} d) *_\mathcal{F} f)(x) &= (c +_{F} d) *_{V} f(x) \\
	&= c *_{V} f(x) +_{V} d *_{V} f(x)\\
	&= (c *_{\mathcal{F}} f)(x) +_{V} (d *_{\mathcal{F}} f)(x) \\
	&= (c *_\mathcal{F} f +_\mathcal{F} d *_\mathcal{F} f)(x)
	\end{align*}$$ for $x  \in S$. $\checkmark$

$\blacksquare$ 
