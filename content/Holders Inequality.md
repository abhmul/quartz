---

title: "Holder Inequality"

---
# Statement
Let $\infty \geq p,q \geq 1$ so that $\frac{1}{p} + \frac{1}{q} = 1$. [[Holders Inequality]] is broken into the following statements. 
1. If $f,g \in L^{0}$, $||fg||_{1} \leq ||f||_{p}||g||_{q}$.
2. If $f \in L^{p}, g \in L^{q}$, $fg \in L^{1}$.
3. If $1 < p,q < \infty$ and $f \in L^{p}, g \in L^{q}$, then $||fg||_{1} = ||f||_{p} ||g||_{q}$ [[If and Only If]] either $f$ or $g$ is $0$ [[Almost Everywhere]] or there exist $\alpha, \beta > 0$ so $\alpha|f|^{p} = \beta |g|^{q}$ ([[Almost Everywhere]]).
4. If  $f \in L^{\infty}, g \in L^{1}$, then $||fg||_{1} = ||f||_{\infty} ||g||_{1}$ [[If and Only If]] $g = 0$ [[Almost Everywhere]] or there exists $C \geq 0$ so that $C = |f|$ [[Almost Everywhere]].

## Proof
### (1) $\Rightarrow$ (2)
First note that if (1) holds, then (2) holds. This follows because if $f \in L^{p}$ and $g \in L^{q}$ so that $1 \leq p,q \leq \infty$ and $\frac{1}{p} + \frac{1}{q} = 1$, then 
$$||fg||_{1} \leq ||f||_{p} ||g||_{q} < \infty.$$
so $fg \in L^{1}$. $\checkmark$
### Proof of (1)
#### Edge cases
Next, we establish (1). Getting some edge cases out of the way for $1 \leq p, q \leq \infty$:
1. If $||f||_{p} = 0$, then $f=0$, so $||fg||_{1} = 0$ and (1) holds, where we take $0 * \infty := 0$. Symmetry ensures (1) follows if $g = 0$.
2. If $||f||_{p} = \infty$ and $||g||_{q} \neq 0$, then because $||fg||_{1} \leq \infty$ already, $||fg||_{1}  \leq ||f||_{p} ||g||_{q}$. Symmetry ensures (1) follows if we flip $f$ and $g$.
$\checkmark$
#### Main case
It remains to show (1) for $f,g \in L^{0}$ so that $0 < ||f||_{p}, ||g||_{q} < \infty$. Note that if the result holds for all $f',g' \in L^{0}$ so $||f'||_{p} = 1 = ||g'||_{q}$, then we have for $f' = \frac{f}{||f||_{p}}$ and $g' = \frac{g}{||g||_{q}}$
$$||fg||_{1} = ||f||_{p} ||g||_{q} ||f'g'||_{1} \leq ||f||_{p} ||g||_{q} ||f'||_{p}||g'||_{q} = ||f||_{p}||g||_{q}.$$
Thus it suffices to prove $||fg||_{1} \leq 1$ for all $f \in S(L^{p}),g \in S(L^{q})$.

##### $p=\infty$, $q=1$
 If $p= \infty$ and $q=1$, then $|f| \leq 1$ [[Almost Everywhere]], which means $|fg| = |f||g| \leq |g|$ [[Almost Everywhere]]. Therefore $$||fg||_{1} = \int\limits |fg| \leq \int\limits |g| = ||g||_{1} = 1 = ||f||_{\infty}||g||_{1}$$ by [[Integration is Non-Decreasing]]. Symmetry ensures the result holds for $q=\infty$, $p = 1$. $\checkmark$

##### $1 < p,q < \infty$
If $1 < p,q < \infty$, then by the [[Log Concavity Inequality]], if $\frac{1}{p} + \frac{1}{q} = 1$, we have that 
$$|fg| = (|f|^{p})^{\frac{1}{p}} (|g|^{q})^{\frac{1}{q}} \leq \frac{1}{p} |f|^{p} + \frac{1}{q} |g|^{q}.$$
Because [[Integration is Non-Decreasing]], 
$$||fg||_{1} = \int\limits |fg| \leq \frac{1}{p} \int\limits |f|^{p} + \frac{1}{q} \int\limits |g|^{q} = \frac{1}{p} ||f||_{p}^{p} + \frac{1}{q} ||g||_{q}^{q} = 1 = ||f||_{p}||g||_{q}.$$

