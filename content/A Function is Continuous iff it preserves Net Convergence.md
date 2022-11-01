---

title: "A Function is Continuous iff it preserves Net Convergence"

---
# Statement
Let $X, Y$ be [[Topological Space]]s and let $f: X \to Y$ be a [[Function]]. Then $f$ is a [[Continuous Function]] [[If and Only If]] for all [[Net]]s $\{x_{\alpha}\}_{\alpha \in A} \subset X$, if $\lim\limits_{\alpha \in A}x_{\alpha} = x$ then $\lim\limits_{\alpha \in A}f(x_{\alpha}) = f(x)$.

## Proof
First note for [[Net]] $\{x_{\alpha}\}_{\alpha \in A} \subset X$, $f \circ x_{\bullet}$ is a [[Net]] on $Y$ since it is a [[Function]] from [[Directed Partial Ordering]] $A$ to $Y$. 

$(\Rightarrow)$: Suppose $f$ is a [[Continuous Function]]. Let $\{x_{\alpha}\}_{\alpha \in A} \subset X$ be a [[Net]]. Let $V \subset Y$ be [[Open]] so $V \ni f(x)$. Then $f^{-1}(V)$ is [[Open]] and $x \in f^{-1}(V)$. Since $x_{\alpha}\to x$, there exists $\alpha_{0}$ s.t. for all $\alpha \geq \alpha_{0}$, $x_{\alpha} \in f^{-1}(V)$. Thus for all $\alpha \geq \alpha_{0}$, $f(x_{\alpha}) \in V$. Then, by definition of [[Net Convergence]], $f(x_{\alpha}) \to f(x)$. $\checkmark$

($\Leftarrow$): Let $K \subset Y$ be [[Closed]]. Let $\{x_{\alpha}\}_{\alpha \in A} \subset f^{-1}(K)$ be a [[Net]] so that $\lim\limits_{\alpha \in A} x_{\alpha} = x \in X$. We will show that $x \in f^{-1}(K)$. By assumption, we know $\lim\limits_{\alpha \in A}f(x_{\alpha}) = f(x)$. Since $\{x_{\alpha}\}_{\alpha \in A}$ is a subset of $f^{-1}(K)$, $\{f(x_{\alpha})\}_{\alpha \in A} \subset K$. Recall [[A Set is Closed iff it contains all Net Limits]]. Thus $f(x) \in K$. This means $x \in f^{-1}(K)$. Since $\{x_{\alpha}\}_{\alpha \in A}$ was arbitrary, then because [[A Set is Closed iff it contains all Net Limits]], $f^{-1}(K)$ is [[Closed]] in $X$. Thus, because [[A Function is Continuous iff it takes Closed Sets back to Closed Sets]], $f$ is a [[Continuous Function]]. $\checkmark$ $\blacksquare$

# Other Outlinks
- [[Net Convergence]]