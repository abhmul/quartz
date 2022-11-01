---

title: "Continuous Functions Preserve Connectedness"

---
# Statement
Let $X, Y$ be [[Topological Space]]s and suppose $X$ be [[Connected]]. Then if $f: X \to Y$ is a [[Continuous Function]], $f(X)$ is also [[Connected]].

## Proof
We'll prove by [[Contraposition]]. We assume $f(X)$ is not [[Connected]]. That is there exist $U, V \subset Y$ [[Open]] so that $U \cap f(X) \sqcup V \cap f(X) = f(X)$ and $U \cap f(X),V \cap f(X)$ not $\emptyset, f(X)$. Then, because $f$ is [[Continuous Function]], $$f^{-1}(U \cap f(X)) = f^{-1}(U) \cap X = f^{-1}(U)$$ is [[Open]]. Likewise for $V \cap f(X)$. Let $$\begin{align*}
U' := f^{-1}(U) (= f^{-1}(U \cap f(X)))\\
V' := f^{-1}(V) (= f^{-1}(V \cap f(X)))
\end{align*}$$ Since $U \cap f(X)$ is [[Disjoint Sets|disjoint]] from $V \cap f(X)$, we have that $f^{-1}(U) \cap f^{-1}(V) = \emptyset$. But since $U \cup V \supset f(X)$, $f^{-1}(U) \cup f^{-1}(V) \supset X$, and is thus equal to $X$. Since $U \cap f(X)$ neither [[Empty Set]] nor $f(X)$, we have that both $f^{-1}(U)$ and $f^{-1}(V)$ are [[Nonempty]]. Thus $X$ is not [[Connected]]. $\blacksquare$