---
title: "Topology: bases and countability"
---
Related notes: [basic topology](topology_basic.html)

1. One important notion for topological spaces is **bases**. The idea is that a **basis** is a collection of "primitive" open sets that is used to generate the rest of the topology. The definition is any collection $\mathcal{B}$ of subsets of $X$ such that

    - $\bigcup \mathcal{B} = X$
    - for all $A, B \in \mathcal{B}$, $A \cap B$ is a union of elements in $\mathcal{B}$.

    The **topology on $X$ induced by basis $\mathcal{B}$** is defined by

    $$\mathcal{T} := \{ \bigcup \mathcal{S} : \mathcal{S} \subseteq \mathcal{B} \}$$

    Clearly $\emptyset \in \mathcal{T}$ since $\bigcup \emptyset = \emptyset$. Also $X \in \mathcal{T}$. If $\{U_i\}$ is any collection of sets in $\mathcal{T}$, then each $U_i$ is a union of basis elements, so $\bigcup_i U_i$ is a union of basis elements and hence in $\mathcal{T}$. Finally, for any $A, B \in \mathcal{T}$, $A = \bigcup_i A_i$ and $B = \bigcup_j B_j$ for some basis elements $A_i, B_j$. By distributivity

    $$(\bigcup_i A_i) \cap (\bigcup_j B_j) = \bigcup_i \bigcup_j A_i \cap B_j$$

    So that $A \cap B$ is the union of intersections of basis elements. Since each intersection of basis elements is a union of basis elements, the whole union is as well.

