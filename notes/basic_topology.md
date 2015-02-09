---
title: Basic topology
---
Related notes: [metric spaces](metric_spaces.html)


1. A **topology** on any set $X$ is a collection $\mathcal{T}$ of subsets of $X$ that is closed under arbitrary union and finite intersection and contains both $\emptyset$ and $X$. The pair $(X, \mathcal{T})$ is said to be a **topological space**. (Usually we abuse terminology and say $X$ is a topological space with topology $\mathcal{T}$.) The sets in the topology are said to be the **open subsets** of $X$. A subset $U \subseteq X$ is said to be a **neighborhood** of $x \in X$ if both $x \in U$ and $U$ is open.

2. If you're trying to understand what the above definition of a topology *means*, stop trying and read what [Terry Tao has to say](http://mathoverflow.net/a/30231) about it:

     > Similarly, a topology is really a package of several different structures: the notion of openness, the notion of closedness, the notion of neighbourhoods, the notion of convergence, the notion of continuity, the notion of a homeomorphism, the notion of a homotopy, and so forth. They are all important, and it is somewhat artificial to try to designate one of them as being more "fundamental" than the other. But the notion of openness happens to generate all the other notions, and has a particularly elegant and simple axiomatisation, so we have elected to make it the basis for the standard minimalist definition of a topology. But it is important to realise that this is by no means the only way to define a topology, and adopting a more package-oriented point of view can be preferable in some cases (for instance, when generalising the notion of a topology to more abstract structures, such as topoi, in which open sets no longer are the most convenient foundation to begin with).

3. If $X$ is a set and $\mathcal{S}$ and $\mathcal{T}$ are topologies on $X$ such that every open set in $\mathcal{S}$ is an open set in $\mathcal{T}$, then $\mathcal{S}$ is said to be **coarser** than $\mathcal{T}$ (and $\mathcal{T}$ is **finer** than $\mathcal{S}$).

    The coarsest topology on any set $X$ is the **trivial topology** $\{ \emptyset, X\}$, while the finest topology, the power set of $X$, is called the **discrete topology**.

3. A point $x \in X$ is said to be an **interior point** of a subset $S \subseteq X$ precisely when there is a neighborhood $U$ of $x$ contained in $S$. Also, a point $x$ is said to be a **closure point** of $S$ when every neighborhood of $x$ intersects $S$. (Note that every $s \in S$ is a closure point of $S$, but there may be other closure points not in $S$. Not every $s \in S$ is an interior point, on the other hand, but all the interior points must be in $S$). The **interior** of a set $S$ is the collection of interior points, and the **closure** is the set of all closure points.

4. It is straightforward to prove that open subsets are precisely the sets that are equal to their interiors. Analogously to this, we can *define* **closed subsets** to be those sets that are equal to their closures.

5. It turns out that when you use the above definition, you can prove that a set is closed iff its complement is open. One can then prove, via DeMorgan's laws, that the collection of all closed sets is closed under arbitrary intersection, finite union, and contains both $\emptyset$ and $X$ (yes, $\emptyset$ and $X$ are simultaneously closed and open, a condition often called **clopen**).

6. Another characterization of closure and interior: interior of any set $S$ is the union of all open sets contained in $S$, while the closure of $S$ is the intersection of all closed sets that contain $S$. By these definitions, the interior is the largest open set contained in $S$, and the closure is the smallest closed set containing $S$.

7. A **boundary point** of a set is a point that is neither in the interior of the set, nor in the interior of the complement of the set. Equivalently, every neighborhood of a boundary point intersects both $S$ and $X - S$. The **boundary** of a set $S$ is the collection of all boundary points of $S$.

8. The **exterior** of a set $S$ is defined to be $\text{int}(X - S)$. It can be proved that this is always identical to $X - \text{clo}(S)$.

9. Given any set $S \subseteq X$, $X$ can always be partitioned into three disjoint sets:

     - the interior of $S$
     - the boundary of $S$
     - the exterior of $S$
    
    The union of the first two is the closure of $S$.

10. An **accumulation point** of a set $S$ is some point $x \in X$ such that every neighborhood of $x$ intersects $X - x$. This definition is designed to exclude the **isolated points** of $X$, which are points $x$ in $S$ such that some neighborhood $U$ of $x$ contains no other point of $S$ other than $x$. Each isolated point of $S$ is a closure point of $S$, but no isolated point is an accumulation point. So the closure is actually the disjoint union of isolated points and accumulation points.

