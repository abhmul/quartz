---
title: "Maximums are Non-Decreasing Set Functions"
---

# Statement
Let $(T, \leq)$ be a [[Total Ordering]] and suppose $A \subset B \subset T$ such that $\max A$ and $\max B$ both exist. Then $\max A \leq \max B$.

# Proof
Let $m = \max B$. Then $m \geq b$ for all $b \in B$. Since $A \subset B$, we have that $m \geq a$ for all $a \in A$. By definition [[Maximum]], $\max A \in A$, so $$\max B = m \geq \max A$$ $\blacksquare$