This completes our proof of (1). $\checkmark$

### Proof of (3)
Let $1 < p,q < \infty$ so that $\frac{1}{p} + \frac{1}{q} = 1$.

#### $\Rightarrow$ direction
Let $f \in L^{p}, g \in L^{q}$ so that $||fg||_{1} = ||f||_{p}||g||_{q}$. We break this proof into the following cases:
##### $f = 0$ or $g=0$ [[Almost Everywhere]]
Then $\Rightarrow$ direction trivially holds by assumption. 
##### $f,g \neq 0$ [[Almost Everywhere]]
For $f \in S(L^{p}), g \in S(L^{q})$ we would have
$$\begin{align*}
&||fg||_{1} = \int\limits |fg| = \frac{1}{p} \int\limits |f|^{p} + \frac{1}{q} \int\limits |g|^{q} = 1 = ||f||_{p} ||g||_{q}\\
\Rightarrow&0 = \int\limits \frac{1}{p} |f|^{p} + \frac{1}{q} |g|^{q} - |fg|\\
\Rightarrow&\frac{1}{p} |f|^{p} + \frac{1}{q} |g|^{q} = |fg| \text{ a.e.}
\end{align*}$$
because $|fg| \leq \frac{1}{p} |f|^{p} + \frac{1}{q} |g|^{q}$ and [[Integration of a Nonnegative Function is 0 iff the Function is 0 Almost Everywhere]]. By the [[Log Concavity Inequality]], since $\frac{1}{p} \in (0,1)$, this means $|f|^{p} = |g|^{q}$ a.e.. For arbitrary $f \in L^{p}, g \in L^{q}$ because $||fg||_{1} = ||f||_{p} ||g||_{q}$ means $||\frac{f}{||f||_{p}} \frac{g}{||g||_{q}}||_{1} = || \frac{f}{||f||_{p}} ||_{p} || \frac{g}{||g||_{q}} ||_{q}$, we know that [[Almost Everywhere]]
$$\begin{align*}
&|\frac{f}{||f||_{p}}|^{p} = |\frac{g}{||g||_{q}}|^{q}\\
\Rightarrow &||g||_{q}^{q} |f|^{p} = ||f||_{p}^{p} |g|^{q}.
\end{align*}$$
Letting $\alpha := ||g||^{q}_{q}$ and $\beta := ||f||_{p}^{p}$, and noting both $||g||_{q} > 0$ and $||f||_{p} >0$, we have our result. $\checkmark$

#### $\Leftarrow$ direction
##### $f = 0$ or $g=0$ [[Almost Everywhere]]
Let $f \in L^{p}, g \in L^{q}$ so that $f=0$ [[Almost Everywhere]]. Then equality follows from noting
$$||fg||_{1} = 0 = ||f||_{p} ||g||_{q}.$$
By symmetry on $p,q$, the proof also holds if $g=0$ [[Almost Everywhere]].

##### $\alpha |f|^{p} = \beta |g|^{q}$ for $\alpha, \beta > 0$ and $f,g \neq 0$ [[Almost Everywhere|somewhere]]
The assumptions means neither $f=0$ or $g=0$ [[Almost Everywhere]]. Thus $||f||_{p}, ||g||_{q} > 0$.

