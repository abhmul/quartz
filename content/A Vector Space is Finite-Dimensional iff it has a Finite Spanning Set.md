---

title: "A Vector Space is Finite-Dimensional iff it has a Finite Spanning Set"

---
# Statement
Let $V$ be a [[Vector Space]]. Then there is some [[Finite Set|finite]] $S \subset V$ for which $\text{span} S = V$ [[If and Only If]] $V$ is a [[Finite-Dimensional Vector Space]].

## Proof 1
$(\Rightarrow)$ Consider the following construction
1. Start with $R = \emptyset$.
2. At each step, add to $R$ an element from $S$ that is not in $\text{span} R$

At the beginning $R = \emptyset$ and the [[Empty Set]] trivially is [[Linearly Independent]]. By [[Growing a Linearly Independent Set]], if $R$ is [[Linearly Independent]], then each successive step will preserve that. This process must terminate since $|S| < \infty$. When it terminates, we will have $S \subset \text{span} R$, so $\text{span} S \subset \text{span} R$ since [[The Span of subset of a Span is also a subset of that Span]]. But
$$V = \text{span} S \subset \text{span} R \subset V,$$
so we have $\text{span} R = V$ and $R$ is a [[Vector Space Basis]] for $V$. Since $R \subset S$, we have that $|R| \leq |S| < \infty$, so it is a [[Finite Set]]. Therefore $V$ is a [[Finite-Dimensional Vector Space]]. $\checkmark$

$(\Leftarrow)$ If $V$ is [[Finite-Dimensional Vector Space]], then it has a [[Finite Set|finite]] [[Vector Space Basis]]. A [[Vector Space Basis]] is by definition a [[Spanning Set|spanning set]] of $V$. $\checkmark$

$\blacksquare$

## Proof 2 *
$(\Rightarrow)$ If $V$ has a [[Finite Set|finite]] [[Subspace Span|spanning set]], then it has a [[Minimal]] [[Spanning Set]], since we can remove elements one-by-one from $S$ until it is either [[Empty Set|empty]] or it is no longer a [[Spanning Set]]. Call this [[Minimal]] [[Spanning Set]] $R$. Because [[A Set is a Basis iff it is a Minimal Spanning Set]], $R$ must be a [[Vector Space Basis]] for $V$. Since $R \subset S$, we have that $|R| \leq |S| < \infty$, so $V$ has a [[Finite Set|finite]] [[Vector Space Basis]] and is thus [[Finite-Dimensional Vector Space|finite-dimensional]]. $\checkmark$

$(\Leftarrow)$ If $V$ is [[Finite-Dimensional Vector Space|finite-dimensional]], then it has a [[Finite Set|finite]] [[Vector Space Basis]] which is a [[Spanning Set]] by definition. $\checkmark$ $\blacksquare$

## Remarks
1. Related: [[A Vector Space is Infinite-Dimensional iff its Linearly Independent Set Size is Unbounded]]

# Other Outlinks
- [[Subspace Span]]
- [[Natural Numbers are Well-Ordered]]