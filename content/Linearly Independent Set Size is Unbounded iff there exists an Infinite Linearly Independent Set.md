---

title: "Linearly Independent Set Size is Unbounded iff there exists an Infinite Linearly Independent Set"

---
# Statement
Let $V$ be a [[Vector Space]]. Then $\forall n \in \mathbb{N}$ there exists [[Linearly Independent]] $S \subset V$ so that $|S| > n$ [[If and Only If]] there exists [[Linearly Independent]] $R \subset V$ so that $|R| = \infty$.

## Proof
$(\Leftarrow)$ $R$ satisfies the requirement for any $n \in \mathbb{N}$. $\checkmark$

$(\Rightarrow)$ This means $V$ is an [[Infinite-Dimensional Vector Space]] because [[A Vector Space is Infinite-Dimensional iff its Linearly Independent Set Size is Unbounded]]. Therefore, starting from $\emptyset$, the [[Growing a Linearly Independent Set]] process will not terminate, otherwise by [[A Set is a Basis iff it is a Maximal Linearly Independent Set]], we would exhibit a [[Finite Set|finite]] [[Vector Space Basis]] and $V$ would be a [[Finite-Dimensional Vector Space]]. Now consider the [[Set]]
$$R = \bigcup\limits_{n \in \mathbb{N}} \{S_{n}\}$$
where $S_{n}$ is the [[Linearly Independent]] set produced by the [[Growing a Linearly Independent Set]] process at step $n \in \mathbb{N}$.  Since the process does not terminate and $|S_{n}| = n$, we have that $|R| = \infty$. We claim that $R$ is [[Linearly Independent]]. 

Suppose $R$ is [[Linearly Dependent]]. Then there is some $m \in \mathbb{N}$, nontrivial $c_{1}, \dots, c_{m} \in F$, distinct $\mathbf{a}_{1}, \dots, \mathbf{a}_{m} \in R$ so that
$$c_{1} \mathbf{a}_{1} + \cdots + c_{m} \mathbf{a}_{m} = \mathbf{0}.$$
But there must be some $N \in \mathbb{N}$ so that all $\mathbf{a}_{1}, \dots, \mathbf{a}_{m} \in S_{N}$. Therefore $S_{N}$ is [[Linearly Dependent]], [[Proof by Contradiction|contradicting]] our assumption that $S_{n}$ are [[Linearly Independent]] for all $n \in \mathbb{N}$. Therefore, $R$ is an [[Infinite Set|infinite]] [[Linearly Independent]] [[Set]]. $\checkmark$ $\blacksquare$

# Other Outlinks
- [[Counting Measure]]
- [[The Empty Set is Linearly Independent]]
- [[Infinite Set]]
- [[Natural Numbers]]