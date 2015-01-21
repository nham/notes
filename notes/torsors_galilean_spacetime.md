1. A **torsor** is a "group that has forgotten its origin". This is achieved formally by considering a *group action* of a group $G$ on a set $X$ (i.e. a group homomorphism $G \to Sym X$) that obeys a certain property:

for all $a, b \in X$, there is exactly one $g \in G$ such that $g(a) = b$.

This condition implies that the group action is faithful (the homomorphism $G \to Sym X$ is injective), so that a $G$-torsor $X$ can be thought of as a group of permutations of $X$ that is isomorphic to $G$.

We will work in a slightly less general setting...

2. An **affine space** is a $V$-torsor where $V$ is the group of vectors of a vector space. More formally, it consists of the data:

 1. an *underlying vector space* $V$
 2. a $V$-torsor, $\mathcal{A}$, called the *underlying space*

3. An **affine subspace** is determined by a point in the affine space, a **point of origin**, and a subspace of the underlying vector space.

4. for any point $x \in \mathcal{A}$ there is an associated vector space $\mathcal{A}_x$ defined on the set 

$\mathcal{A}_x := \{(x, y) : y \in \mathcal{A} \}$

With $(x, y) + (x,z) := (x, x + (y-x  z-x)$ for $y, z \in \mathcal{A}$ and $c \cdot (x, y) := (x, x + c(y-x))$ for $c \in \mathbb{R}, y \in \mathcal{A}$. We call this the **linear space of $\mathcal{A}$ rooted at $x$**. This vector space is of course isomorphic to the underlying vector space of $\mathcal{A}$.

5. An **affine map** is any map $f: \mathcal{A} \to \mathcal{B}$ between affine spaces such that the induced map $f_x^{\triangle}: \mathcal{A}_x \to \mathcal{B}_{f(x)}$ is linear for every $x$.

6. An alternative way of viewing affine maps is as those maps between affine spaces that preserve barycenters of any finite collection of points. Recall that the **barycenter** of points $p_1, \ldots, p_n \in \mathcal{A}$ with weights (scalars) $\lambda_1, \ldots, \lambda_n$ such that $\sum_1^n \lambda_i = 1$ is the point $G := P_1 + \sum_1^n \lambda_i (p_i - p_1)$. Another way of saying this is that it is the point $G$ such that $\sum_1^n (G - p_i) = 0$. (Also recall that $\sum_1^n \mu_i v_i$ for some vectors $v_i$ and some scalars $\mu_i$ such that $\sum_1^n \mu_i = 0$ is called a **convex combination** of the $v_i$. We usually only define this for real vector spaces. The convex combinations of a collection of points are exactly those points in the convex hull of the points.)

TODO: The above is half-baked. Decide whether to study more or just remove it for now.

7. Alternatively, an affine map $f: \mathcal{A} \to \mathcal{B}$ may be thought of as a linear map $V \to V$ composed with a translation of $W$, where $V$ and $W$ are the underlying vector spaces of $\mathcal{A}$ and $\mathcal{B}$, respectively.


TODO: understand the convexity things in 1.1
