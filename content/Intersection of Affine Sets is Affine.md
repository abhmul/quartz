---
title: "Intersection of Affine Sets is Affine"
---

# Statement
Let $V$  be a [[Vector Space]] on $\mathbb{R}$ and let $\mathcal{S} \subset \mathcal{P}(V)$ be a [[Set|collection]] of [[Affine Set]]s. Then $\bigcap\limits_{S \in \mathcal{S}}S$ is a [[Affine Set]].

## Proof 1
Let $T = \bigcap\limits_{S \in \mathcal{S}}S$ and let $u, v \in T$. Suppose $\lambda \in \mathbb{R}$. Then $\forall S \in \mathcal{S}$, we have that $\lambda u + (1 - \lambda) v \in S$. Thus $\lambda u + (1 - \lambda) v \in T$ and $T$ is a [[Affine Set]]. $\blacksquare$

## Proof 2
[[Intersection of Structures is still a Structure]]