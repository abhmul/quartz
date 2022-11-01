---

title: "Language"

---
# Definition
A [[Language]] $\mathcal{L}$ is a [[Tuple]] $(\mathcal{F}, \mathcal{R}, \mathcal{C}, n_{\mathcal{R}}, n_{\mathcal{F}})$ where
1. $\mathcal{F}$ is a [[Set]] of [[Function Symbol]]s
2. $\mathcal{R}$ is a [[Set]] of [[Relation Symbol]]s
3. $\mathcal{C}$ is a [[Set]] of [[Constant Symbol]]s
4. $n_\mathcal{R} : \mathcal{R} \to \mathbb{N}$ is a [[Function]] that maps each [[Relation]] [[Symbol]] to it's respective [[Arity]]

## Remarks
1. [[Language]]s do not actually give any meaning to their [[Symbol]]s. This comes from a [[Language Structure]]
2. When we write out a [[Language]], we often omit the [[Tuple]] structure of it and simply write out all symbols in a single [[Set]]. It is usually clear enough which ones are [[Relation Symbol]]s, [[Function Symbol]]s, or [[Constant Symbol]]s.

## Examples
1. [[Language]] of [[Ring]]s: $\mathcal{L}_{R} = \{+, -, \cdot, 0, 1\}$. 
2. [[Language]] of [[Pure Set]]s: $\mathcal{L} = \emptyset$.
	- I think we take it as given that we can maniuplate [[Language]]s in terms of [[Zermelo-Fraenkel Set Theory|set theory]]. In that case, this makes sense, because there is no more data we need to describe [[Pure Set]]s.
3. The [[Language]] of [[Directed Graph]]s: $\mathcal{L} = \{R\}$. Here $R$ is a [[Relation]] that represents the [[Directed Graph]].