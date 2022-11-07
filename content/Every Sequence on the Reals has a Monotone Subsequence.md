---
title: "Every Sequence on the Reals contains a Monotone Subsequence"
---

# Statement
Let $(a_{n}) \subset \mathbb{R}$ be a [[Sequence]]. Then there exists a [[Subsequence]] $(a_{n_{k}})$ that is [[Monotone Sequence|monotone]].

## Proof 1
Consider the [[Complete Graph]] on $\mathbb{N}$, $K_{\mathbb{N}}$. Each edge is a pair $\{i, j\} \in \mathbb{N}^{2}$.  As a convention, when we write edge $\{i, j\}$, we will write it with $i < j$. Now color each edge $\{i,j\}$ RED if $a_{i}< a_{j}$ and BLUE if $a_{i} \geq a_{j}$.

Denote $A_{1}$ to be an [[Infinite Set|infinite]] subset of $\mathbb{N} \setminus \{1\}$ so the edges $\{1, j\}$ for $j \in A_{1}$ are [[Monochromatic]], letting $i_{1}=1$. This is possible by [[Infinite Pigeonhole]]. Now set $i_{2} = \min(A_{1})$. Since $A_{1} \cap (\mathbb{N} \setminus [i_{2}])$ is infinite, by [[Infinite Pigeonhole]] there exists $A_{2} \subset A_{1} \cap (\mathbb{N} \setminus [i_{2}])$ s.t. the edges $\{i_{2}, j\}$ for $j \in A_{2}$ are monochromatic. Continue in this way to get a non-increasing sequence of sets $A_{1} \supset A_{2} \supset \cdots$ along with a sequence of indicies $(i_{k})$ s.t. $i_{k} \in A_{k-1}$ $\forall k > 1$.

Now examine $(i_{k})$. For each $k \in \mathbb{N}$ there exists a color $c_{k} \in \{\text{RED}, \text{BLUE}\}$ so that $\{i_{k}, i_{j}\}$ is colored $c_{k}$ $\forall j > k$. Thus we get a corresponding sequence $(c_{k}) \in \{\text{RED}, \text{BLUE}\}^{\mathbb{N}}$. By [[Infinite Pigeonhole]], there exists a single-valued subsequence $(c_{k_{j}})$. Observe that 
1. If this subsequence is RED, then every $\{i_{k_{j_{1}}}, i_{k_{j_{2}}}\}$ is RED, so $(a_{i_{k_{j}}})$ forms an increasing sequence.
2. If this subsequence is BLUE, then every $\{i_{k_{j_{1}}}, i_{k_{j_{2}}}\}$ is BLUE, so $(a_{i_{k_{j}}})$ forms a non-increasing sequence.

In either case we have our monotone subsequence. $\blacksquare$

### Remarks
1. This proof is a [[Ramsey Theory]]-like proof. We are pairing finiteness of our labelling with infiniteness of our sequence to show we must contain some particular structure. [[Infinite Pigeonhole]] plays a key role here.
2. This proof will hold for any [[Total Ordering]].

### Credit
[[Andrés E. Caicedo]] - [Answer to Math SE question](https://math.stackexchange.com/a/716484)

## Proof 2
Consider $\{a_{n}\}_{n=1}^{\infty}$. If it has no [[Upper Bound]], then we can let $i_{1} = 1$ and choose $i_{n+1} > i_{n}$ so that $a_{i_{n+1}} \geq a_{i_{n}}$ for $n \in \mathbb{N}$. By construction, this is a [[Monotone Sequence]]. 

Now consider when $\{a_{n}\}_{n=1}^{\infty}$ has an [[Upper Bound]]. Since $\mathbb{R}$ is [[Completeness of the Real Numbers|complete]], we know there exists $M = \sup\limits \{a_{n}\}_{n=1}^{\infty}$. If $M \not\in \{a_n\}_{n=1}^{\infty}$, then letting $i_{1} = 1$, choose $i_{n+1} > i_{n}$ so that $M > a_{i_{n+1}} \geq a_{i_{n}}$ for $n \in \mathbb{N}$. Such an $i_{n+1}$ always exists, otherwise $M = \max\limits(a_{1}, \dots, a_{i_{n}})$ since $a_{i_{n}}$ is an [[Upper Bound]] for $\{a_{k}\}_{k=i_{n}+1}^{\infty}$. By construction, this is a [[Monotone Sequence]]. If $M \in \sup\limits \{a_{n}\}_{n=1}^{\infty}$, let $i_{1} \in \mathbb{N}$ be such that $a_{i_{1}} = M$. Repeat the described procedure in this paragraph on $\{a_{n}\}_{n=i_{1} + 1}^{\infty}$. That is, suppose we have chosen $i_{1}, \dots, i_{n}$ to be s.t. $a_{i_{j+1}} = \sup\limits \{a_{k}\}_{k=i_{j}+1}^{\infty}$ for $j \in [n-1]$. If  $\sup\limits \{a_{k}\}_{k=i_{n} + 1}^{\infty} \not\in \{a_{k}\}_{k=i_{n} + 1}^{\infty}$, then we have a [[Monotone Sequence|monotone subsequence]] of $\{a_{k}\}_{k=i_{1} + 1}^{\infty} \subset \{a_{k}\}_{k=1}^{\infty}$. Otherwise pick $i_{n+1} > i_{n}$ to be such that $a_{i_{n+1}} = \sup\limits \{a_{k}\}_{k=i_{n} + 1}^{\infty}$. If we proceed so that $a_{i_{n}} = \sup\limits \{a_{k}\}_{k=i_{n} + 1}^{\infty}$ for $n \in \mathbb{N}$, then we have a [[Monotone Sequence|monotone]] [[Subsequence]] since
$$\sup\limits \{a_{k}\}_{k=1}^{\infty} \geq  \sup\limits \{a_{k}\}_{k=i_{1}+1}^{\infty} \geq \cdots \geq  \sup\limits \{a_{k}\}_{k=i_{n}+1}^{\infty} \geq \cdots.$$
$\blacksquare$

### Remarks
1. I think this proof should generalize easily to [[Net]]s: [[Every Net on a Total Ordering has a Monotone Subnet]]

# Other Outlinks
- [[Real Numbers]]
- [[Natural Numbers]]

# Encounters
1. [[Pugh - Real Mathematical Analysis]] - Ch 2 exercise, unknown number
2. [Math SE Question](https://math.stackexchange.com/questions/716461/proof-verification-every-sequence-in-bbb-r-contains-a-monotone-sub-sequence)
