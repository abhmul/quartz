---

title: "Markov Process"

---
[[TODO]] - flesh out [[Conditional Probability]] then come back to this.
# Definition 1
Let $\{X_{n} : \Omega \to S\}_{n \in \mathbb{N}}$ be a [[Adapted Process]] to [[Filtration]] $\{\mathcal{F}_{n}\}_{n \in \mathbb{N}}$ on [[Probability Space]] $(\Omega, \mathcal{B}, \mathbb{P})$ with [[Total Ordering]] $T$ and [[Countable]] [[State Space]] $S$. Then this process is a [[Markov Process]] if for any $i, j, i_{1}, \dots, i_{n-1} \in S$, $n \in \mathbb{N}$ we have that
$$\mathbb{P}(X_{n+1} = j | X_{n} = i, \dots, X_{1} = i_{1}) = \mathbb{P}(X_{n+1} = j | X_{n} = i)$$


# Definition 2
Let $\{X_{t}: \Omega \to \mathbb{R}\}_{t \in T}$ be a [[Stochastic Process]] on [[Probability Space]] $(\Omega, \mathcal{A}, \mathbb{P})$ with [[Total Ordering]] $T$. $\{X_{t}: \Omega \to \mathbb{R}\}_{t \in T}$ is a [[Markov Process]] if $\forall n \in \mathbb{N}$, $\forall t_{1} < t_{2} < \dots < t_{n}$ $\forall \lambda \in \mathbb{R}$
$$\mathbb{P}(X_{t_{n}} \leq \lambda | X_{t_{1}}, \dots, X_{t_{n-1}} ) = \mathbb{P}(X_{t_{n}} \leq \lambda | X_{t_{n}} )$$
[[Almost Surely]].

## Remarks
1. Intuitively we are saying that the only the most recent observation matters. The past is only relevant in so much as it tells us about the most recent observation.
2. [[Conditional independence]]

# Other Outlinks
- [[Conditional Probability]]
- [[Regular Conditional Distribution]]