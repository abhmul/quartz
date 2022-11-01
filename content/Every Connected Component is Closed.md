---

title: "Every Connected Component is Closed"

---
# Statement
Let $X$ be a [[Topological Space]] and let $C \subset X$ be a [[Connected Component]]. Then $C$ is [[Closed]].

## Proof
Consider $x \not\in C$. We know $\{x\} \cup C$ must be dis[[Connected]] because $C$ is a [[Maximal]] [[Connected]] [[Set]]. Thus there exists $U_{x}, V_{x} \subset X$ [[Open]] that disconnect $C \cup \{x\}$. Because $C$ is [[Connected]] either $C \subset U_{x}$ or $C \subset V_{x}$. [[Without Loss of Generality]] suppose $C \subset V_{x}$. Then we must have $x \in U_{x}$ and $U_{x} \cap C = \emptyset$. Thus $U := \bigcup\limits_{x \in X} U_{x}$ is [[Open]] and $U^{C} = C$. Thus $C$ is [[Closed]]. $\blacksquare$