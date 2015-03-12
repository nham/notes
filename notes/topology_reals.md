1. An **interval** of $\mathbb{R}$ is a subset $I$ such that for all $a, b \in I$, $a < x < b$ implies that $x \in I$. This includes as degenerate cases singletons and the empty set.

2. Every interval is connected. *Proof:* We can clearly ignore degenerate cases, they are connected. Suppose $A$ and $B$ are a disconnection of $I$. There is some $a \in A$, $b \in B$. WLOG we assume $a < b$. Then interval $[a, b]$ has to be contained in $I$.
Consider $c := \inf \{ x \in B : a < x \}$, which is valid since $a$ is a lower bound of the set. $c$ has to be a boundary point of $A$ (and $B$), because

     - every open ball centered at $c$ must intersect $A$ (if one did not,it would contradict the definition of $c$ since we could find elements of the set smaller than $c$)

     - every open ball centered at $c$ must also intersect $B$ by definition of infimum (if one did not, we could find a greater lower bound)

    But $A$ and $B$ are open, and so do not contain boundary points. But they also cover $I$, so one of them must contain $c$. This is a contradiction.

3. Conversely, any connected subset $S$ of $\mathbb{R}$ must be an interval. We again neglect the case of $S$ with less than two points. If $S$ is connected and contains $a, b$ with $a < b$ and is missing some $x$ with $a < x < b$, then $(- \infty, x) \cap I$ and $(x, \infty) \cap I$ are together a disconnection of $I$.

4. The **intermediate value theorem** says that if $X$ is a connected topological space and $f: X \to \mathbb{R}$ is continuous, then for any $a, b \in X$, WLOG supposing $f(a) \leq f(b)$, we have that for every $z \in \mathbb{R}$ with $f(a) < z < f(b)$, there is a $c \in X$ such that $f(c) = z$. This is because the image of $f$ must be a connected subset of $\mathbb{R}$, which we have just proven must be an interval.

5. There are two ways to view the standard topology on $\mathbb{R}$: either as the metric topology induced by $d(x, y) := |x - y|$, or as the order topology on $\mathbb{R}$. This latter characterization is equivalent to the former due to the fact that the basis for the order topology is the same as the open balls of the metric space: the collection of all open intervals $(a, b)$.

6. Here's a neat/useful fact about $\mathbb{R}$: every open subset $U$ of $\mathbb{R}$ is the disjoint union of countable open intervals. One proof goes like this: we partition $U$ by defining an equivalence relation $x \sim y$ iff $[\min{x,y}, \max{x,y}] \subseteq U$. It's easy to prove this really is an equivalence relation. Furthermore the equivalence classes are intervals because if $a \sim b$ with $a < b$, for any $x \in U$ with $a < x < b$, by definition $x \in [a, b] \subseteq U$ so $x$ is in the same equivalence class. What's more, they must be *open intervals* because if there's an inclusive end point, that implies that $U$ contains a boundary point, contrary to it being open.

    So we've just shown that $U$ has a partition of open intervals. But it is a basic theorem that between any two real numbers is a rational number. So pick a rational number in each open interval. This gives an injective map from intervals to rationals, proving the collection of partition elements is countable.

7. There's a homeomorphism between $(-1, 1) \subseteq \mathbb{R}$ and $\mathbb{R}$ itself. First: prove that $f: (-1, 1) \to \mathbb{R}$ defined by

    $$f(x) := \frac{x}{1 - |x|}$$

    is strictly monotone ($x < y$ implies $f(x) < f(y)$), which can be done by first proving it true for all $0 \leq x < y$ and all $x < y \leq 0$, and then proving for $x < 0 < y$. Then, by monotonicity, the inverse image of any open interval in $\mathbb{R}$ is another open interval, which establishes that $f$ is continuous (the inverse image of any basis set of $\mathbb{R}$ is open in $(-1, 1)$).

    Now, $f$ has an inverse $g: \mathbb{R} \to (-1, 1)$ defined by

    $$g(x) := \frac{x}{1 + |x|}$$

    So $f$ is bijective. Finally, $g$ must be strictly monotone as well, and the subspace basis for $(-1, 1)$ is just the open intervals contained in $(-1, 1)$, so by monotonicity again the preimage of any open interval is another open interval, blah blah $g$ is continuous.

