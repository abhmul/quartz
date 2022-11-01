---
title: "Smoothing"
---

# Statement 1
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $X$ be a [[Random Variable]] on $\Omega$. Suppose $\mathcal{G}_{1} \subset \mathcal{G}_{2} \subset \mathcal{B}$ are sub-[[Sigma Algebra]]s on $\Omega$. Then 

$$\mathbb{E}\big[ \mathbb{E}[X|\mathcal{G}_{2}] | \mathcal{G}_{1} \big] = \mathbb{E}[X| \mathcal{G}_{1}]$$

Recalling that [[Conditional Expectation over the Trivial Sigma Algebra is Expectation]], we see that if $\mathcal{G}_{1}$ is the [[Trivial Sigma Algebra]] on $\Omega$ then

$$\mathbb{E}\big[ \mathbb{E}[X|\mathcal{G}_{2}] | \mathcal{G}_{1} \big] = \mathbb{E}[X| \mathcal{G}_{1}] = \mathbb{E}[X]$$

## Proof
We show that $\mathbb{E}[X| \mathcal{G}_{1}]$ satisfies the properties for [[Conditional Expectation]] of $\mathbb{E}[X|\mathcal{G}_{2}]$ with respect to $\mathcal{G}_{1}$. By definition of [[Conditional Expectation]], we know $\mathbb{E}[X|\mathcal{G}_{1}]$ is $\mathcal{G}_{1}$-[[Measureable Function|measureable]]. Let $A \in \mathcal{G}_{1}$. Then

$$\int\limits_{A} \mathbb{E}[X|\mathcal{G}_{1}] = \int\limits_{A} X = \int\limits_{A} \mathbb{E}[X|\mathcal{G}_{2}]$$

where the first equality follows from the definition of [[Conditional Expectation]] and the second because $A \in \mathcal{G}_{2}$ as well. Thus,

$$\mathbb{E}\big[ \mathbb{E}[X|\mathcal{G}_{2}] | \mathcal{G}_{1} \big] = \mathbb{E}[X| \mathcal{G}_{1}]$$

$\blacksquare$

# Statement 2
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $X$ be a [[Random Variable]] on $\Omega$. Suppose $\mathcal{G}_{1} \subset \mathcal{G}_{2} \subset \mathcal{B}$ are sub-[[Sigma Algebra]]s on $\Omega$. Then 

$$\mathbb{E}\big[ \mathbb{E}[X|\mathcal{G}_{1}] | \mathcal{G}_{2} \big] = \mathbb{E}[X| \mathcal{G}_{1}]$$

## Proof
Since $\mathcal{G}_{1} \subset \mathcal{G}_{2}$ and $\mathbb{E}[X|\mathcal{G}_{1}] \in \mathcal{G}_{1}$, we have that $\mathbb{E}\big[ \mathbb{E}[X|\mathcal{G}_{1}] | \mathcal{G}_{2} \big] = \mathbb{E}[X| \mathcal{G}_{1}]$ because [[Conditioning on known information is Idempotent]]. $\blacksquare$