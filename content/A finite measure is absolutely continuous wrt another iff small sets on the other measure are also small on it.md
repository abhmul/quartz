---

title: "A finite measure is absolutely continuous wrt another iff small sets on the other measure are also small on it"

---
# Statement
Let $(X, \mathcal{M})$ be a [[Measure Space]] and let $\mu, \nu$ be two [[Measure]]s on this space so that $\nu$ is [[Finite Measure|finite]]. Then $\nu << \mu$ [[If and Only If]] $\forall \epsilon > 0$, $\exists \delta > 0$ so that $\forall A \in \mathcal{M}$ so that $\mu(A) < \delta$, we have that $\nu(A) < \epsilon$. 

[[TODO]] generalize to [[Signed Measure]]s and [[Complex Measure]]s

## Proof
$(\Rightarrow)$ Suppose there is some $\epsilon > 0$ so that for all $\delta > 0$ there exists an $A \in \mathcal{M}$ so that $\mu(A) < \delta$ but $\nu(A) \geq \epsilon$. Fix this $\epsilon$. Let $A_{n} \in \mathcal{M}$ be a [[Set]] so that $\mu(A_{n}) < \frac{1}{2^{n}}$ but $\nu(A_{n}) \geq \epsilon$. Let $B_{n} = \bigcup\limits_{k \geq n} A_{k}$. Then by [[Union Bound]], $$\mu(B_{n}) \leq \sum\limits_{k=n}^{\infty} \frac{1}{2^{k}} = \frac{1}{2^{n-1}}$$
and because $B_{n} \supset A_{n}$ $$\nu(B_{n}) \geq \nu(A_{n}) \geq \epsilon.$$
Furthermore, by construction of $(B_{n})_{n=1}^{\infty}$, we have that $$B_{n} = \bigcup\limits_{k \geq n} A_{k} \supset \bigcup\limits_{k \geq n+1} A_{k} = B_{n+1}$$
Because $\mu(B_{n}) \leq 1 < \infty$, we can apply [[Continuity of Measures from Above]], so $$\mu(\bigcap\limits_{n \in \mathbb{N}} B_{n}) = \lim\limits_{n \to \infty} \mu(B_{n}) \leq \lim\limits_{n \to \infty}\frac{1}{2^{n-1}} = 0.$$
Because $\nu << \mu$, we have that $\nu(\bigcap\limits_{n \in \mathbb{N}} B_{n}) = 0$. But because $\nu$ is a [[Finite Measure]], $\nu(B_{1}) < \infty$, and by [[Continuity of Measures from Above]] we have that
$$0 = \nu(\bigcap\limits_{n \in \mathbb{N}} B_{n}) = \lim\limits_{n \to \infty} \nu(B_{n}) \geq \lim\limits_{n \to \infty} \epsilon = \epsilon > 0$$
$\unicode{x21af}$.

Therefore, $\forall \epsilon > 0$, $\exists \delta > 0$ so that for all $A \in \mathcal{M}$ so that $\mu(A) < \delta$, we have that $\nu(A) < \epsilon$. $\checkmark$.

$(\Leftarrow)$ [[If small sets on one measure are also small on another measure then it is absolutely continuous wrt the other]]. $\checkmark$ $\blacksquare$

## Remarks
1. I don't think this carries over to [[Sigma-Finite Measure|sigma-finite]] $\nu$.  Observe the following line of reasoning for the $\Rightarrow$ direction:
	> Now relax our assumption on $\nu$ to allow it to be [[Sigma-Finite Measure|sigma-finite]]. Let $\{P_{n}\}_{n \in \mathbb{N}} \subset \mathcal{M}$ be our [[Partition]] of $X$ so that $\nu(P_{n}) < \infty$ for all $n \in \mathbb{N}$. Let $\epsilon > 0$. By our result above, since $\nu {\big|}_{P_{n}}$ is a [[Finite Measure]], there exists a $\delta_{n} > 0$ so that for all $A_{n} \in \mathcal{M} \cap P_{n} \subset \mathcal{M}$ for which $\mu(A_{n}) < \delta_{n}$, we have that $\nu {\big|}_{P_{n}}(A_{n}) < \frac{\epsilon}{2^{n}}$. We could have $\inf\limits_{n \in \mathbb{N}}\delta_{n} = 0$, in which case any choice of overall $\delta > 0$, could concentrate too much measure on some $k \in \mathbb{N}$ for which $\delta_{k} < \delta$.
# Other Outlinks
- [[Absolute Continuity]]
- [[Proof by Contradiction]]
- [[Restriction Measure]]
- [[Intersection Sigma Algebra]]