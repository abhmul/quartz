---

title: "Upcrossing Strategy"

---
# Statement
Let $(\Omega, \mathcal{B}, \mathbb{P})$ be a [[Probability Space]] . Let $(X_{n})_{n \geq 1}$ be a [[Discrete-Time Process|discrete-time]] [[Adapted Process]] wrt [[Discrete-Time Filtration]] $\mathcal{F}_{*} := (\mathcal{F}_{n} \subset \mathcal{B})_{n \in \mathbb{N}}$. Let
$$H_{n} := \begin{cases} 
1 & \text{if } \exists k \geq 1 \text{ s.t. } N_{2k-1} < n \leq N_{2k} \\
0  & \text{otherwise}
 \end{cases}$$
 for $N_{j}$ defined in [[Complete Upcrossings]] (statement 2) for $j \geq 1$. Then $(H_{n})_{n \geq 1}$ is a [[Predictable Sequence]], and thus a [[Strategy]] for $(X_{n})_{n \geq 1}$. We call it the [[Upcrossing Strategy]].
## Proof
Note that this is a [[Predictable Sequence]] since
$$H_{n} = \sum\limits_{k=1}^{\infty} 1_{N_{2k-1} \leq n-1} 1_{n-1 < N_{2k}}$$
and $N_{j}$ are all [[Stopping Time]]s for $j \geq 1$. Therefore $H$ is a [[Strategy]] for $X$. $\blacksquare$