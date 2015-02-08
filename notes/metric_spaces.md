---
title: Metric spaces
---
Related notes: [basic topology](basic_topology.html)

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

6. Every Cauchy sequence with a convergent subsequence itself converges. To see this, let $(x_{n_k})$ be the convergent subsequence (with limit $a$) and let $\epsilon > 0$.

     1. $(x_n)$ is Cauchy, so some tail sequence starting at, say, $N$, has all terms within $\epsilon/2$ of one another. 
     2. It would suffice to find a term that is a) within the $\epsilon/2$ ball around $a$, and b) in the tail sequence of $(x_n)$ starting at $N$. Any such term would (by the triangle inequality) prove that all terms of $(x_n)$ starting at $N$ are within $\epsilon$ of $a$.
     3. But there are infinitely many terms in the subsequence that are within $\epsilon/2$ of $a$, so surely there is one that comes after $N$.

7. A metric space is **complete** if every Cauchy sequence converges. So in complete metric spaces, a sequence converges iff it is Cauchy. The standard example of a complete metric space is $\mathbb{R}$, which is complete pretty much by construction (in fact, one way of building the reals from the rationals is as equivalence classes of Cauchy sequences of rational numbers. This can be thought of as adding in all the missing limits for rational Cauchy sequences).

8. A subset of a metric space is **bounded** if it is contained in some open ball. In this case we can define the **diameter** of a bounded set to be the supremum of the set of distances between any two points in the set. (We can also define the diameter of unbounded sets to be $\infty$ using the extended reals)

9. A map $f: X \to Y$ between metric spaces is **continuous** at $a$ if for every open ball in $Y$ around $f(a)$, there is an open ball in $X$ around $a$ that $f$ maps into the first open ball. This is the standard $\epsilon-\delta$ definition in different clothes. See the topology notes for further deets.

10. One interesting characterization of continuous maps is as *locally approximately constant* maps. (The following is non-standard. I have not seen it anywhere, I made it up). Let's say that a map $f$ is **locally approximately constant at $a$ of tolerance $\epsilon$** ($\epsilon > 0$) if there is a neighborhood around $a$ such that when $f$ is restricted to that neighborhood, the output is always within $\epsilon$ of $f(a)$.
    
    If we further say that $f$ is **locally approximately constant at $a$** if it is locally approximately constant at $a$ of tolerance $\epsilon$ for all $\epsilon > 0$, then **locally approximately constant** maps are exactly continuous maps.
