---
title: "Topology: miscellaneous stuff. The basics"
---
Related notes: [metric spaces](metric_spaces.html), [topology: bases and countability](topology_bases_countability.html)


1. A **topology** on any set $X$ is a collection $\mathcal{T}$ of subsets of $X$ that is closed under arbitrary union and finite intersection and contains both $\emptyset$ and $X$. The pair $(X, \mathcal{T})$ is said to be a **topological space**. (Usually we abuse terminology and say $X$ is a topological space with topology $\mathcal{T}$.) The sets in the topology are said to be the **open subsets** of $X$. A subset $U \subseteq X$ is said to be a **neighborhood** of $x \in X$ if both $x \in U$ and $U$ is open.

2. If you're trying to understand what the above definition of a topology *means*, stop trying and read what [Terry Tao has to say](http://mathoverflow.net/a/30231) about it:

     > Similarly, a topology is really a package of several different structures: the notion of openness, the notion of closedness, the notion of neighbourhoods, the notion of convergence, the notion of continuity, the notion of a homeomorphism, the notion of a homotopy, and so forth. They are all important, and it is somewhat artificial to try to designate one of them as being more "fundamental" than the other. But the notion of openness happens to generate all the other notions, and has a particularly elegant and simple axiomatisation, so we have elected to make it the basis for the standard minimalist definition of a topology. But it is important to realise that this is by no means the only way to define a topology, and adopting a more package-oriented point of view can be preferable in some cases (for instance, when generalising the notion of a topology to more abstract structures, such as topoi, in which open sets no longer are the most convenient foundation to begin with).

3. If $X$ is a set and $\mathcal{S}$ and $\mathcal{T}$ are topologies on $X$ such that every open set in $\mathcal{S}$ is an open set in $\mathcal{T}$, then $\mathcal{S}$ is said to be **coarser** than $\mathcal{T}$ (and $\mathcal{T}$ is **finer** than $\mathcal{S}$).

    The coarsest topology on any set $X$ is the **trivial topology** $\{ \emptyset, X\}$, while the finest topology, the power set of $X$, is called the **discrete topology**.

4. A point $x \in X$ is said to be an **interior point** of a subset $S \subseteq X$ precisely when there is a neighborhood $U$ of $x$ contained in $S$. Also, a point $x$ is said to be a **closure point** of $S$ when every neighborhood of $x$ intersects $S$. (Note that every $s \in S$ is a closure point of $S$, but there may be other closure points not in $S$. Not every $s \in S$ is an interior point, on the other hand, but all the interior points must be in $S$). The **interior** of a set $S$ is the collection of interior points, and the **closure** is the set of all closure points.

5. It is straightforward to prove that open subsets are precisely the sets that are equal to their interiors. Analogously to this, we can *define* **closed subsets** to be those sets that are equal to their closures.

6. Another characterization of closure and interior: interior of any set $S$ is the union of all open sets contained in $S$, while the closure of $S$ is the intersection of all closed sets that contain $S$.

    To prove the former, note that the union of all open subsets contains every interior point, and that every point in said union is in one open subset and so must be an interior point.

    To prove the latter, note that the closure of $S$ is a closed set containing $S$, and that every closed superset $Z$ of $S$ contains all its closure points. The closure points of any subset of $Z$ are also closure points of $Z$ itself, so $Z$ contains the closure of $S$.

    By these definitions, the interior is *the largest open set contained in $S$*, and the closure is *the smallest closed set containing $S$*.


7. A **boundary point** of a set is a point that is neither in the interior of the set, nor in the interior of the complement of the set. Equivalently, every neighborhood of a boundary point intersects both $S$ and $X - S$. The **boundary** of a set $S$ is the collection of all boundary points of $S$, sometimes denoted $\partial S$.


8. The closure of a set is the disjoint union of the interior and the boundary. Proof: take any closure point $x$ of $S$. Then either every neighborhood intersects both $S$ and $X - S$, or one doesn't and so is contained in $S$. So the interior is what you get when you logically negate the definition of a boundary point.

9. A pretty important fact is that the boundary of any set $S$ is the same as the boundary of $X - S$. This is apparent from the definition since $X - (X - S) = X$.

10. We have defined closed subsets to be those that are equal to their closures. But the closure is the disjoint union of the interior and the boundary, and sets always contain their interiors. So a subset is closed iff it contains its boundary.

    Similarly, open subsets are those equal to their interiors, and boundary points are by definition not interior points. So open sets contain no boundary points, and a set containing no boundary points contains only interior points.

11. We are now in a position to not only prove, but intuitively *see* that a set $S$ is closed in a top. space $X$ iff $X - S$ is open. $S$ and $X - S$ share their boundary, so $S$ contains the boundary iff $X - S$ contains none of it.

12. Now we can prove, using DeMorgan's laws, that the collection of all closed subsets of a space $X$ is

     - closed under arbitrary intersection
     - closed under finite union
     - contains $\emptyset$ and $X$

    The first two follow immediately from $X - \bigcap_i C_i = \bigcup_i (X - C_i)$, $X - \bigcup_i C_i = \bigcap_i (X - C_i)$ , and the topology axioms. The third is because $\emptyset$ and $X$ are complements of one another.

13. By the way, $\emptyset$ and $X$ are simultaneously closed and open in every topological space. Such sets are sometimes called **clopen**.

