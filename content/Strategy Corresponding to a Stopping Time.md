---

title: "Strategy Corresponding to a Stopping Time"

---
# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] and let $(\mathcal{F}_{n})_{n=0}^{\infty}$ be a [[Discrete-Time Filtration]] on $\mathcal{B}$. Let $\nu$ be a [[Stopping Time]] on $(\mathcal{F}_{n})_{n=0}^{\infty}$. Then $(H_{n} := \mathbb{1}_{\nu \geq n})_{n=1}^{\infty}$ is a [[Predictable Sequence]]. Therefore, $(H_{n})$ defines a [[Strategy]] for a $(\mathcal{F}_{n})_{n=0}^{\infty}$-[[Adapted Process]].

## Proof
This follows because $[\nu \geq n] = [\nu > n-1] \in \mathcal{F}_{n-1}$ by [[Equivalent Conditions for being a Stopping Time|equivalent condition]] (3). Since [[Indicators are Measureable iff their Set is Measureable]], we have that $H_{n} \in \mathcal{F}_{n-1}$ and is [[Predictable Sequence|predictable]]. $\blacksquare$