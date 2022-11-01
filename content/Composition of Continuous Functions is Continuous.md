---

title: "Composition of Continuous Functions is Continuous"

---
# Statement
Suppose $X,Y, Z$ are [[Topological Space]]s and $F : X \to Y, G: Y \to Z$ are [[Continuous Function]]s. Then $G \circ F$ is a [[Continuous Function]].

## Proof
Let $W \subset Z$ be [[Open]]. Then because $G$ is [[Continuous Function|continuous]], $G^{-1}(W)$ is [[Open]] in $Y$. Since $F$ is [[Continuous Function|continuous]], $(G \circ F)^{-1}(W) = F^{-1}(G^{-1}(W))$ is [[Open]] in $X$. Since $W$ was arbitrary, $G \circ F$ is a [[Continuous Function]]. $\blacksquare$

# Other Outlinks
- [[Function Preimage]]
- [[Function Composition]]