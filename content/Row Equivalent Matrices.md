---

title: "Row Equivalent Matrices"

---
# Statement
Let $F$ be a [[Field]], $m,n \in \mathbb{N}$. Let $r$ be the [[Relation]] so that $ArB$ for $A, B \in F^{m \times n}$ if there exists [[Elementary Row Operation]]s $e_{1}, \dots , e_{k}$ for some $k \in \mathbb{N}$ so that 
$$B = e_{k}(e_{k-1} ( \cdots e_{1}(A) \cdots )).$$
Then $r$ is an [[Equivalence Relation]]. We call $A, B$ [[Row Equivalent Matrices]] if $ArB$. If $A, B$ are [[Row Equivalent Matrices]], then we write $A \sim_{R} B$.

## Proof
We check the criteria for being an [[Equivalence Relation]]:
1. $ArA$ because the identity is an [[Elementary Row Operation]].
2. If $ArB$, then because [[Elementary Row Operations are Invertible by other Elementary Row Operations]], we have that $BrA$.
3. If $ArB$ and $BrC$, then composing the [[Elementary Row Operation]]s that from $A$ to $B$ with those that go from $B$ to $C$ give us $ArC$.
$\blacksquare$