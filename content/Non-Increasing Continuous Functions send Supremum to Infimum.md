# Statement
Let $(X, \leq_{X})$, $(Y, \leq_{Y})$ be [[Total Ordering]]s equipped with their respective [[Order Topology]]s and let $f: X \to Y$ be a [[Continuous Function|continuous]]  [[Non-Increasing Function]]. Let $A \subset X$ and suppose $\sup\limits A$ exists. Then
$$f(\sup\limits A) = \inf\limits f(A)$$
## Proof
By definition of [[Infimum]], $\inf\limits_{\leq_{Y}} f(A) = \sup\limits_{\leq_{Y}'} f(A)$, where $\leq_{Y}'$ is the [[Reverse Ordering]] on $Y$. Since $f$ is a [[Continuous Function|continuous]] [[Non-Decreasing Function]] to the [[Reverse Ordering]], [[Non-Decreasing Continuous Functions preserve Supremum]] tells us that 
$$f(\sup\limits A) = \sup\limits_{\leq_{Y}'}f(A) = \inf\limits_{\leq_{Y}}f(A).$$
$\blacksquare$