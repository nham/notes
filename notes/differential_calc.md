---
title: Differential calculus
---

1. If $f: D \to \mathbb{R}^k$ where $D \subseteq \mathbb{R}^n$, then a **derivative** of $f$ at $a$ for any interior point $a$ of $D$ is defined to be any map $L: \mathbb{R}^n \to \mathbb{R}^k$ such that

    $$lim_{h \to 0} \frac{f(a+h) - f(a) - L(h)}{|h|} = 0$$

    Equivalently, the function $\boldsymbol \epsilon (h) := f(a+h) - f(a) - L(h)$ has $\frac{\boldsymbol \epsilon(h)}{|h|} \to 0$ as $h \to 0$.

2. The derivative is always unique. This is proved via a lemma: if $T: \mathbb{R}^n \to \mathbb{R}^k$ is linear and such that $\frac{T(h)}{|h|} \to 0$ as $h \to 0$, then $T$ is the zero map. After this, if we have any two derivatives $L$ and $M$ of $f$ at $a$, then it can be proved that $L - M$ has the above property and so must be the zero map, establishing $L = M$. We notate this unique map by $Df(a)$, called **the differential of $f$ at $a$**.

3. Note that if $f$ is real-valued, the derivative of $f$ at any $a$ is a covector (element of the dual space) of $\mathbb{R}^n$.

4. The **directional derivative** in direction $u$ of some $f$ at $a \in \text{int} \text{ dom} f$, where $|u| = 1$, is defined to be

    $$D_u f(a) := lim_{t \to 0} \frac{(f(a+tu) - f(a)}{t}$$

    if it exists.

    Note that as we have defined it, the $u$-th directional derivative of f at $a$, $D_u f(a)$, is a vector in $\mathbb{R}^k$ (scalar in the case of $k = 1$) and not a function, in contrast to total derivatives. Of course, we can always consider for any $v \in \mathbb{R}^k$ as a function $\mathbb{R} \to \mathbb{R}^k$ defined by scalar multiplication $x \mapsto x \cdot v$.

    In particular, the directional derivatives for $e_1, \ldots, e_n$, the standard basis vectors of $\mathbb{R}^n$, are denoted $D_1 f, \ldots, D_n f$, each one $D_i$ being called **the $i$-th partial derivative**.

5. Consider the case of real-valued $f$. We can view the graph of $f$ as a subset of $\mathbb{R}^{n+1}$, an $n$-dimensional differentiable manifold of some sort. Then the derivative can be thought of, geometrically, as the **tangent hyperplane** to the surface at $a$. This is why some books occasionally talk about "affine approximation" in conjunction with derivatives: you are locally approximating some $n$-dimensional surface with a certain affine subspace (an affine hyperplane, specifically).

6. $D_u f(a) = Df(a)[u]$ for any direction $u$. We can see this by noting that since

    $$\boldsymbol \epsilon(h) = f(a+h) - f(a) - Df(a)[h]$$

    is true for sufficiently small $h$, we must have

    $$\boldsymbol \epsilon(tu) = f(a+tu) - f(a) - t Df(a)[u]$$

    Since $\frac{ \boldsymbol \epsilon(h) }{ |h| } \to 0$ as $h \to 0$, we similarly have $\frac{ \boldsymbol \epsilon(tu) }{ |tu|} \to 0$ as $t \to 0$. This implies that $\frac{ \boldsymbol \epsilon(tu) }{ |t| } \to 0$ as $t \to 0$, which further implies

    $$lim_{t \to 0} \frac{ \boldsymbol \epsilon(tu) }{ t } = 0$$

    But $lim_{t \to 0} \frac{ \boldsymbol \epsilon(tu) }{ t } = lim_{t \to 0} \frac{ f(a+tu)-f(a) }{t} - Df(a)[u] = 0$, so

    $$D_u f(a) = Df(a)[u]$$.

    This proves that the existence of the differential at $a$ implies the existence of all directional derivatives at $a$. In

7. If $Df(a)$ exists, then $f$ is continuous at $a$.

    One proof uses the operator norm $\|T\| := \inf \{c \geq 0 : \forall v, |Tv| \leq c |v|\}$ defined for any linear map $T$. This is always finite for linear maps between finite dimensional spaces (TODO: proof isn't in notes?)

    We proceed: since $Df(a)$ exists, we have that

    $$\epsilon_a(h) := f(a+h) - f(a) - Df(a)[h]$$

    is such that $\frac{\epsilon_a(h)}{|h|} \to 0$ as $h \to 0$.

    Let's write $\triangle_h f(a) := f(a+h) - f(a)$. So we have

    $$\triangle_h f(a) = Df(a)[h] + \epsilon_a(h)$$

    And hence by the triangle inequality,

    $$|\triangle_h f(a)| \leq \|Df(a)\| |h| + |\epsilon_a(h)|$$

    From the assumed properties of $\epsilon_a$, we can pick a $\delta > 0$ such that $|\epsilon_a(h)| < |h|$ for all $h$ with $0 < |h| < \delta$. So for any $\epsilon > 0$, if we take $h$ such that

    $$0 < |h| < \min \{\delta, \frac{\epsilon}{1 + \|Df(a)\|} \}$$

    then we must have

    $$|\triangle_h f(a)| < \epsilon$$

    This proves we can always find an input neighborhood around $a$ on which the output of $f$ is arbitrarily close to $f(a)$.

8. When the derivative of $f$ exists everywhere on some neighborhood $U$, then we can consider $Df$ as a function $U \to \mathcal{L}(\mathbb{R}^n, \mathbb{R}^k)$. This function $Df$ need not be continuous: consider 

    TODO: give an example

9. The mean value theorem from calculus is this: given $f: [a, b] \to \mathbb{R}$ which is continuous on $[a, b]$ and differentiable on $]a, b[$, there must exist a $c \in ]a, b[$ such that

    $$f(b)-f(a) = f'(c) (b - a)$$

    This can be extended to multivariable functions. Given any $f: A \to \mathbb{R}$ where $A \subseteq \mathbb{R}^n$, if $a, h \in \mathbb{R}^n$ are such that the line segment $[a, a+h] \subseteq A$, if $f$ is continuous on $[a, a+h]$ and differentiable on $]a, a+h[$, then we again have a $c \in ]a, a+h[$ such that

    $$f(a+h)-f(a) = D[f @ c] \circ (\lambda \mapsto \lambda h)$$

    The above is proved via the single variable MVT and the chain rule applied to $\phi(t) := f(a + th)$.

10. A function $f: A \to \mathbb{R}^k$ with $A \subseteq \mathbb{R}^n$ and $A$ being open, is said to be **$C^0$** if $f$ is continuous on $A$. It is instead said to be **$C^1$** if every partial derivative $D_j f_i: A \to \mathbb{R}$ exists is a $C^0$ function on $A$, where $f_1, \ldots, f_k$ are the real-valued component functions of $f$.

    In general, a function $f$ as above is said to be **$C^k$** whenever each of its partial derivatives $D_j f_i$ exists and is $C^{k-1}$ on $A$.

    Some sources define $C^k$ as having $k$-derivatives at every point of the domain. My guess is that these two definitions are equivalent, given that it is proved, both in Munkres and Fleming, that $C_1$ implies differentiable (the other direction holds immediately).
