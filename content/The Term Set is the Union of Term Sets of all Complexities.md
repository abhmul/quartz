---

title: "The Term Set is the Union of Term Sets of all Complexities"

---
# Statement
Let $\mathcal{L}$ be a [[Language]] and let $\mathcal{T}$ be the [[Set]] of $\mathcal{L}$-[[Term]]s. Let $\mathcal{T}_{0} := \mathcal{C} \cup \{v_{i} : i \in \mathbb{N}\}$ and inductively define
$$\mathcal{T}_{n+1} := \mathcal{T}_{n} \cup \{f(t_{1}, \dots, t_{n_{f}}) : t_{1}, \dots \in \mathcal{T}_{n}, f \in \mathcal{F}\}$$
We refer to $\mathcal{T}_{n}$ as the [[Term]] set of [[Logical Complexity]] $n$. Then
$$\mathcal{T} = \bigcup\limits_{n=1}^{\infty} \mathcal{T}_{n}$$
## Proof
We have not fully established the existence of $\mathcal{T}$ yet. However, simply a showing a [[Set]] exists with the desired properties establishes that the "smallest" such [[Set]] exists by application of [[Set Intersection]] to the [[Set|collection]] of all subsets that also satisfy our desired property.
$(\subset)$: Denote $\mathcal{T}' := \bigcup\limits_{n=1}^{\infty} \mathcal{T}_{n}$. We will show that $\mathcal{T}'$ satisfies all the properties of a [[Term|Term set]]. Observe
1. $\mathcal{C} \subset \mathcal{T}_{0} \subset \mathcal{T}'$.
2. $\{v_{i} : i \in \mathbb{N}\} \subset \mathcal{T}_{0} \subset \mathcal{T}'$
3. Suppose $f \in \mathcal{F}$ and $t_{1}, \dots, t_{n_{f}} \in \mathcal{T}'$. This means, each $i \in [n_{f}]$, there is a $j_{i} \in \mathbb{N}$ so that  $t_{i} \in \mathcal{T}_{j_{i}}$. Since $n_{f}$ is [[Finite Set|finite]], there exists a $m \in \mathbb{N}$ so that $m = \max\limits_{i \in [n_{f}]} \mathcal{T}_{j_{i}} + 1$, and thus $\mathcal{T}_{m-1} \supset \mathcal{T}_{j_{i}}$ for each $i \in [n_{f}]$. Then, by definition of $\mathcal{T}_{m-1}$, since $t_{1}, \dots, t_{n_{f}} \in \mathcal{T}_{m-1}$, we have that $f(t_{1}, \dots, t_{n_{f}}) \in \mathcal{T}_{m} \subset \mathcal{T}'$.

Since $\mathcal{T}$ is the smallest such set that satisfies this property, this means $\mathcal{T} \subset \mathcal{T}'$

$(\supset)$: We will show by [[Induction]] that we must have $\mathcal{T} \supset \mathcal{T}_{n}$ for each $n \in \mathbb{N}$. First observe that by definition $\mathcal{T} \supset \mathcal{T}_{0}$. Now suppsoe $\mathcal{T} \supset \mathcal{T}_{n}$ for some $n \in \mathbb{N}$. Then, for $f \in \mathcal{F}$ and $t_{1}, \dots, t_{n_{f}} \in \mathcal{T}_{n} \subset \mathcal{T}$, we have that $f(t_{1}, \dots, t_{n_{f}}) \in \mathcal{T}$, so $\mathcal{T}_{n+1} \subset \mathcal{T}$. Since for each $n \in \mathbb{N}$, $\mathcal{T} \supset \mathcal{T}_{n}$, we have that $\mathcal{T} \supset \bigcup\limits_{n=1}^{\infty} \mathcal{T}_{n} = \mathcal{T}'$.
Thus $\mathcal{T} = \mathcal{T}'$. $\blacksquare$

## Remarks
1. This theorem is most useful when we want to establish that $\mathcal{L}$-[[Term]]s have some property. We can apply [[Induction on Complexity]] by showing that the property inductively holds for all $\mathcal{T}_{n}$ for $n \in \mathbb{N}$. Since each $t \in \bigcup\limits_{n=1}^{\infty}\mathcal{T}_{n}$ belongs to some $\mathcal{T}_{n}$, we have the property holds for $\mathcal{T} = \bigcup\limits_{n=1}^{\infty} \mathcal{T}_{n}$.