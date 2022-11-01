---

title: "Lp Space"

---
# Statement
Let $(X, \mathcal{M}, \mu)$ be a [[Measure Space]], let $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $p \in [1, \infty]$. Define for $p < \infty$
$$L^{p}(X, \mathcal{M}, \mu) := \{[f] \in L^{0}(X, \mathbb{K}): \int\limits_{X} |f|^{p} d \mu < \infty\}$$
and for $p = \infty$
$$L^{\infty}(X, \mathcal{M}, \mu):= \{[f] \in L^{0}(X, \mathbb{C}) : \exists C \geq 0, A \subset X \text{ s.t. }\mu(A^{C}) = 0,|f(x)| \leq C \text{ }\forall x \in A\}.$$
Then $L^{p}$ is a [[Normed Vector Space]] equipped with the [[Lp Norm]] 
$$||f||_{p} := \left(\int\limits_{X} |f|^{p} d \mu\right)^{\frac{1}{p}}$$
if $p < \infty$ and 
$$||f||_{\infty} := \text{esssup}_{X} f := \inf\limits\{C > 0 : \mu(|f|^{-1}((C, \infty)) = 0\}$$
If we want to refer to the original [[Set]] of [[Measureable Function]]s rather than their [[Equivalence Class]]es, we use $\mathcal{L}^{p}$.

## Proof
First we check that $L^{p}$ and $||\cdot||_{p}$ are well-defined. 

If $p=\infty$, $f \in \mathcal{L}^\infty$, and $f' \in \mathcal{L}^{0}$ so that $[f] = [f']$, then there exists $C = ||f||_{\infty}$. Then because $[f \neq f']$ is a [[Null Set]], and $[f' > C] \subset [f > C] \cup [f' \neq f]$, $[f' > C]$ is a [[Null Set]]. Therefore $||f'||_{\infty} \leq C$ and $f' \in \mathcal{L}^\infty$. But then our argument also works from $f'$ to $f$, so $C \leq ||f'||_\infty$. Therefore $||f||_{\infty} = ||f'||_\infty$.

Suppose $p < \infty$, $f \in \mathcal{L}^{p}$, $[f] = [f]'$ for some $f' \in \mathcal{L}^{0}$. If $x \in X$ so that $f(x) = f'(x)$, then $|f(x)|^{p} = |f'(x)|^{p}$. Since [[Integration of a Null Set is 0]]
$$\int\limits_{X}|f|^{p} = \int\limits_{[f = f']}|f|^{p} = \int\limits_{[f = f']}|f'|^{p} = \int\limits_{X} |f'|^{p}.$$Thus $f' \in \mathcal{L}^{p}$ and $||f||_{p} = ||f'||_{p}$.

Next we show $L^{p}$ is a [[Vector Space]]. Recall $L^{0}$ [[Measureable Functions form a Vector Space|forms a vector space]]. Thus we need only show $L^{p}$ is a [[Vector Subspace]] for $p \in [1, \infty]$. 

For $p = \infty$, let $f,g \in L^\infty$ and $c \in \mathbb{K}$. We know there exists $C, C' > 0$ so $\mu([|f| > C]) = 0 = \mu([|g| > C'])$. Since $|\cdot|$ is a [[Magnitude is a Norm|is a norm]], if $x \in X$ so $C \geq |f(x)|$ and $C' \geq |g(x)|$, then $$|c|C + C' \geq |c||f(x)| + |g(x)| \geq |cf(x) + g(x)|.$$ Letting $D := |c|C + C'$, $[|cf + g| \leq D]\supset [|f| \leq C] \cup [|g| \leq C']$. Then, $$0 \leq \mu([|cf + g| > D]) \leq \mu([|f| > C] \cap [|g| > C']) \leq \mu([|f| > C]) = 0.$$This gives us that $cf + g \in L^\infty$ and it is a [[Vector Space]] because [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]].


For $1 \leq p < \infty$, let $f,g \in L^{p}$ and let $c \in \mathbb{K}$. Then because 
$$|f + g|^{p} \leq (|f| + |g|)^{p} \leq (2 \max\limits(|f|, |g|))^{p} = 2^{p} \max\limits(|f|^{p}, |g|^{p}) \leq 2^{p}(|f|^{p} + |g|^{p})$$
We have
$$\int\limits_{X} |f + g|^{p} \leq 2^{p} \int\limits_{X} |f|^{p} + |g|^{p} < \infty,$$
and $f+g \in L^{p}$. Furthermore
$$\int\limits_{X} |cf|^{p} = |c|\int\limits_{X} |f|^{p} < \infty,$$
so $cf \in L^{p}$. Because [[A Subset of a Vector Space is a Subspace iff it is closed under scaling and addition]], $L^{p}$ is a [[Vector Space]].

The final piece to show is that the [[Lp Norm]] is indeed a [[Norm]].

[[TODO]] The proof is effectively broken into the following pieces
- [x] Lp is a [[Vector Space]]
- [x] [[Lp Norm]] is well defined
- [ ] [[Lp Norm]] is a [[Norm]]

## Remarks
1. The definition of $||\cdot||_\infty$ hinges on the fact that $\mathbb{K}$ is a [[Complete Metric Space]].


# Other Outlinks
- [[Measureable Function]]
- [[Almost Everywhere Equivalence Relation]]
- [[Integration]]
- [[Essential Supremum]]