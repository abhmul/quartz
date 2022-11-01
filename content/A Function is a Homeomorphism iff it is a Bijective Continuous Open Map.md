
# Statement
Let $X, Y$ be [[Topological Space]]s and let $F: X \to Y$ be a [[Function]]. Then $F$ is a [[Homeomorphism]] [[If and Only If]] $F$ is a [[Bijection]], [[Continuous Function|contintuous]], and an [[Open Map]].

## Proof
$(\Rightarrow)$ Suppose $F$ is a [[Homeomorphism]]. Then $F$ is a [[Bijection]] and a [[Continuous Function]] by definition. Futhermore $F^{-1}$ is a [[Continuous Function]] by definition. Thus, for any [[Open]] $U \subset X$, $F(U) = (F^{-1})^{-1}(U)$ is [[Open]]. $\checkmark$

$(\Leftarrow)$: Suppose $F$ is a [[Bijection]], a [[Continuous Function]],  and an [[Open Map]]. Then, let $U \subset X$ be [[Open]]. We want to show $F^{-1}$ is [[Continuous Function|continuous]]. Note $(F^{-1})^{-1}(U) = F(U)$ is [[Open]] because $F$ is an [[Open Map]]. Thus $F^{-1}$ is a [[Continuous Function]] and $F$ is a [[Homeomorphism]]. $\checkmark$ $\blacksquare$