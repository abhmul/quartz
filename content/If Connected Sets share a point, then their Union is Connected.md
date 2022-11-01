---

title: "If Connected Sets share a point, then their Union is Connected"

---
# Statement
Let $X$ be a [[Topological Space]], $x \in X$, and suppose $\mathcal{C} \subset \mathcal{P}(X)$ is such that for all $C \in \mathcal{C}$
1. $C$ is [[Connected]]
2. $x \in C$

Then $D := \bigcup\limits_{C \in \mathcal{C}} C$ is [[Connected]].

## Proof
Suppose there were some disconnecting [[Open]] $U, V \subset X$. Then because $x \in D$, only one of $x \in U$ or $x \in V$ holds. [[Without Loss of Generality]], let $x \in V$. Because all $C \in \mathcal{C}$ are [[Connected]] and $C \cap V \neq \emptyset$, we must have $C \cap V = C$. Thus $C \cap U = \emptyset$. But since this holds for all $C \in \mathcal{C}$:
$$D \cap U = \bigcup\limits_{C \in \mathcal{C}} C \cap U = \bigcup\limits_{C \in \mathcal{C}} \emptyset = \emptyset.$$
Thus $D \cap U = \emptyset$ and $D \cap V = D$, so $D$ is [[Connected]]. $\blacksquare$