14. Nice little corollary from (12) is that that boundaries are always closed: it's the intersection of $clo(X - S)$ and $clo(S)$, two closed sets.

15. We can extend the idea in (14) and note that, since closures are partitioned into the interior and the boundary, for any set $S$ we have a partition of all of $X$ into:

     - interior of $S$
     - interior of $X - S$
     - boundary of $S$ / $X - S$

    The interior of $X - S$ will be called the **exterior of $S$**.

    Another way of saying this is that the interior of $X - S$ is identically the complement of the closure of $S$. This is evident since the points of $X$ that fail to be closure points of $S$ are exactly the ones that have a neighborhood contained in $X - S$, i.e. the interior points of $X - S$.


16. A **limit point** of a set $S$ is some point $x \in X$ such that every neighborhood of $x$ intersects $S - x$. This definition is designed to exclude the **isolated points** of $S$, which are points $x$ in $S$ such that some neighborhood $U$ of $x$ contains no other point of $S$ other than $x$.

17. Isolated points are by definition closure points, but they may either be interior points or boundary points depending on the set and the topology.

    In $\mathbb{R}^2$ under the Euclidean topology, the set $A = B(0; 1) \cup \{(5, 0)\}$ has $(5, 0)$ as an isolated point of $A$, and it is clearly a boundary point of $A$.

    Consider, on the other hand, any discrete space. Every subset is open (so all points in a set are interior points), but every point is an isolated point (singletons are open sets).

    TODO: can we find a single topology where one set has an isolated boundary point, and another set has an isolated interior point? What about a single set that has isolated boundary and isolated interior points?

18. Limit points are similarly closure points, but they may again either be interior points or boundary points.

    Take the example of $\mathbb{R}$ with the standard topology. Then the set $(-1, 1)$ has $1$ as an limit point that is a boundary point, and $0$ as an limit point that is an interior point.

19. (12) shows that limit points are not necessarily in the set, unlike isolated points. More generally, any boundary point of a set $A$ that is not contained in $A$ is necessarily an limit point. This means that a set without limit points must contain every boundary point, and so is closed.

20. Every closure point is either an isolated point or an limit point. If it's not in the set, it must be a boundary point and hence an limit point. If it's in the set, then it is either an limit point or an isolated point.

    This implies that the closure is the disjoint union of the isolated points and the limit points.


21. A subset $S$ of a topological space $X$ is **dense** in $X$ if its closure is $X$, and **nowhere dense** in $X$ if its interior of its closure is empty.

    Equivalently, $S$ is dense iff every non-empty open subset of $X$ contains an element of $S$: $S$ being dense is the same as every point of $X$ being a closure point, which is the same as every non-empty open set being the neighborhood of some closure point.

    Also equivalently, $S$ is nowhere dense in $X$ iff $X - clo(S)$ is dense in $X$: $S$ is nowhere dense iff $clo(S)$ has no interior iff $clo(S)$ is all boundary points of $clo(S)$. Clearly

    $$X = clo S \sqcup X - clo S$$

    and also

    $$clo(X - clo S) = \partial(X - clo S) \sqcup int(X - clo S) = \partial clo S \sqcup X - clo S$$

    since the boundary of a set and its complement are equal and since $X - clo S$ is open. So $clo(X - clo S) = X$ iff $clo S = \partial clo S$.


22. Why isn't "nowhere dense" defined to be sets with empty interior? Consider $\mathbb{R}$ with the standard topology. The rationals have empty interior, so the set

    $$A := \{x \in \mathbb{Q} : -1 < x < 1\}$$

    also has empty interior (considered as a subset of $\mathbb{R}$). But $clo(A) = [-1, 1]$, so clearly $X - clo(A) = (-\infty, 1) \cup (1, \infty)$ is not dense in $\mathbb{R}$


23. We can define the **convergence** of sequences in a topological space as follows: $(x_n)$ converges to $a \in  X$ when every neighborhood of $a$ contains all but finitely many terms of the sequence. This definition is not generally useful since limits are not unique in general topological spaces. For example, in the three-point space depicted by

    ![three point topological space with non-unique limits](non_unique_limits.png)

    The constant sequence of $b$'s converges to both $a$ and $c$ (in addition to $b$) because every neighborhood around $a$ or $c$ contains the whole sequence.

    Even weirder, under the trivial topology every sequence converges to every point. So there are topological spaces where the concept of convergent sequences is nonsensical. (There are two notions for discussing convergence in general topological spaces: nets and filters. I haven't had a reason to care about them yet, so I don't know anything about them)

24. A sufficient (but not necessary) condition for ensuring uniqueness of limits is the **Hausdorff** property, which says that any two distinct points in a topological space have disjoint neighborhoods. Any space with this property is called a **Hausdorff space**. This ensures uniqueness of limits since two tail sequences of one sequence could not be contained in two disjoint sets (the smaller of the tail sequences would have to be contained in two disjoint sets, which is crazy talk).

    Another property of Hausdorff spaces is that all finite subsets are closed. To prove it, note that a singleton set $\{x\}$ must be closed because if there was a closure point $y \neq x$, then every neighborhood of $y$ would contain $x$, implying that the space is not Hausdorff. (Alternate proof: every point $y \neq x$ certainly has a neighborhood $U_y$ not containing $x$, so the union of them all is open and is $X - x$.) Since singletons are closed, finite unions of singletons are closed, so all finite subsets are closed.

25. TODO: An example of a non-Hausdorff space where limits are unique.