11. A subset $S$ of a topological space $X$ is **dense** in $X$ if its closure is $X$, and **nowhere dense** in $X$ if its interior is empty. Equivalently, $S$ is dense if every non-empty open subset of $X$ contains an element of $S$, and nowhere dense if every non-empty open subset of $X$ contains an element of $X - S$.

12. A **continuous map** is any function $f: X \to Y$ (where $X$ and $Y$ are topological spaces) such that every open $V \subseteq Y$ has $f^{pre}(V)$ open in $X$.

    If $f$ is bijective, continuous, with continuous inverse, it is called a **homeomorphism**. This is the notion of isomorphism for topological spaces.

    A **topological embedding** is an injective continuous map $f: X \to Y$ such that the codomain restriction $X \to f(X)$ is a homeomorphism

13. There's a bunch of equivalent definitions for continuous maps. Here are three. Let $f: X \to Y$ be a map between topological spaces. Then $f$ is continuous exactly when either of these hold:

    1. For every $x \in X$ and any neighborhood $V$ of $f(x)$ in $Y$, there is a neighborhood $U$ of $x$ such that $f(U) \subseteq V$.
    2. $f^{pre}(C) is closed for every $C$ closed in $Y$
    3. For any $A \subseteq X$, $f$ maps closure points of $A$ to closure points of $f(A)$.

    If (1) is true, for any open $V$ in $Y$, either there is some $x \in X$ such that $f(x) \in V$, or $f^{pre}(V) = \emptyset$ and is hence open. In the former case by hypothesis there is some neighborhood of $x$ contained in $f^{pre}(V)$, so this set is open, proving $f$ is continuous. The converse is proved by noting that for every $x \in X$ and neighborhood $V$ of $f(x)$, $f^{pre}(V)$ is an open neighborhood of $x$ that works.

    For (2), note that $f^{pre}(Y - S) = X - f^{pre}(S)$ for any $S \subseteq Y$. So if preimages of open sets are all open, then so are preimages of closed sets, and vice versa.

    For (3), if $f$ is continuous and $A \subseteq X$, $\bar{f(A)}$ is closed in $Y$, so $f^{pre}(\bar{f(A)})$ is closed too (by what was just proved). Clearly $A \subseteq f^{pre}(\bar{f(A)})$, and since every closure point of a subset is a closure point of the whole set, $\bar{A} \subseteq f^{pre}(\bar{f(A)})$ (since the latter set is closed). So we have $f(\bar{A}) \subseteq \bar{f(A)}$, proving (3). Conversely, if (3) holds and $C$ is closed in $Y$, every closure point of $f^{pre}(C)$ gets mapped into a closure point of $f(f^{pre}(C)) = C$. $C$ being closed, this proves that $f^{pre}(C)$ contains its closure, so is closed.


14. The composition of continuous maps is continuous: If $f: X \to Y$, $g: Y \to Z$ are continuous and $W$ is open in $Z$, then $g^{pre}(W)$ is open in $Y$, so $f^{pre}(g^{pre}(W))$ is open in $X$. But $f^{pre}(g^{pre}(S)) = (g \circ f)^{pre}(S)$ for all $S \subseteq Z$. A few simple examples of continuous maps are the **identity map** on any topological space, and any constant map (the pre-image of any set under a constant map is either the whole space or the empty set).


15. A **local homeomorphism** is a function $f: X \to Y$ such that for every $x \in X$ there is a neighborhood $U$ of $x$ with 

     - $f(U)$ open in $Y$
     - the two-sided restriction of $f$, $F: U \to f(U)$, is a homeomorphism

    The only use I've ever seen for local homeomorphisms (so far) is in the definition of topological manifolds.

16. We can define the **convergence** of sequences in a topological space as follows: $(x_n)$ converges to $a \in  X$ when every neighborhood of $a$ contains all but finitely many terms of the sequence. This definition is not generally useful since limits are not unique in general topological spaces. For example, in the three-point space depicted by

    ![three point topological space with non-unique limits](non_unique_limits.png)

    The constant sequence of $b$'s converges to both $a$ and $c$ (in addition to $b$) because every neighborhood around $a$ or $c$ contains the whole sequence.

    Even weirder, under the trivial topology every sequence converges to every point. So there are topological spaces where the concept of convergent sequences is nonsensical. (There are two notions for discussing convergence in general topological spaces: nets and filters. I haven't had a reason to care about them yet, so I don't know anything about them)

