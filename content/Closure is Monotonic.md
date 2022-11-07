---

title: "Closure is Monotonic"

---
# Statement
Let $X$ be a [[Topological Space]]. Suppose $A \subset B \subset X$. Then $\text{cl} A \subset \text{cl} B$.

## Proof
[[Limit Points of a subset are Limit Points of the original Set]] so [[Limit Point]]s of $A$ are [[Limit Point]]s of $B$. Since [[Closure of a Set is all its Limit Points]], 
$$\text{cl} A = \{x \in X : x \text{ is a limit point of } A\} \subset \{x \in X : x \text{ is a limit point of } B\} = \text{cl} B.$$
$\blacksquare$

## Remarks
1. If $B$ is [[Closed]], then $\text{cl} A \subset \text{cl} B = B$ so $\text{cl} A \subset B$.