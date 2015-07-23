5. There are two ways to view the standard topology on $\mathbb{R}$: either as the metric topology induced by $d(x, y) := |x - y|$, or as the order topology on $\mathbb{R}$. This latter characterization is equivalent to the former due to the fact that the basis for the order topology is the same as the open balls of the metric space: the collection of all open intervals $(a, b)$.

7. There's a homeomorphism between $(-1, 1) \subseteq \mathbb{R}$ and $\mathbb{R}$ itself. First: prove that $f: (-1, 1) \to \mathbb{R}$ defined by

    $$f(x) := \frac{x}{1 - |x|}$$

    is strictly monotone ($x < y$ implies $f(x) < f(y)$), which can be done by first proving it true for all $0 \leq x < y$ and all $x < y \leq 0$, and then proving for $x < 0 < y$. Then, by monotonicity, the inverse image of any open interval in $\mathbb{R}$ is another open interval, which establishes that $f$ is continuous (the inverse image of any basis set of $\mathbb{R}$ is open in $(-1, 1)$).

    Now, $f$ has an inverse $g: \mathbb{R} \to (-1, 1)$ defined by

    $$g(x) := \frac{x}{1 + |x|}$$

    So $f$ is bijective. Finally, $g$ must be strictly monotone as well, and the subspace basis for $(-1, 1)$ is just the open intervals contained in $(-1, 1)$, so by monotonicity again the preimage of any open interval is another open interval, blah blah $g$ is continuous.

8. Every open ball in $\mathbb{R}^n$ is homeomorphic to $\mathbb{R}^n
$B(0; 1)$ in $\mathbb{R}^n$ is homeomorphic to $\mathbb{R}^n$.

    *Proof:* Define $f: B(0; 1) \to \mathbb{R}^n$ by $f(x) = x/(1 - |x|)$, where $| \cdot |$ denotes the norm on $\mathbb{R}^n$. Then for any $x, y \in B(0; 1)$,

    $$|f(y) - f(x)| = |y/(1 - |y|) - x/(1 - |x|)|$$

    If we let $X = 1 - |x|$ and $Y = 1 - |y|$, we can rewrite this as

    $$|f(y) - f(x)| = |y/Y - x/X| = |Xy - Yx| / XY$$

    since $X, Y > 0$. But this equals

    $$|Xy - Xx + Xx - Yx| / XY \leq |y - x| / Y + |X - Y| |x| / XY$. We can simplify this by noting that $|X - Y| = |1 - |x| - 1 + |y|| = ||y| - |x|| \leq |y - x|$ by the reverse triangle inequality, so

    $$|f(y) - f(x)| \leq |y - x| / Y + |y - x| |x| / XY = |y - x| / XY$$

    Now, supposing $\delta > 0$ and $|y - x| < \delta$, we have $|y| \leq |x| + |y - x| < |x| + \delta$, so $Y > 1 - |x| - \delta = X - \delta$. Thus for all $y$ with $|y - x| < \delta$,

    $$|f(y) - f(x)| < \delta / X(X - \delta)$$

    Since the part on the right side of the inequality goes to zero as $\delta$ goes to zero, we can choose $\delta$ small enough to make

    $$\delta / X(X - \delta) < \epsilon$$

    for every $x$. This proves that $f$ is continuous. To prove it is a bijection, define $g: \mathbb{R}^n \to B(0; 1)$ by $g(x) = x / (1 + |x|)$. Then $g(f(x)) = [x/(1 - |x|)] / (1 + |x| / (1 - |x|)) = [x/(1 - |x|)] / (1 / (1 - |x|)) = x$ and $f(g(x)) = [x/(1 + |x|)] / (1 - |x| / (1 + |x|)) = x$, so they are inverses.

    Finally, we must prove that $g$ is continuous. But for any $y$, letting $X = 1 + |x|$ and $Y = 1 + |y|$, we have $|g(y) - g(x)| = |y/Y - x/X| = |Xy - Yx| / XY$. This is the same expression as for $f$, so $|g(y) - g(x)| \leq |y - x| / XY$. Here, however, $1 / Y < 2$ for all $y$ since $|y|$ is always positive, so $|g(y) - g(x)| < 2 |y - x| / X$. So for all $y$ with $|y - x| < \epsilon X / 2$, $|g(y) - g(x)| < \epsilon$.


