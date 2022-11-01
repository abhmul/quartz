---

title: "Reverse Ordering"

---
# Statement 1
Let $(P, \leq)$ be a [[Partial Ordering]]. Then the [[Reverse Ordering]] of $P$, $(P, \leq')$ is  defined as $a \leq' b \Leftrightarrow a \geq b$ $\forall a,b \in T$. It is a [[Partial Ordering]].

## Proof
For all $a \in P$, $a \leq' a$ since $a \geq a$ $\checkmark$. Suppose $a,b \in P$. If $a \leq' b$ and $b \leq' a$, then $a \geq b$ and $b \geq a$, so $a = b$ $\checkmark$. Suppose $a,b,c \in P$. If $a \leq' b$ and $b \leq' c$, then $a \geq b$ and $b \geq c$, so $a \geq c$, implying that $a \leq' c$ $\checkmark$. $\blacksquare$

# Statement 2
The [[Reverse Ordering]] of a [[Total Ordering]] is a [[Total Ordering]].

## Proof
This follows because we can compare any $a,b \in T$ with $\leq'$ using the corresponding comparison with $\leq$. $\blacksquare$

