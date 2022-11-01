---
title: "Continuous Functions are Determined on Dense Sets"
---

# Statement
Suppose $(X, \tau)$, $(Y, \rho)$  are [[Topological Space]]s, $Y$ is [[Hausdorff|Hausdorff]], and $f: X \to Y$, $g: X \to Y$ are [[Continuous Function|continuous functions]]. Suppose $D \subset X$ is [[Dense]] in $X$. If $$g {\big|}_{D} = f {\big|}_{D}$$ we have that $g = f$.

## Proof
First observe that since $D$ is [[Dense]] its [[Closure]] is $X$. Because [[Closure of a Set is all its Net Limits]], so for every $x \in X$, there exists a [[Net]] $(x_{\alpha})_{\alpha \in A} \subset D$ so that $x_{\alpha} \to x$. Recall that [[A Function is Continuous iff it preserves Net Convergence]], so $f(x_{\alpha}) \to f(x)$ and $g(x_{\alpha}) \to g(x)$. [[Net Limits are unique in Hausdorff Spaces]] so, because $f(x_{\alpha}) = g(x_{\alpha})$ for all $\alpha \in A$, we must have that $f(x) = g(x)$. $x \in X$ was arbitrary so $f = g$. $\blacksquare$

## Remarks
1. This is not true in general. Suppose $X=\{1, 2, 3\}$ is equipped with the [[Indiscrete Topology]]. Suppose $f = \text{id}_{X}$ and $g: X \to X$ s.t. $$g(x) = \begin{cases} 1 & \text{if } x = 1\\ 3 & \text{if } x = 2\\ 2 & \text{if } x = 3\\ \end{cases}$$ Then $f$ is [[Continuous Function]] since [[Identity Functions are Continuous]]. $g$ is continuous since [[All Surjective Functions to the Indiscrete Topology are Continous]]. [[All Nonempty Subsets of the Indiscrete Topology are Dense]], so $\{1\}$ is [[Dense]]. We see $g(1) = f(1)$, but $g(2) = 3 \neq 2 = f(2)$. $\blacksquare$
2. Since [[Metric Spaces are First Countable and Hausdorff]], [[Continuous Function|continuous functions]] between [[Metric Space]]s are determined on a [[Dense|dense set]].