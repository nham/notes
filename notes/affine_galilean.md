---
title: Affine spaces and Galilean spacetime
---
1. A **torsor** is a "group that has forgotten its origin". More formally, for any group $G$, a **$G$-torsor** is any set $X$ equipped with a group action $\phi$ of $G$ on $X$ (a group homomorphism $\phi: G \to \text{Sym } X$) that obeys this property:

    for all $a, b \in X$, there is exactly one $g \in G$ such that $g(a) = b$.

    This condition implies that the group action is faithful (the homomorphism $G \to Sym X$ is injective), so that a $G$-torsor on $X$ can alternatively be thought of as a set $X$ and a group of permutations of $X$ that is isomorphic to $G$ and obeys the property above.

    We are primarily concerned with the case where the group $G$ is a vector space.

2. An **affine space** is a $V$-torsor where $V$ is the group of vectors of a vector space. More formally, it consists of the data:

     1. an *underlying vector space* $V$
     2. a $V$-torsor, $\mathcal{A}$, called the *underlying space*

3. An **affine subspace** is determined by a point in the affine space, a **point of origin**, and a subspace of the underlying vector space.

4. for any point $x \in \mathcal{A}$ there is an associated vector space $\mathcal{A}_x$ defined on the set

    $$\mathcal{A}_x := \{x\} \times \mathcal{A}$$

    with

    $$(x, y) + (x,z) := (x, x + (y-x  z-x)$$

    for $y, z \in \mathcal{A}$ and

    $$c \cdot (x, y) := (x, x + c(y-x))$$

    for $c \in \mathbb{R}, y \in \mathcal{A}$.

    We call this the **linear space of $\mathcal{A}$ rooted at $x$**. This vector space is of course isomorphic to the underlying vector space of $\mathcal{A}$.

5. An **affine map** is any map $f: \mathcal{A} \to \mathcal{B}$ between affine spaces such that the induced map $f_x^{\triangle}: \mathcal{A}_x \to \mathcal{B}_{f(x)}$ is linear for every $x$.


6. A **Galilean spacetime** is a tuple $\mathcal{G} = (\mathcal{E}, V, g, \tau)$ where

     - $V$ is a real, four-dimensional vector space
     - $(\mathcal{E}, V)$ is an affine space
     - $g$ is a (Euclidean) inner product on $\ker \tau$, (which is a 3-d subspace of $\mathcal{V}$ by the rank-nullity theorem)
     - $\tau: V \to \mathbb{R}$ is a surjective linear map called the **time map**

7. For any two points $x, y \in \mathcal{E}$, we say $x$ and $y$ are **events**. We say any two events $x$ and $y$ are **simultaneous** iff $\tau(x) = \tau(y)$. This is clearly an equivalence relation on $\mathcal{E}$, and the equivalence classes are precisely the fibers $\tau^{pre}(c)$ of the time map $\tau$. The collection of equivalence classes/fibers of Galilean spacetime $\mathcal{G}$ is called the **set of instants** and denoted by $I_{\mathcal{G}}$. Each instant is a three-dimensional affine subspace of $\mathcal{E}$.

8. Recall that under any Galilean spacetime, $g$ is an inner product for a 3-d subspace of the underlying 4-d real vector space. So if we are considering any instant $s \in I_{\mathcal{G}}$, then for any $x, y \in s$ we have $y - x \in \ker \tau$, which means $g(x-y, x-y)$ is known. Therefore we can define the distance $d(x, y) := \sqrt{g(x-y, x-y)}$ between simultaneous events $x$ and $y$ (but not between non-simultaneous events). The distance here is often the familiar Euclidean distance (whenever we have the standard Euclidean inner product).


9. $I_{\mathcal{G}}$ may be considered as an affine space in itself as well, over the vector space $\mathcal{R}$.

10. If $\mathcal{G}$ is any Galilean spacetime, then define

    $$V_{\mathcal{G}}$ := \{v \in V : \tau(v) = 1\}$$

    We can turn $V_{\mathcal{G}}$ into an affine space over the 3-d vector space $\ker \tau$ by noting that $w - v \in \ker \tau$ for all $w, v \in V_{\mathcal{G}}$. This space is said to be the affine space of **Galilean velocities**.

11. **Standard Galilean spacetime** is where we use

     - $\mathcal{E} = \mathcal{R}^3 \times \mathcal{R}$
     - $V = \mathbb{R}^4$
     - $\tau$ is the projection map $(x,y,z,t) \mapsto t$.
     - $g(a, b) = \sum_1^3 a_i b_i$ for $a, b \in \ker \tau$ ($a_4 = b_4 = 0$)
