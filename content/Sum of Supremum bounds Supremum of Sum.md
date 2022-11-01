---

title: "Sum of Supremum bounds Supremum of Sum"

---
# Statement 1
Suppose $X$ is a [[Set]] and $(Y, \leq)$ is a [[Bi-Ordered Group]]. Suppose $f: X \to Y$ and $g: X \to Y$. Then 
$$\sup\limits_{x \in X} f(x) \cdot \sup\limits_{x \in X} g(x) \geq \sup\limits_{x \in X} (f(x) \cdot g(x))$$
## Proof
Let $s := \sup\limits_{x \in X} f(x) \cdot \sup\limits_{x \in X} g(x)$. All we must show is that $s \geq f(x) \cdot g(x)$ for all $x \in X$. Suppose $x \in X$. Then, by definition of [[Supremum]], $\sup\limits_{y \in X} f(y) \geq f(x)$ and $\sup\limits_{y \in X}g(y) \geq g(x)$. Thus by [[Basic Properties of Bi-Ordered Groups|Property 1 of Bi-Ordered Groups]] $s = \sup\limits_{y \in X} f(y) \cdot \sup\limits_{y \in X}g(y) \geq f(x) \cdot g(x)$. $\blacksquare$

# Statement 2
Suppose $X$ is a [[Set]] and $(Y, \leq)$ is an [[Ordered Abelian Group]]. Suppose $f: X \to Y$ and $g: X \to Y$. Then 
$$\sup\limits_{x \in X} f(x) + \sup\limits_{x \in X} g(x) \geq \sup\limits_{x \in X} (f(x) + g(x))$$
## Proof
[[Ordered Abelian Groups are Bi-Ordered Groups]]. Apply Statement 1. $\blacksquare$

# Statement 3
Suppose $X$ is a [[Set]]. Suppose $f: X \to \mathbb{R}$ and $g: X \to \mathbb{R}$. Then 
$$\sup\limits_{x \in X} f(x) + \sup\limits_{x \in X} g(x) \geq \sup\limits_{x \in X} (f(x) + g(x))$$
## Proof
[[Reals form an Ordered Abelian Group]]. Apply Statement 2. $\blacksquare$