9. Stretching $\mathbb{R}$ is a homeomorphism: the map $f: \mathbb{R} \to \mathbb{R}$ defined by $x \mapsto cx$ for $c \neq 0$ is a homeomorphism on $\mathbb{R}$. *Proof:* It suffices to prove that $f$ is continuous, since each such $f$ is bijective and its inverse is also a stretching map. When $c > 0$, $f$ is a strictly monotone function ($a < b$ implies $ca < cb$), so $f^{pre}((a, b)) = (a/c, b/c)$. When $c < 0$, $f$ is strictly anti-monotone or whatever you'd call that, so again the preimage of any open interval is another open interval.

10. Translation of $\mathbb{R}$ is a homeomorphism, for basically the same reason that stretching was: the inverse image of any open interval $(a, b)$ under translation by $z$ is the open interval $(a - z, b - z)$.

11. From the previous two notes we can establish that stretching/translating $\mathbb{R}^n$ is a homeomorphism since they can both be thought of as a product map of the single-variable streches/translations.

12. Any two open balls in $\mathbb{R}^n$ are homeomorphic. To prove this, it suffices to prove that $B(a; \epsilon)$ and $B(0; 1)$ are homeomorphic for any $a$ and $\epsilon$. But this is easy to see: $B(a; \epsilon)$ and $B(0; \epsilon)$ are homeomorphic via a restriction of a translation map on $\mathbb{R}$, and $B(0; \epsilon)$ and $B(0; 1)$ are homeomorphic via a restriction of the stretching map. Since the composition of homeomorphisms is a homeomorphism, we are done.


13. The **extended real numbers** are the system of numbers you get by adding $\infty, -\infty$ to $\mathbb{R}$. Let's denote the set by $\bar{\mathbb{R}}$. We can extend the ordering on $\mathbb{R}$ so that

    $$-\infty < x < \infty$$

    for all finite $x$, making $\bar{\mathbb{R}}$ totally ordered.

14. Of course, the extended real line being totally ordered means it has a topology on it, courtesy of the order topology.

15. $\mathbb{R}$ is dense in $\bar{\mathbb{R}}$ because every every non-empty open subset of $\bar\{\mathbb{R}}$ contains some basis set, and each basis set contains a finite real.

    Not only that, but the subspace topology on $\mathbb{R}$ relative to $\bar{\mathbb{R}}$ is just the standard topology on $\mathbb{R}$ because the subspace basis of $\mathbb{R}$ consists of all open intervals $(a, b)$ with $a$ and $b$ finite and all intervals $(a, \infty)$, and $(-\infty, a)$ for finite $a$. These are all open in the standard topology on $\mathbb{R}$, and this is a superset of the standard metric basis, so subspace basis induces the standard topology.


16. $\bar{\mathbb{R}}$ is homeomorphic with $[-1, 1]$: using the $f$ and $g$ as above for homeomorphisms between $(-1, 1)$ and $\mathbb{R}$, we extend it by mapping $-1 \leftrightarrow -\infty$ and $1 \leftrightarrow \infty$. Then the basis sets of $\bar{\mathbb{R}}$ involving $\infty$ or $-\infty$ have preimages of $(a, 1]$ or $[-1, a)$ for some $a \in (0, 1)$, which are clearly open in $[-1, 1]$. Similarly the preimages of open intervals in $[-1, 1]$ involving $-1$ or $1$ will be the half-open intervals involving $-\infty$ or $\infty$. So this is a homeomorphism.

17. A corollary is that the extended reals are compact (since closed intervals in $\mathbb{R}$ are). So the extended reals are a compactification of $\mathbb{R}$.


18. I'm assuming it to be well-known that the rationals are dense in the reals, which makes $\mathbb{R}$ separable and hence second-countable (every separable metric space is second-countable). To prove that $\mathbb{Q}^n$ is dense in $\mathbb{R}^n$, we use the fact that the Euclidean norm and $\infty$-norm induce the same topology. Then every open subset of $\mathbb{R}^n$ contains some open box, the open box is a product of closed intervals, each of which contains a rational number. So the product contains a tuple of rationals, i.e. an element of $\mathbb{Q}^n$. This proves that $\mathbb{R}^n$ is separable and hence second-countable.

19. $\mathbb{R}^n$ is clearly path-connected (consider $a, b \in \mathbb{R}^n$. then $t \mapsto a + t(b-a)$ is a path from $a$ to $b$).

    Any open ball is path-connected as well, which is a consequence of open balls being convex. The proof is not tricky: if $a, b \in B(x; \epsilon)$ and $0 \leq t \leq 1$, then $|a + t(b-a) - x| = |(1-t)(a-x) + t(b-x)| \leq (1-t) |a-x| + t |b-x| < \epsilon$.
