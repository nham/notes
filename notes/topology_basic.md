---
title: "Topology: miscellaneous stuff. The basics"
---
Related notes: [metric spaces](metric_spaces.html), [topology: bases and countability](topology_bases_countability.html)


16. A **limit point** of a set $S$ is some point $x \in X$ such that every neighborhood of $x$ intersects $S - x$. This definition is designed to exclude the **isolated points** of $S$, which are points $x$ in $S$ such that some neighborhood $U$ of $x$ contains no other point of $S$ other than $x$.

17. Isolated points are by definition closure points, but they may either be interior points or boundary points depending on the set and the topology.

    In $\mathbb{R}^2$ under the Euclidean topology, the set $A = B(0; 1) \cup \{(5, 0)\}$ has $(5, 0)$ as an isolated point of $A$, and it is clearly a boundary point of $A$.

    Consider, on the other hand, any discrete space. Every subset is open (so all points in a set are interior points), but every point is an isolated point (singletons are open sets).

    TODO: can we find a single topology where one set has an isolated boundary point, and another set has an isolated interior point? What about a single set that has isolated boundary and isolated interior points?

18. Limit points are similarly closure points, but they may again either be interior points or boundary points.

    Take the example of $\mathbb{R}$ with the standard topology. Then the set $(-1, 1)$ has $1$ as an limit point that is a boundary point, and $0$ as an limit point that is an interior point.

19. The previous note shows that limit points are not necessarily in the set, unlike isolated points. More generally, any boundary point of a set $A$ that is not contained in $A$ is necessarily an limit point. This means that a set without limit points must contain every boundary point, and so is closed.

20. Every closure point is either an isolated point or an limit point. If it's not in the set, it must be a boundary point and hence an limit point. If it's in the set, then it is either an limit point or an isolated point.

    This implies that the closure is the disjoint union of the isolated points and the limit points.


23. We can define the **convergence** of sequences in a topological space as follows: $(x_n)$ converges to $a \in  X$ when every neighborhood of $a$ contains all but finitely many terms of the sequence. This definition is not generally useful since limits are not unique in general topological spaces. For example, in the three-point space depicted by

    ![three point topological space with non-unique limits](non_unique_limits.png)

    The constant sequence of $b$'s converges to both $a$ and $c$ (in addition to $b$) because every neighborhood around $a$ or $c$ contains the whole sequence.

    Even weirder, under the trivial topology every sequence converges to every point. So there are topological spaces where the concept of convergent sequences is nonsensical. (There are two notions for discussing convergence in general topological spaces: nets and filters. I haven't had a reason to care about them yet, so I don't know anything about them)

24. The **order topology** on any totally ordered set $X$ is the one induced by the basis consisting of

     - all open intervals $(a, b)$ for $a, b \in X$
     - if there is a minimal element $z$, all half-open intervals $[z, x)$
     - if there is a maximal element $z$, all half-open intervals $(x, z]$

    This is a basis: it covers $X$ since if there's no maximal or minimal element, every $x \in X$ is contained in one open interval. If there's a minimal or a maximal element, it will be contained in one of the half-open intervals. Also, the intersection of two open intervals is either empty or another open interval, the intersection of an open interval and a half-closed interval is again either empty or open, and the intersection of two half-open intervals is either empty, another half-open interval, or an open interval. In all of these cases, the collection of all sets defined above is actually closed under non-disjoint intersection, so is a basis.
