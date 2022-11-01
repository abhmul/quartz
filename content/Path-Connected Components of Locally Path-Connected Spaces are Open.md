---

title: "Path-Connected Components of Locally Path-Connected Spaces are Open"

---
# Statement
Let $X$ be a [[Topological Space]] that is [[Locally Path-Connected]]. Then every [[Path-Connected Component]] $P \subset X$ is [[Open]].

## Proof
Let $P \subset X$ be a [[Path-Connected Component]] of $X$. Since $X$ is [[Locally Path-Connected]], for each $x \in P$, there exists $U \subset X$ [[Open]] so $x \in U$ and $U$ is [[Path-Connected]]. Since $U \cap P \ni x$, we know that $U \cup P$ is [[Path-Connected]] because [[If Path-Connected Sets share a point, then their Union is Path-Connected]]. But $U \cup P \supset P$. Because $P$ is [[Maximal]], $U \cup P = P$. Thus $U \subset P$. Since $x$ was arbitrary, we can find such a $U_{x}$ for each $x \in P$. But then $$P = \bigcup\limits_{x \in P}U_{x}$$so $P$ is [[Open]]. $\blacksquare$

# Other Outlinks
- [[Subset Relation]]
- [[Set Union]]