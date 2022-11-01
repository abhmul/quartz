---
title: "A set is Closed iff it contains all its Limit Points"
---

# Statement
Suppose $(X, \tau)$ is a [[Topological Space]]. Then $K \subset X$ is [[Closed]] [[If and Only If]] $\bar{K} \subset K$. That is, $K$ is [[Closed]] [[If and Only If]] for all $x \in X$ [[Limit Point]] of $K$, $x \in K$.

## Proof
$(\Rightarrow)$ Since $K$ is [[Closed]] and [[A Set is Closed iff it is its own Closure]], $\text{cl} K = K$. We also know that $\bar{K} = \text{cl} K$. So $\bar{K} = K$ and thus $\bar{K} \subset K$. $\checkmark$

$(\Leftarrow)$ Suppose $\bar{K} \subset K$. Recall [[All points in a Set are Limit Points]], so $K \subset \bar{K}$. Thus $\bar{K} = K$. Since $\bar{K} = \text{cl} K$ and $\text{cl} K$ is [[Closed]], we have that $K = \text{cl} K$ is [[Closed]]. $\checkmark$ $\blacksquare$

$\blacksquare$

## Remark
1. This seems like a trivial result, but I anticipate using it occasionally. It's easier to reference this result than repeat the line of reasoning in the proof everytime

# Other Outlinks
- [[Closure]]
- [[Limit Point]]
- [[A Set is Closed iff it is its own Closure]]
- [[Closure of a Set is all its Limit Points]]