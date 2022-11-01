---

title: "Random Classifier"

---
# Definition
Let $(X, Y, n)$ be a [[Classification Problem]]. Let $f: \mathcal{D} \to \mathcal{P}^{n}$. Then a [[Random Classifier]] is a [[Random Variable]] $F$ on $[n]$ s.t. $\forall i \in [n]$
$$\mathbb{P}(F=i | X=x) = f(x).$$
$\mathcal{P}^{n} = \{t \in [0,1]^{n} : \sum\limits_{i=1}^{n} t_{i} = 1\}$ is the [[Set]] of [[Probability Mass Function]]s on $n$ elements.