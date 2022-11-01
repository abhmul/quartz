---

title: "Satisfaction Relation"

---
# Definition 1
Let $\mathcal{L}$ be a [[Language]], let $\mathcal{M}$ be an $\mathcal{L}$-[[Language Structure|structure]], let $\phi$ be an $\mathcal{L}$-[[Formula|formula]], and let $\sigma$ be an [[Assignment]] to $\mathcal{M}$. We [[Induction|inductively]] define $\mathcal{M} \models_{\sigma} \phi$ as
1. If $\phi$ is $t_{1} = t_{2}$ for [[Term]]s $t_{1}, t_{2}$, then $\mathcal{M} \models_{\sigma} \phi$ if $t_{1}^{\mathcal{M}}[\sigma] = t_{2}^{\mathcal{M}}[\sigma]$.
2. If $\phi$ is $R(t_{1}, \dots, t_{n_{R}})$, then $\mathcal{M} \models_{\sigma} \phi$ if $(t^{\mathcal{M}}_{1} [\sigma], \dots, t^{\mathcal{M}}_{n_{R}} [\sigma]) \in R^{\mathcal{M}}$.
3. If $\phi$ is $\neg \psi$, then $\mathcal{M} \models_{\sigma} \phi$ if $\mathcal{M} \not\models_{\sigma} \psi$.
4. If $\phi$ is $(\varphi \wedge \psi)$, for $\mathcal{L}$-[[Formula|formula]]s $\varphi$ and $\psi$, then $\mathcal{M} \models_{\sigma} \phi$ if $\mathcal{M} \models_{\sigma} \varphi$ and $\mathcal{M} \models_{\sigma} \psi$.
5. If $\phi$ is $(\varphi \vee \psi)$, for $\mathcal{L}$-[[Formula|formula]]s $\varphi$ and $\psi$, then $\mathcal{M} \models_{\sigma} \phi$ if $\mathcal{M} \models_{\sigma} \varphi$ or $\mathcal{M} \models_{\sigma} \psi$.
6. If $\phi$ is $\exists v \psi$, for [[Variable Symbol]] $v$, then $\mathcal{M} \models_{\sigma} \phi$ if there is some $a \in \mathcal{M}$ so that $\mathcal{M} \models_{\sigma[\frac{a}{v}]} \psi$.
7. If $\phi$ is $\forall v \psi$, for [[Variable Symbol]] $v$, then $\mathcal{M} \models_{\sigma} \phi$ if for any $a \in \mathcal{M}$ we have that $\mathcal{M} \models_{\sigma[\frac{a}{v}]} \psi$.

If $\mathcal{M} \models_{\sigma} \phi$, we say that $\mathcal{M}$ [[Satisfaction Relation|satisfies]] $\phi$ under [[Assignment]] $\sigma$. We call $\models$ the [[Satisfaction Relation]].

## Remarks
1. This part also felt very circular to me, especially cases 3-7. However, now I look at it as an extension of the concept of an $\mathcal{L}$-[[Language Structure|structure]]. They are "interpretations" of the symbols we use.
2. Although an [[Assignment]] has an [[Infinite Set]] as its [[Domain]], when applied to a particular [[Formula]], only [[Finite Set|finitely]] many [[Variable Symbol]]s come into play. This is because [[Formulas are Finite]].

# Definition 2
Let $\mathcal{L}$ be a [[Language]], let $\mathcal{M}$ be an $\mathcal{L}$-[[Language Structure]], and let $\phi$ be an $\mathcal{L}$-[[Formula]]. $\mathcal{M} \models \phi$ if $\mathcal{M} \models_{\sigma} \phi$ for all [[Assignment]]s $\sigma$.

## Remarks
1. This is equivalent to saying $\mathcal{M} \models_{\sigma} \phi$ for some [[Assignment]] $\sigma$ because of [[Sentence Satisfaction under one Assignment means Satisfaction under all Assignments]].

# Definition 3
See [[Model]]