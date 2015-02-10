---
title: Topology: bases and countability
---
Related notes: [basic topology](basic_topology.html)

1. One important notion for topological spaces is **bases**. One way to think about these is as generalizations of the open balls of a metric space, which are used to generate the metric space topology. The idea is that a **basis** is a collection of "primitive" open sets that is used to generate the rest of the topology. Specifically, the open sets are defined to be exactly the unions of basis sets (including the empty union).

    Not just any collection of subsets of a topological space will work as a basis. We need to verify that the topology axioms all hold. Let $\mathcal{B}$ be some collection of subsets of $X$ and let $\mathcal{T} := \{ \bigcup \mathcal{S} : \mathcal{S} \subseteq \mathcal{B} \}$. By definition, $\emptyset \in \mathcal{T}$. Also by definition, if $\mathcal{X} \subseteq \mathcal{T}$, then $\bigcup \mathcal{X}$ is a union of unions of basis elements, hence still a union a basis elements, hence in $\mathcal{T}$. So the collections $\mathcal{B}$ that work as bases are exactly those that ensure

     - $X \in \mathcal{T}$
     - if $A, B \in \mathcal{T}$, then $A \cap B \in \mathcal{T}$

    The necessary and sufficient condition for the first is that $\bigcup \mathcal{B} = X$. If we want the second to be true, then we must at least have that the intersection of basis elements is in $\mathcal{T}$. Equivalently, for any basis elements $B_1, B_2$, we have for all $x \in B_1 \cap B_2$, there is some basis element $D$ such that $x \in D \subseteq B_1 \cap B_2$. Conversely, if the intersection of basis elements is in $\mathcal{T}$, then for any $A, B \in \mathcal{T}$, $A = \bigcup \mathcal{S}_1$ and $B = \bigcup \mathcal{S}_2$ for some $\mathcal{S}_1, \mathcal{S}_2$, so

    $$A \cap B = (\bigcup \mathcal{S}_1) \cap B = \bigcup_{S_1 \in \mathcal{S}_1} S_1 \cap B = \bigcup_{S_1 \in \mathcal{S}_1, S_2 \in \mathcal{S}_2} S_1 \cap S_2$$

    So $A \cap B$ is a union of intersections of basis elements, each of which is a union of basis elements by hypothesis, yadda yadda. Essentially the two conditions below are exactly the conditions that ensure the set induced by $\mathcal{B}$ is a topology

    - $\bigcup \mathcal{B} = X$
    - for all $B, C \in \mathcal{B}$, for all $x \in B \cap C$, there is a $D \in \mathcal{B}$ with $x \in D \subseteq B \cap C$

19. A space is **second-countable** if it has a countable (finite or countably infinite) basis. $\mathbb{R}^n$ with the Euclidean topology is second countable. An outline of a proof is:

     - $\mathbb{Q}$ is dense in $\mathbb{R}$ by basic properties of the reals
     - $\mathbb{Q}^n$ is countable since it is a finite cartesian product of countable sets
     - the collection of open balls centered at $x \in \mathbb{Q}^n$ with rational radii is countable since it is a countable union of countable sets
     - the sup-norm on $\mathbb{R}^n$ is topologically equivalent to the Euclidean norm, and every open box under the sup-norm contains a point with rational coordinates (using density of $\mathbb{Q}$ in $\mathbb{R}$) so $\mathbb{Q}^n$ is dense in $\mathbb{R}^n$ 
     - from this we get that the collection of open balls centered at rational coordinates with rational radii covers the whole space. Intersections of such balls are clearly open, so the collection is a countable basis for $\mathbb{R}^n$

2. A **cover** for a subset $S$ of some topological space $X$ is any collection of subsets of $X$ whose union is a superset of $S$. An **open cover** is a cover consisting of open sets. A **subcover** is a subcollection of cover elements that still acts as a cover for the set.

3. A space is said to be a **Lindelöf space** if every open cover of the space has a countable subcover. A useful fact (I'm foggy on how useful, exactly) is that every second-countable space is Lindelöf.

    Proof: There is some countable basis for the space, so (WLOG) assume $\mathcal{U}$ is an open cover containing $\emptyset$. For every basis element $B$, we define $U_B$ to be either one of the cover elements that contains that basis element if one such cover element exists, or $U_B = \emptyset$ otherwise. If the collection of $U_B$'s is not a subcover, then for some point $x$, every basis element containing $x$ is not contained in any cover element of $\mathcal{U}$, which contradicts that $x$ is in at least one cover element $U$ and that therefore there is some basis element that is a neighborhood of $x$ and is contained in $U$. So the $U_B$'s are a subcover, and they are countable since we are working with a countable basis.