Since $\alpha > 0$, we have that $| \frac{f}{||f||_{p}} |^{p} = \frac{\beta}{\alpha ||f||_{p}^{p} } |g|^{q}$. Let $C := (\frac{\beta}{\alpha ||f||_{p}^{p} })^{\frac{1}{q}}$. Then we have 
$$1 = \int\limits | \frac{f}{||f||_{p}} |^{p} = \int\limits |Cg|^{q}$$
and $Cg \in S(L^{q})$. Denote $f' := \frac{f}{||f||_{p}}$ and $g' := Cg$. We have that $|f'|^{p} = |g'|^{q}$ [[Almost Everywhere]], so by the [[Log Concavity Inequality]]:
$$|f'g'| = \frac{1}{p} |f'|^{p} + \frac{1}{q} |g'|^{q}.$$
Then 
$$||f'g'||_{1} = \frac{1}{p} + \frac{1}{q} = 1 = ||f'||_{p}||g'||_{q}.$$
Thus,
$$\frac{C}{||f||_{p}} ||fg||_{1} = \frac{C}{||f||_{p}} ||f||_{p}||g||_{q}$$
giving us $||fg||_{1} = ||f||_{p}||g||_{q}$. $\checkmark$

### Proof of (4)
#### $\Rightarrow$ direction
We assume $f \in L^{\infty}, g \in L^{1}$ and $||fg||_{1} = ||f||_{\infty}||g||_{1}$

##### $g =0$ [[Almost Everywhere]]
Then the result hold trivially by assumption.

##### $g \neq 0$ [[Almost Everywhere|somewhere]]
We will show $|f| = ||f||_{\infty}$ [[Almost Everywhere]]. Let $f' = \frac{f}{||f||_{\infty}} \in S(L^{\infty})$. Then  $$||f'g||_{1} = \frac{||fg||_{1}}{||f||_{\infty}} = \frac{||f||_{\infty} ||g||_{1}}{||f||_{\infty}} = ||g||_{1}.$$
Since $|f'| \leq ||f'||_{\infty} = 1$ [[Almost Everywhere]], We have $|f'g| \leq |g|$ [[Almost Everywhere]]. Thus,

$$\begin{align*}
&\int\limits |f'g| = ||f'g||_{1} = ||g||_{1} = \int\limits |g|\\
\Rightarrow&0 = \int\limits |g| - |f'g|\\
\Rightarrow&|g| = |f'||g| \text{ a.e.}\\
\Rightarrow&1 = |f'| \text{ a.e.}
\end{align*}$$
because [[Integration of a Nonnegative Function is 0 iff the Function is 0 Almost Everywhere]] and $|g| \neq 0$ [[Almost Everywhere|somewhere]]. Therefore $|f| = |f'| ||f||_{\infty} = ||f||_{\infty}$ [[Almost Everywhere]]. $\checkmark$

#### $\Leftarrow$ direction
##### $g =0$ [[Almost Everywhere]]
Then equality follows from noting
$$||fg||_{1} = 0 = ||f||_{\infty} ||g||_{1}.$$
##### $|f| = C$ for $C \geq 0$ [[Almost Everywhere]]

Then $||f||_{\infty} = C$ so
$$||fg||_{1} = \int\limits|fg| = C\int\limits |g| = ||f||_{\infty} ||g||_{1}.$$
This completes the proof of (4) and the entire set of statement. $\checkmark$

$\blacksquare$

## Remarks
1. If $\infty > p,q > 0$ so that $\frac{1}{p} + \frac{1}{q} = 1$, then $q = \frac{p}{p-1}$.
2. If $\infty > p,q > 0$ so that $\frac{1}{p} + \frac{1}{q} =1$, then noting Remark (1) above, $q > 0 \Rightarrow 1-p > 0$, so $p > 1$. But our defining property of $p,q$ is symmetric, so $q > 1$ as well. Thus, we can relax our condition on $p,q$ to be $0 < p,q \leq \infty$.
3. Although we are using [[Lp Norm]]s in the definition, we have not yet proven they satisfy the [[Triangle Inequality]]. We can however use their [[Non-Degeneracy]] and [[Homogeniety]] since that was proved in [[Lp Space]] without the use of [[Holders Inequality]]. However, in our statement for [[Holders Inequality]].

# Other Outlinks
- [[Measureable Function]]
- [[Lp Space]]
- [[Unit Sphere]]