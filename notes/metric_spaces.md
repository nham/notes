---
title: Metric spaces
---
Related notes: All the topology notes.

1. A metric space is a pair $(X, d)$ where $d: X^2 \to \mathbb{R}$ is a function (called a **metric**) that obeys

     - $d(x,y) \geq 0$ for all $x,y$ and $d(x, y) = 0$ iff $x = y$
     - $d(x, y) = d(y,x)$
     - $d(x, z) \leq d(x,y) + d(y,z)$

    This is just a formal way of saying that any pair of two points has a non-negative real number assigned to it, which can be thought of as the *distance* between the points under the metric, such that the triangle inequality (the third property) is obeyed.

    The standard example is $\mathbb{R}$ with $d(x,y) := |x - y|$ ($| \cdot |$ is the absolute value). More generally, we can consider $\mathbb{R}^n$ with the **Euclidean metric** $d(x, y) := |x - y|$, where $| \cdot |$ is now the (vector) norm induced by the standard dot product.

2. Metric spaces have a well-defined topology on them called the **metric space topology**. Let $X$ be any metric space. We start out by defining the **open ball centered at $a$ of radius $r$** to be:

    $$B(a; r) := \{ x \in X : d(x, a) < r\}$$

    Also define the **closed ball centered at $a$ of radius $r$** to be:
    
    $$C(a; r) := \{ x \in X : d(x, a) \leq r\}$$

    (We will sometimes use subscripts like $B_X(a; r)$ or $B_d(a; r)$ when talking about open balls in different metric spaces or under different metrics on the same space.)

    The open sets of the metric space topology are defined to be all sets $S$ for which every point $x \in S$ has some open ball centered at $x$ that is contained in $S$.

    (We're really using the open balls as a basis for the metric space topology here).


3. Sequence convergence in metric spaces is defined in a way similar to that of topological spaces: $(x_n) \to a$ when every open ball centered at $a$ contains all but finitely many terms of the sequence. $a$ is said to be the **limit** of the sequence $(x_n)$

    I have found it useful to think about **tail sequences**. A tail sequence of some given sequence $(x_n)_{n \in \mathbb{N}}$ is the sequence starting at some $k \in \mathbb{N}$. I.e. the sequence $(x_n)_{n \geq k}$. $(x_n)$ converging to $a$ can be re-stated as saying every open ball centered at $a$ contains some tail sequence of $(x_n)$.

    A **subsequence** of sequence $(x_n)$ is any sequence $(x_{n_k})$ for some injective mapping $k \to n_k$. Intuitively it is the original sequence with some of the terms possibly removed and the order untouched.

4. Limits are unique because metric spaces are Hausdorff: if $x, y \in X$ are distinct, then the open balls $B(x; \epsilon / 2)$ and $B(y; \epsilon / 2)$ are disjoint, where $\epsilon := d(x, y)$.

5. A **Cauchy sequence** is a sequence $(x_n)$ such that for every $\epsilon > 0$, there is some tail sequence of $(x_n)$ where all the terms are within an $\epsilon$ of one another.

    Intuitively, this is a sequence where the terms get closer and closer to one another as $n \to \infty$. If you've never seen this before, you're probably confused about the difference betwen Cauchy sequences and convergent sequences. Indeed, every convergent sequence is Cauchy: to find a tail sequence with all terms within an $\epsilon$ of one another, take the tail sequence contained in the open ball of radius $\epsilon / 2$ centered at the limit. By the triangle inequality any two terms are within an $\epsilon$ of one another.

    The reason Cauchy sequences were invented was to talk about metric spaces with "missing points", that is spaces that contain sequences whose terms get arbitrarily close to one another and yet do not converge to any limit. The common example is the sequence of decimal expansions of $\sqrt{2}$:

    $$(1, 1.4, 1.41, 1.414, 1.4142, 1.41421, 1.414213, ...)$$

    These are all rational, so this is a sequence in $\mathbb{Q}$. This is certainly a Cauchy sequence. However, it does not converge in $\mathbb{Q}$ because $\sqrt{2}$ is not rational.

6. Every Cauchy sequence with a convergent subsequence itself converges.

    To see this, note that if there's a convergent subsequence, then for every $\epsilon > 0$ there are infinitely many terms of the sequence that are within $\epsilon/2$ of some point $a$. But by Cauchy-ness there's always a point in the sequence after which all terms are within an $\epsilon/2$ of one another. So we can find some term $x_m$ such that a) $d(x_m, a) < \epsilon/2$, and b) d(x_m, x_n) < \epsilon/2$ for all terms $x_n$ in some tail sequence. By the triangle inequality, all terms of this tail sequence are within an $\epsilon$ of $a$.

