---
title: "Every Sequence on the Reals contains a Monotone Subsequence"
---

# Statement
Let $(a_{n}) \subset \mathbb{R}$ be a [[Sequence]]. Then there exists a [[Subsequence]] $(a_{n_{k}})$ that is [[Monotone Function|monotone]].

# Proof 1
Consider the [[Complete Graph]] on $\mathbb{N}$, $K_{\mathbb{N}}$. Each edge is a pair $\{i, j\} \in \mathbb{N}^{2}$.  As a convention, when we write edge $\{i, j\}$, we will write it with $i < j$. Now color each edge $\{i,j\}$ RED if $a_{i}< a_{j}$ and BLUE if $a_{i} \geq a_{j}$.

Denote $A_{1}$ to be an [[Infinite Set|infinite]] subset of $\mathbb{N} \setminus \{1\}$ so the edges $\{1, j\}$ for $j \in A_{1}$ are [[Monochromatic]], letting $i_{1}=1$. This is possible by [[Infinite Pigeonhole]]. Now set $i_{2} = \min(A_{1})$. Since $A_{1} \cap (\mathbb{N} \setminus \{1,2\})$ is infinite, by [[Infinite Pigeonhole]] there exists $A_{2} \subset A_{1} \cap (\mathbb{N} \setminus [i_{2}])$ s.t. the edges $\{i_{2}, j\}$ for $j \in A_{2}$ are monochromatic. Continue in this way to get a non-increasing sequence of sets $A_{1} \supset A_{2} \supset \cdots$ along with a sequence of indicies $(i_{k})$ s.t. $i_{k} \in A_{k-1}$ $\forall k > 1$.

Now examine $(i_{k})$. For each $k \in \mathbb{N}$ there exists a color $c_{k} \in \{\text{RED}, \text{BLUE}\}$ so that $\{i_{k}, i_{j}\}$ is colored $c_{k}$ $\forall j > k$. Thus we get a corresponding sequence $(c_{k}) \in \{\text{RED}, \text{BLUE}\}^{\mathbb{N}}$. By [[Infinite Pigeonhole]], there exists a single-valued subsequence $(c_{k_{j}})$. Observe that 
1. If this subsequence is RED, then every $\{i_{k_{j_{1}}}, i_{k_{j_{2}}}\}$ is RED, so $(a_{i_{k_{j}}})$ forms an increasing sequence.
2. If this subsequence is BLUE, then every $\{i_{k_{j_{1}}}, i_{k_{j_{2}}}\}$ is BLUE, so $(a_{i_{k_{j}}})$ forms a non-increasing sequence.

In either case we have our monotone subsequence. $\blacksquare$

## Remarks
1. This proof is a [[Ramsey Theory]]-like proof. We are pairing finiteness of our labelling with infiniteness of our sequence to show we must contain some particular structure. [[Infinite Pigeonhole]] plays a key role here.
2. This proof will hold for any [[Total Ordering]].

## Credit
[[Andrés E. Caicedo]] - [Answer to Math SE question](https://math.stackexchange.com/a/716484)

# Other Outlinks
- [[Real Numbers]]
- [[Natural Numbers]]

# Encounters
1. [[Pugh - Real Mathematical Analysis]] - Ch 2 exercise, unknown number
2. [Math SE Question](https://math.stackexchange.com/questions/716461/proof-verification-every-sequence-in-bbb-r-contains-a-monotone-sub-sequence)
