1. If $f: D \to \mathbb{R}^k$ where $D \subseteq \mathbb{R}^n$, and also if $a$ is in the interior of $D$, then a **derivative** of $f$ at $a$ is defined to be any map $L: \mathbb{R}^n \to \mathbb{R}^k$ such that

$$lim_{h \to 0} \frac{f(a+h) - f(a) - L(h)}{|h|} = 0$$

Equivalently, the function $\textbf{\epsilon}(h) := f(a+h) - f(a) - L(h)$ has $\frac{\textbf{\epsilon}(h)}{|h|} \to 0$ as $h \to 0$.

2. The derivative is always unique. This is proved via a lemma: if $T: \mathbb{R}^n \to \mathbb{R}^k$ is such that $\frac{T(h)}{|h|} \to 0$ as $h \to 0$, then $T$ is the zero map. After this, if we have any two derivatives $L$ and $M$ of $f$ at $a$, then it can be proved that $L - M$ has the above property, establishing $L = M$. We notate this unique map by $Df(a)$, called **the differential of $f$ at $a$**.

3. Note that if $f$ is real-valued, the derivative of $f$ at any $a$ is a covector of $\mathbb{R}^n$.

4. The **directional derivative** in direction $u$ of some $f$ at $a \in int dom f$, where $|u| = 1$, is defined to be

$$D_u f(a) := lim_{t \to 0} \frac{(f(a+tu) - f(a)}{t}$$

if it exists.

Note that as we have defined it, the $u$-th directional derivative of f at $a$, $D_u f(a)$, is a vector in $\mathbb{R}^k$ (scalar in the case of $k = 1$) and not a function, in contrast to total derivatives. Of course, we can always consider for any $v \in \mathbb{R}^k$ as a function $\mathbb{R} \to \mathbb{R}^k$ defined by $x \mapsto x \cdot v$.

In particular, the directional derivatives for $e_1, \ldots, e_n$, the standard basis vectors of $\mathbb{R}^n$, are denoted $D_1 f, \ldots, D_n f$, each one $D_i$ being called **the $i$-th partial derivative**.

5. Consider the case of real-valued $f$. We can view the graph of $f$ as a subset of $\mathbb{R}^{n+1}$, an $n$-dimensional differentiable manifold of some sort. Then the derivative can be thought of, geometrically, as the **tangent hyperplane** to the surface at $a$. This is why some books occasionally talk about "affine approximation" in conjunction with derivatives: you are locally approximating some $n$-dimensional surface with a certain affine subspace (an affine hyperplane, specifically).

6. $D_u f(a) = Df(a)[u]$ for any direction $u$. We can see this by noting that since

$$\textbf{\epsilon}(h) = f(a+h) - f(a) - Df(a)[h]$$

is true for sufficiently small $h$, we must have

$$\textbf{\epsilon}(tu) = f(a+tu) - f(a) - t Df(a)[u]$$

Since $\textbf{\epsilon}(h) \ |h| \to 0$ as $h to 0$, we similarly have $\frac{ \textbf{\epsilon}(tu) }{ |tu|} \to 0$ as $t \to 0$. This implies that $\frac{ \textbf{\epsilon}(tu) }{ |t| } \to 0$ as $t \to 0$, which further implies

$$lim_{t \to 0} \frac{ \textbf{\epsilon}(tu) }{ t } = 0$$

But $lim_{t \to 0} \frac{ \textbf{\epsilon}(tu) }{ t } = lim_{t \to 0} \frac{ f(a+tu)-f(a) }{t} - Df(a)[u] = 0$, so

$$D_u f(a) = Df(a)[u]$$.

This proves that the existence of the differential at $a$ implies the existence of all directional derivatives at $a$. In

7. TODO: Prove diff @ a implies cont @ a