7. A metric space is **complete** if every Cauchy sequence converges. So in complete metric spaces, a sequence converges iff it is Cauchy. The standard example of a complete metric space is $\mathbb{R}$, which is complete pretty much by construction (in fact, one way of building the reals from the rationals is as equivalence classes of Cauchy sequences of rational numbers. This can be thought of as adding in all the missing limits for rational Cauchy sequences).

8. A subset of a metric space is **bounded** if it is contained in some open ball. In this case we can define the **diameter** of a bounded set to be the supremum of the set of distances between any two points in the set. (We can also define the diameter of unbounded sets to be $\infty$ using the extended reals)

9. A map $f: X \to Y$ between metric spaces is **continuous** at $a$ if for every open ball in $Y$ around $f(a)$, there is an open ball in $X$ around $a$ that $f$ maps into the first open ball. This is the standard $\epsilon-\delta$ definition in different clothes. See the topology notes for further deets.

10. One interesting characterization of continuous maps is as *locally approximately constant* maps. (The following is non-standard. I have not seen it anywhere, I made it up). Let's say that a map $f$ is **locally approximately constant at $a$ of tolerance $\epsilon$** ($\epsilon > 0$) if there is a neighborhood around $a$ such that when $f$ is restricted to that neighborhood, the output is always within $\epsilon$ of $f(a)$.
    
    If we further say that $f$ is **locally approximately constant at $a$** if it is locally approximately constant at $a$ of tolerance $\epsilon$ for all $\epsilon > 0$, then **locally approximately constant** maps are exactly continuous maps.

11. An **isometry** is any map between metric spaces that preserves distance: $d_X(a, b) = d_Y(f(a), f(b))$ for all $a, b \in X$. Every isometry $f$ is a topological embedding:

     - it is injective since $f(a) = f(b)$ implies that $d_X(a, b) = 0$, which implies that $a = b$
     - it is continuous since for any $x$, any $a$ within $\epsilon$ of $x$ will have $f(a) also within $\epsilon of $f(x)$
     - letting $g: X \to f(X)$ be the codomain restriction of $f$, letting $u, v \in Y$ and $a = g(u)$, $b = g(v)$, we have $d_Y(u, v) = d_Y(f(a), f(b)) = d_X(a, b) = d_X(g(u), g(v))$, so $g$ is also an isometry, hence continuous.

12. Different metrics on the same set can nevertheless induce the same metric topologies. We say that two such metrics are **topologically equivalent**. Metrics are topologically equivalent iff the open balls *nest*, meaning for every $x \in X$ and every $\epsilon > 0$, there are $\delta, \gamma > 0$ such that

    $$B_1(x; \delta) \subseteq B_2(x; \epsilon), B_2(x; \gamma) \subseteq B_1(x; \epsilon)$$

    Proof: Nesting open balls implies the same topology since every $1$-open set $U$ is a union of $1$-open balls, so by nesting $U$ will be a union of $2$-open balls as well (and vice versa). Conversely if the topologies are the same, every $1$-open ball  will be $2$-open, hence some $2$-open ball centered at the point will be contained in the $1$-open ball (and vice versa).


13. If two metrics $d_1$ and $d_2$ on a space are topologically equivalent, then a sequence $(x_n)$ converges to $a$ in $1$ iff it converges to $a$ in $2$. The proof: If every $1$-open ball around $a$ contains some tail sequence, then for any $2$-open ball around $a$ there's a $1$-open ball around $a$ nested inside the $2$-open ball, and that $1$-open ball contains a tail sequence, so the $2$-open ball does as well. The converse clearly holds.


14. For any metric spaces $X$ and $Y$, a sequence $(f_n)$ of functions $f_n: X \to Y$ is said to **converge pointwise** to $g: X \to Y$ if each sequence $(f_n(x))$ for $x \in X$ converges to $g(x)$. Think of it like slicing the functions in the sequence by input value. If each sliced sequence converges to each value of $g$, then $(f_n)$ converges pointwise to $g$.

    A sequence $(f_n)$ is alternatively said to **converge uniformly** to $g: X \to Y$ if $\forall \epsilon > 0$ there is an $N \in \mathbb{N}$ such that $\sup \{d_Y(f_n(x), g(x)) : x \in X\} < \epsilon$ for all $n \geq N$. The value $\sup \{d_Y(f_n(x), g(x)) : x \in X\}$ can be thought of as the max distance between outputs of $f_n$ and $g$ across all inputs.

    In fact we can define $U[f, g] := \sup \{d_Y(f(x), g(x)) : x \in X\}$ for all $f, g: X \to Y$. Note that this is not quite a metric, since $U[f, g]$ might not be finite. Still, we can reformulate our definition above using the idea behind Cauchy sequences: $(f_n)$ converges uniformly to $g$ iff for all $\epsilon > 0$ there is an $N \in \mathbb{N}$ such that $U[f_n, f_m] < \epsilon$ for all $m, n \geq N$.

