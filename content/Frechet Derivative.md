---
title: "Frechet Derivative"
---

# Definition
Suppose $V, W$ are [[Normed Vector Space]]s and $f: V \to W$. Suppose for $v \in V$ there exists $T \in BL(V, W)$ s.t.

$$\lim\limits_{h \to 0} \frac{|f(v + h) - f(v) - Th|_{W}}{|h|_{V}} = 0$$

Then we say $f$ has [[Frechet Derivative]] $D_{v} f =T$.

## Properties
### Continuity of $f$
#### Statement
If $D_{v} f$ exists for $v \in V$, then $f$ is [[Continuous Function]] at $v$. [[TODO]]
#### Proof
Existence of the [[Frechet Derivative]] means
$$\begin{align*}
&&\lim\limits_{h \to 0} \frac{|f(v + h) - f(v) - Th|_{W}}{|h|_{V}} = 0\\
&\Rightarrow& 0 = \lim\limits_{h \to 0} \Big| \big( f(v + h) - f(v) - Th\big) - \mathbf{0}_{W} \Big|_{W}\\
\end{align*}$$
By definition of [[Function Limit]], we have that
$$\begin{align*}
&\lim\limits_{h \to 0} \big( f(v + h) - f(v) - Th\big) = \mathbf{0}_{W}\\
&\Rightarrow \lim\limits_{h \to 0} \big( f(v + h) - f(v) \big) - \lim\limits_{h \to 0} Th = \mathbf{0}_{W}\\
&\Rightarrow \lim\limits_{h \to 0} \big( f(v + h) - f(v) \big) = \mathbf{0}_{W}
\end{align*}$$
Where the last line follows because [[Bounded Linear Maps are Continuous]] (how to prove this?). The last line is the definition of [[Continuous Function|continuity]] and $f$ is [[Continuous Function]].