2. The converse is true too: If $\mathcal{B$ is any collection of subsets of $X$ and $\mathcal{T}$ defined as in (1), then $\mathcal{T}$ contains $\emptyset$ and is closed under arbitrary unions automatically. If $\mathcal{T}$ is to be a topology, we must have $X \in \mathcal{T}$, or that $X = \bigcup \mathcal{S}$ for some $\mathcal{S} \subseteq \mathcal{B}$, which implies that $X = \bigcup \mathcal{B}$. For any $A, B \in \mathcal{B}$, they are in $\mathcal{T}$ by definition, and since $\mathcal{T}$ is a topology by assumption, $A \cap B$ must be a union of sets in $\mathcal{B}$, which is exactly the second basis property.

3. Here's one sufficient condition for when a collection of sets is a basis for some topology: if $(X, \mathcal{T})$ is a topological space and $\mathcal{C}$ is any collection of open subsets of $X$, then if for all $U \in \mathcal{T}$ and all $x \in U$ we have some $C \in \mathcal{C} with $x \in C \subseteq U$, then $\mathcal{C}$ is a basis that induces $\mathcal{T}$.

    *Proof:* Clearly $\mathcal{C}$ covers the space. But any intersection of two sets in $\mathcal{C}$ is open, so every point in the intersection has a $\mathcal{C}$-set contained in the intersection.

    Note this is just saying "if $\mathcal{C}$ is a collection of open subsets and every open $U$ is a union of sets in $\mathcal{C}$, then $\mathcal{C}$ is a basis for the topology."

4. If $\mathcal{B}$ and $\mathcal{C}$ are bases for a set $X$, let $\mathcal{S}$ and $\mathcal{T}$ be the respective induced topologies.

    If for every $C \in \mathcal{C}$ and every $x \in C$ we have a $B \in \mathcal{B}$ with $x \in B \subseteq C$, then $\mathcal{S}$ is finer than $\mathcal{T}$. This is so because the hypothesis implies that $\mathcal{C}$-elements are unions of $\mathcal{B}$-elements, so every $\mathcal{T}$-open set is $\mathcal{S}-open$.

    The converse is true too: if $\mathcal{S}$ is finer than $\mathcal{T}$, every $C \in \mathcal{C}$ must be $\mathcal{S}$-open, hence a union of $\mathcal{B}$-elements, which is equivalent to the condition we stated above.

    A corollary of the above is that the topologies induced by two bases are equivalent iff each $\mathcal{C}$-element is a union of $\mathcal{B}$-elements and vice versa.


5. A space is **second-countable** if it has a countable (finite or countably infinite) basis. $\mathbb{R}^n$ with the Euclidean topology is second countable. An outline of a proof is:

     - $\mathbb{Q}$ is dense in $\mathbb{R}$ by basic properties of the reals
     - $\mathbb{Q}^n$ is countable since it is a finite cartesian product of countable sets
     - the collection of open balls centered at $x \in \mathbb{Q}^n$ with rational radii is countable since it is a countable union of countable sets
     - the sup-norm on $\mathbb{R}^n$ is topologically equivalent to the Euclidean norm, and every open box under the sup-norm contains a point with rational coordinates (using density of $\mathbb{Q}$ in $\mathbb{R}$) so $\mathbb{Q}^n$ is dense in $\mathbb{R}^n$ 
     - from this we get that the collection of open balls centered at rational coordinates with rational radii covers the whole space. Intersections of such balls are clearly open, so the collection is a countable basis for $\mathbb{R}^n$

6. A space is **separable** if it has a countable dense subset.

7. Second-countable spaces are separable: if $X$ is second countable, pick an element in each basis element. This is a countable subset of $X$, and every non-empty open set, being a union of basis elements, contains an element of this set, so it is dense in $X$.

8. A **neighborhood basis** for point $a \in X$ is some collection $\mathcal{B}$ of neighborhoods of $a$ such that every neighborhood of $a$ contains some $B \in \mathcal{B}$.

9. A space is **first-countable** if every point has a countable neighborhood basis.

10. Any second-countable space is first countable. Let $\mathcal{B}$ be a countable basis for $X$. Then one basis that works for any $a \in X$ is all the sets in $\mathcal{B}$ that are neighborhoods of $a$. It's countable since it's a subset of $\mathcal{B}$, and clearly any neighborhood $U$ of $a$ contains some basis set around $a$.

11. A **cover** for a subset $S$ of some topological space $X$ is any collection of subsets of $X$ whose union is a superset of $S$. An **open cover** is a cover consisting of open sets. A **subcover** is a subcollection of cover elements that still acts as a cover for the set.

12. A space is said to be a **Lindelöf space** if every open cover of the space has a countable subcover. A useful fact (I'm foggy on how useful, exactly) is that every second-countable space is Lindelöf.

    Proof: There is some countable basis for the space, so (WLOG) assume $\mathcal{U}$ is an open cover containing $\emptyset$. For every basis element $B$, we define $U_B$ to be either one of the cover elements that contains that basis element if one such cover element exists, or $U_B = \emptyset$ otherwise. If the collection of $U_B$'s is not a subcover, then for some point $x$, every basis element containing $x$ is not contained in any cover element of $\mathcal{U}$, which contradicts that $x$ is in at least one cover element $U$ and that therefore there is some basis element that is a neighborhood of $x$ and is contained in $U$. So the $U_B$'s are a subcover, and they are countable since we are working with a countable basis.

13. The **subspace basis** for a subspace $A$ of some space $X$ w.r.t. a basis $\mathcal{B}$ is just all the basis element intersected with $A$. This construction is easily seen to be a basis (it obviously covers $A$, and if $U_1 = A \cap V_1, U_2 = A \cap V_2$ for $V_1, V_2 \in \mathcal{B}$, for any $x \in U_1 \cap U_2$ there is a $D \in \mathcal{B}$ such that $x \in D \subseteq V_1 \cap V_2$, so $x \in D \cap A \subseteq U_1 \cap U_2$.) It generates the subspace the topology because of distributivity: the union of subspace basis elements is actually the intersection of $A$ with a union of basis elements in $\mathcal{B}$, (so every open set in the topology induced by the subspace basis is open in the subspace topology, but also if it's open in the subspace topology, it must be a union of (original) basis elements intersected with $A$, so is open in the subspace basis induced topology).

14. The **product basis** given bases $\mathcal{B}_i$ for spaces $X_i$, $1 \leq i \leq n$ is (predictably) the collection of all products of basis sets. This is indeed a basis, since for every $x = (x_i : 1 \leq i \leq n) \in \prod_1^n X_i$, we can bind basis elements $B_i$ such that $x_i \in B_i$, so $x \in \prod_1^n B_i$. Also, we have:

    $$\prod_1^n B_i \cap \prod_1^n C_i = \prod_1^n (B_i \cap C_i)$$

    For every $x_i \in B_i \cap C_i$, there's a basis set $D_i$ with $x_i \in D_i \subseteq B_i \cap C_i$, so clearly $x \in \prod_1^n D_i \subseteq \prod_1^n (B_i \cap C_i)$.

    To prove that it really induces the product topology, we first note that the product basis is a collection of open sets (a collection of elements of the standard product topology basis, actually!). So if every $\prod_1^n U_i$ is such that every $x \in prod_1^n U_i$ has a product of basis elements $\prod_1^n B_i$ such that $x \in \prod_1^n B_i \subseteq \prod_1^n U_i$, then it follows that the product basis generates the product topology. But this is certainly true, since if $x_i \in U_i$, there is a basis element containing $x_i$ and contained in $U_i$.

15. The product of second countable spaces is second countable since countable bases for $X_1, \ldots, X_n$ induce, through the product basis, a basis which is the finite product of countable sets.
