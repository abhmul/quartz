---

title: "Bijection"

---
# Definition
A [[Function]] that is both an [[Injection]] and a [[Surjection]].

## Properties
1. Every [[Bijection]] $f: X \to Y$ has a [[Function Inverse]]. This is because for each $y \in Y$, there exists $x \in X$ so that $f(x) = y$, since $f$ is a [[Surjection]]. This $x$ is unique because $f$ is an [[Injection]], so we can define $f^{-1}(y) := x$. Then $f \circ f^{-1}(y) = y$ and $f^{-1} \circ f(x) = x$ for all $y \in Y$, $x \in X$.