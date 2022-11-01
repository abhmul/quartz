---

title: "Connected Components of Locally Path-Connected Spaces are Open"

---
# Statement
Let $X$ be a [[Topological Space]] that is [[Locally Path-Connected]]. Then every [[Connected Component]] $C \subset X$ is [[Open]].

## Proof
Let $C \subset X$ be a [[Connected Component]] of $X$. Since $X$ is [[Locally Path-Connected]], for each $x \in C$, there exists $U \subset X$ [[Open]] so $x \in U$ and $U$ is [[Path-Connected]]. Recall [[Path-Connected implies Connected]], so $U$ is [[Connected]]. Since $U \cap C \ni x$, we know that $U \cup C$ is [[Connected]] because [[If Connected Sets share a point, then their Union is Connected]]. But $U \cup C \supset C$. Because $C$ is [[Maximal]], $U \cup C = C$. Thus $U \subset C$. Since $x$ was arbitrary, we can find such a $U_{x}$ for each $x \in C$. But then $$C = \bigcup\limits_{x \in C}U_{x}$$so $C$ is [[Open]]. $\blacksquare$

# Other Outlinks
- [[Subset Relation]]