17. A sufficient (but not necessary) condition for ensuring uniqueness of limits is the **Hausdorff** property, which says that any two distinct points in a topological space have disjoint neighborhoods. Any space with this property is called a **Hausdorff space**. This ensures uniqueness of limits since two tail sequences of one sequence could not be contained in two disjoint sets (the smaller of the tail sequences would have to be contained in two disjoint sets, which is crazy talk).

    Another property of Hausdorff spaces is that all finite subsets are closed. To prove it, note that a singleton set $\{x\}$ must be closed because if there was a closure point $y \neq x$, then every neighborhood of $y$ would contain $x$, implying that the space is not Hausdorff. Since singletons are closed, finite unions of singletons are closed, so all finite subsets are closed.


18. One important notion for topological spaces is **bases**. One way to think about these is as generalizations of the open balls of a metric space, which are used to generate the metric space topology. The idea is that a **basis** is a collection of "primitive" open sets that is used to generate the rest of the topology. Specifically, the open sets are defined to be exactly the unions of basis sets (including the empty union).

    Not just any collection of subsets of a topological space will work as a basis. We need to verify that the topology axioms all hold. Let $\mathcal{B}$ be some collection of subsets of $X$ and let $\mathcal{T} := \{ \bigcup \mathcal{S} : \mathcal{S} \subseteq \mathcal{B} \}$. By definition, $\emptyset \in \mathcal{T}$. Also by definition, if $\mathcal{X} \subseteq \mathcal{T}$, then $\bigcup \mathcal{X}$ is a union of unions of basis elements, hence still a union a basis elements, hence in $\mathcal{T}$. So the collections $\mathcal{B}$ that work as bases are exactly those that ensure

     - $X \in \mathcal{T}$
     - if $A, B \in \mathcal{T}$, then $A \cap B \in \mathcal{T}$

    The necessary and sufficient condition for the first is that $\bigcup \mathcal{B} = X$. If we want the second to be true, then we must at least have that the intersection of basis elements is in $\mathcal{T}$. Equivalently, for any basis elements $B_1, B_2$, we have for all $x \in B_1 \cap B_2$, there is some basis element $D$ such that $x \in D \subseteq B_1 \cap B_2$. Conversely, if the intersection of basis elements is in $\mathcal{T}$, then for any $A, B \in \mathcal{T}$, $A = \bigcup \mathcal{S}_1$ and $B = \bigcup \mathcal{S}_2$ for some $\mathcal{S}_1, \mathcal{S}_2$, so

    $$A \cap B = (\bigcup \mathcal{S}_1) \cap B = \bigcup_{S_1 \in \mathcal{S}_1} S_1 \cap B = \bigcup_{S_1 \in \mathcal{S}_1, S_2 \in \mathcal{S}_2} S_1 \cap S_2$$

    So $A \cap B$ is a union of intersections of basis elements, each of which is a union of basis elements by hypothesis, yadda yadda. Essentially the two conditions below are exactly the conditions that ensure the set induced by $\mathcal{B}$ is a topology

    - $\bigcup \mathcal{B} = X$
    - for all $B, C \in \mathcal{B}$, for all $x \in B \cap C$, there is a $D \in \mathcal{B}$ with $x \in D \subseteq B \cap C$

19. A space is **second-countable** if it has a countable basis. $\mathbb{R}^n$ with the Euclidean topology is second countable. An outline of a proof is:

     - $\mathbb{Q}$ is dense in $\mathbb{R}$ by basic properties of the reals
     - $\mathbb{Q}^n$ is countable since it is a finite cartesian product of countable sets
     - the collection of open balls centered at $x \in \mathbb{Q}^n$ with rational radii is countable since it is a countable union of countable sets
     - the sup-norm on $\mathbb{R}^n$ is topologically equivalent to the Euclidean norm, and every open box under the sup-norm contains a point with rational coordinates (using density of $\mathbb{Q}$ in $\mathbb{R}$) so $\mathbb{Q}^n$ is dense in $\mathbb{R}^n$ 
     - from this we get that the collection of open balls centered at rational coordinates with rational radii covers the whole space. Intersections of such balls are clearly open, so the collection is a countable basis for $\mathbb{R}^n$