15. Excuse me while I shove this in here. A subset $A$ of a metric space is **totally bounded** if for every $\epsilon > 0$ a finite number of open balls of radius $\epsilon$ cover $A$. Every totally bounded set is bounded since there are points $x_1, \ldots, x_n$ that are the centers of balls of radius $1$ that cover the space, so every point is within $max \{1, d(x_1, x_2) + 1, \ldots, d(x_1, x_n) + 1\}$ of $x_1$ by the triangle inequality.

    For an example of a bounded set that is not totally bounded, consider any infinite subset of a metric space under the discrete metric. The set is contained in any ball of radius $2$, but every ball of radius $1/2$ contains only a single point, and so no finite collection of them cover the set.


16. Here's a sequential characterization of closed subsets that are useful: a subset $S$ of a metric space is closed iff every sequence in $S$ that converges in $X$ has its limit in $S$.

    The proof: If $S$ is closed, the limit of any sequence in $S$ is a closure point of the term set, so the limit must be contained in $S$. Conversely, if $S$ is not closed, it lacks a closure point $a$. We can build a sequence in $S$ that converges to $a$ by picking points in $S$ that are in $B(a; 1)$, $B(a; 1/2)$, $B(a; 1/3)$, $\ldots$, which all must exist because $a$ is a closure point.

17. A function $f: X \to Y$ between metric spaces is **uniformly continuous** if for every $\epsilon > 0$, there's a $\delta > 0$ such that for *all* $x \in X$, $f(B(x; \delta)) \subseteq B(f(x); \epsilon)$. The difference from mere continuity is that the same $\delta$ works for *every $x$* in uniform continuity, whereas $\delta$ is dependent on $x$ under continuity.

18. A function $f: X \to Y$ between metric spaces is **Lipschitz continuous** with **Lipschitz constant $K \geq 0$** when $d_Y(f(a), f(b)) \leq K d_X(a, b)$ for all $a, b \in X$.

19. Every Lipschitz continuous map is uniformly continuous, since for any $\epsilon$ and any $x \in X$, if $d_X(a, x) < \epsilon/K$ then $d_Y(f(a), f(x)) < \epsilon$.

20. A **contraction map** is any Lipschitz continuous map where the domain and the codomain are equal and the Lipschitz constant $K$ has $0 \leq K < 1$.

21. If $X, Y$ are metric spaces, $X$ compact and $f: X \to Y$ continuous, then $f$ must additionally be uniformly continuous. *Proof:* Since $f$ is continuous, for every $\epsilon$ and $x \in X$ there's a $\delta_x$ such that

    $$f[B(x; \delta_x)] \subseteq B(f(x); \epsilon / 2)$$

    If we now consider the collection of balls $B(x; \delta_x / 2)$, this is an open cover of $X$, so by compactness a finite number of them $B(x_i; \delta_{x_i} / 2)$ cover $X$. Consider defining

    $$\delta := \min\{ \delta_{x_i} : 1 \leq i \leq n\}$$

    Now for any $a \in X$, $a$ is in some $B(x_i; \delta_{x_i} / 2)$ so $d(a, x_i) < \delta_{x_i} / 2$ \leq \delta_{x_i} - \delta$, which proves (see (23)) $B(a; \delta)$ is contained in $B(x_i; \delta_{x_i})$.

    This establishes that for all $y \in B(a; \delta)$, we have $d(f(a), f(x) < \epsilon / 2$ and $d(f(y), f(x)) < \epsilon / 2$, so by the triangle inequality $d(f(y), f(x)) < \epsilon$. This proves uniform continuity.


22. Two open balls $B(x; r)$ and $B(y; s)$ are disjoint when $r+s \leq d(x,y)$. This is because

    $$d(x,y) \leq d(x, a) + d(a, y)$$

    for any $a$, so if there were some $a$ in both balls we'd have $d(x, y) < r + s$.

23. One open ball $B(x; r)$ is contained in another $B(y; s)$ when $d(x,y) \leq s - r$. We reason again by the triangle inequality: for all $a \in B(x; r)$, we have

    $$d(y,a) < r + d(x,y)$$

    So the condition just stated suffices.
