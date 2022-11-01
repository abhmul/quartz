---
title: "Field"
---

# Definition
Suppose $X$ is a [[Nonempty]] [[Set]], and $+: X \times X \to X$, $*: X \times X \to X$ are two [[Operation]]s on $X$. Then $(X, +, *)$ is a [[Field]] if it satisfies the following properties:
1. [[Additive Identity]]: There exists $0 \in X$ so that for all $x \in X$, $0 + x = x$.
2. [[Associativity]] of $+$: For all $x,y,z \in X$, $(x + y) + z = x + (y + z)$
3. [[Commutativity]] of $+$: For all $x, y \in X$, $x + y = y + x$ 
4. [[Additive Inverse]]s: If $x \in X$, then there exists $-x \in X$ so that $x + (-x) = 0$
5. [[Multiplicative Identity]]: There exists $1 \in X$ so that for all $x \in X$, $1 * x = x$
6. [[Associativity]] of $*$: For all $x,y,z \in X$, $(x * y) * z = x * (y * z)$
7. [[Commutativity]] of $*$: For all $x, y \in X$, $x * y = y * x$
8. [[Multiplicative Inverse]]s: If $x \in X$ and $x \neq 0$, then there exists $x^{-1} \in X$ so that $x * x^{-1} = 1$
9. [[Distributivity]] of $*$ over $+$: For all $x, y, z \in X$, $x(y + z) = x*y + x*z$ 

## Remarks
1. In other words, a [[Field]] is a [[Commutative Ring]] with [[Multiplicative Inverse]]s. Thus, a [[Field]] carries with it all properties of [[Commutative Ring]]s and its subclasses (like [[Group]]s).