8. Stretching $\mathbb{R}$ is a homeomorphism: the map $f: \mathbb{R} \to \mathbb{R}$ defined by $x \mapsto cx$ for $c \neq 0$ is a homeomorphism on $\mathbb{R}$. *Proof:* It suffices to prove that $f$ is continuous, since each such $f$ is bijective and its inverse is also a stretching map. When $c > 0$, $f$ is a strictly monotone function ($a < b$ implies $ca < cb$), so $f^{pre}((a, b)) = (a/c, b/c)$. When $c < 0$, $f$ is strictly anti-monotone or whatever you'd call that, so again the preimage of any open interval is another open interval.

9. Translation of $\mathbb{R}$ is a homeomorphism, for basically the same reason that stretching was: the inverse image of any open interval $(a, b)$ under translation by $z$ is the open interval $(a - z, b - z)$.

10. From the previous two notes we have that stretching/translating $\mathbb{R}^n$ is a homeomorphism since they can both be thought of as a product map of the single-variable streches/translations.

11. Any two open balls in $\mathbb{R}^n$ are homeomorphic. To prove this, it suffices to prove that $B(a; \epsilon)$ and $B(0; 1)$ are homeomorphic for any $a$ and $\epsilon$. But this is easy to see: $B(a; \epsilon)$ and $B(0; \epsilon)$ are homeomorphic via a restriction of a translation map on $\mathbb{R}$, and $B(0; \epsilon)$ and $B(0; 1)$ are homeomorphic via a restriction of the stretching map. Since the composition of homeomorphisms is a homeomorphism, we are done.


12. The **extended real numbers** are the system of numbers you get by adding $\infty, -\infty$ to $\mathbb{R}$. Let's denote the set by $\bar{\mathbb{R}}$. We can extend the ordering on $\mathbb{R}$ so that

    $$-\infty < x < \infty$$

    for all finite $x$, making $\bar{\mathbb{R}}$ totally ordered.

13. Of course, the extended real line being totally ordered means it has a topology on it, courtesy of the order topology.

14. $\mathbb{R}$ is dense in $\bar{\mathbb{R}}$ because every every non-empty open subset of $\bar\{\mathbb{R}}$ contains some basis set, and each basis set contains a finite real.

    Not only that, but the subspace topology on $\mathbb{R}$ relative to $\bar{\mathbb{R}}$ is just the standard topology on $\mathbb{R}$ because the subspace basis of $\mathbb{R}$ consists of all open intervals $(a, b)$ with $a$ and $b$ finite and all intervals $(a, \infty)$, and $(-\infty, a)$ for finite $a$. These are all open in the standard topology on $\mathbb{R}$, and this is a superset of the standard metric basis, so subspace basis induces the standard topology.


15. $\bar{\mathbb{R}}$ is homeomorphic with $[-1, 1]$: using the $f$ and $g$ as above for homeomorphisms between $(-1, 1)$ and $\mathbb{R}$, we extend it by mapping $-1 \leftrightarrow -\infty$ and $1 \leftrightarrow \infty$. Then the basis sets of $\bar{\mathbb{R}}$ involving $\infty$ or $-\infty$ have preimages of $(a, 1]$ or $[-1, a)$ for some $a \in (0, 1)$, which are clearly open in $[-1, 1]$. Similarly the preimages of open intervals in $[-1, 1]$ involving $-1$ or $1$ will be the half-open intervals involving $-\infty$ or $\infty$. So this is a homeomorphism.

16. A corollary is that the extended reals are compact (since closed intervals in $\mathbb{R}$ are). So the extended reals are a compactification of $\mathbb{R}$.
