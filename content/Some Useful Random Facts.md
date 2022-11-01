---
tags:
- GraphExclude
---

 

These are some facts that I've found useful, but I don't think they really warrant their own page.

Let $A,B$ be [[Set]]s. Then $(A \cap B)^{C} = (A^{C} \cap B) \sqcup B^{C}$. This can be understood as the stuff not in $A$ and $B$ is the stuff not in $A$ when condition on being in $B$ and the stuff not in $B$ . We can formally prove it using [[De Morgan's Law]] and [[Set Subtraction]]:
$$(A \cap B)^{C} = A^{C} \cup B^{C} = (A^{C} \cap B) \cup (A^{C} \cap B^{C}) \cup B^{C} = (A^{C} \cap B) \sqcup B^{C}$$
since $(A^{C} \cup B^{C}) \subset B^{C}$.