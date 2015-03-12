---
title: "Topology: finite product spaces"
---

1. We seek to define a topology on a finite product of topology spaces. Similar to how the subspace topology was defined, we shall define the **product topology** to be the coarsest topology that makes each projection map $\pi_i: \prod_1^n X_i \to X_i$ continuous. This means that for any $U$ open in $X_i$, we must at least have each set

    $$\prod_1^n X_j \text{ if } j \neq i \text{ else } U$$

    open in $\prod_1^n X_i$

    Furthermore, if we have a collection of $U_i$'s each open in $X_i$, then the intersection of the preimages of these under the $i$-th projection is $\prod_1^n U_i$. So products of open sets must be open.

    The converse is true too. If all products of open sets are open, we can consider the union of all the ones with $U$ in the $i$-th position. This is just

    $$\prod_1^n X_j \text{ if } j \neq i \text{ else } U$$

    So the projections are all continuous.

2. Consider the collection of products of open sets. It covers $\prod_1^n X_i$ (that set is actually in the collection).

    Also, the intersections of products is the product of intersections, any intersection of two such sets is another product of open sets. I.e. the collection of products of open sets is a basis.

    This clearly makes projections continuous, by reasoning in the previous note. The claim is that this is a basis for the product topology.

    But this is true since topologies making projections continuous must contain products of open sets, and thus all unions of such sets.

3. As for the subspace topology, there is a "characteristic property" for the product topology, namely it is the unique topology on $\prod_1^n X_i$ such that functions $f: Y \to \prod_1^n X_i$ are continuous iff the component functions $\pi_i \circ f: Y \to X_i$ are continuous.

    To show that the product topology obeys the property, one direction is easy since any continuous $f$ will have $\pi_i \circ f$ continuous ($\pi_i$ is continuous by the above). Conversely, if $f: Y \to \prod_1^n X_i$ is such that $\pi_i \circ f$ is continuous for all $i$, let $Z = \prod_1^n U_i$ be an element of the product basis. Then $Z = \cap_1^n \pi_i^{pre}(U_i), so $f^{pre}(Z) = \cap_1^n (\pi_i \circ f)^{pre}(U_i)$, which is a finite union of open sets since $\pi_i \circ f$ is continuous by assumption. This proves that $f$ is continuous because the inverse image of any basis element is open.

    To show that no other topologies on $\prod_1^n X_i$ obey the property,let $\mathcal{S}$ be some topology on $\prod_1^n X_i$ that has it. Then defining $\phi$ to be the identity on $\prod_1^n X_i$, each $\pi_i \circ \phi = \pi_i$. But considering $\prod_1^n X_i$ to have topology $\mathcal{S}$, we have that $\phi$ is continuous (being an identity map), so each $\pi_i$ is also continuous, meaning that $\mathcal{S}$ must be finer than the subspace topology by (11).

    Conversely, let $\phi$ again be the identity on $\prod_1^n X_i$, but now consider the domain to have the product topology and the codomain to have topology $\mathcal{S}$. Each $\pi_i \circ \phi$ is just the $i$-th projection on the product topology, which is continuous. But by the characteristic property holding for $\mathcal{S}$, we have that $\phi$ must be continuous, which implies that $\mathcal{S}$ must be coarser than the product topology. In other words, $\mathcal{S}$ *is* the product topology.

4. One thing product spaces affords us is taking the product of continuous maps. If $f_i: X_i \to Y_i$ are continuous maps for $1 \leq i \leq n$, the map $f: \prod_1^n X_i \to \prod_1^n Y_i$ defined by

    $$f(x) = ((f_i \circ \pi_i)(x) : 1 \leq i \leq n)$$

    is called the **product map** of $f_1, \ldots, f_n$. You're probably expecting that we'll prove that $f$ is continuous. You're darned tootin'. Since it suffices to consider basis elements, we have for any $\prod_1^n U_i \subseteq \prod_1^n Y_i$ that $f(x_i : 1 \leq i \leq n) \in \prod_1^n U_i$ iff $f_i(x_i) \in U_i$ for all $i$ iff $x_i \in f_i^{pre}(U_i)$ for all $i$. So 

    $$f^{pre}(\prod_1^n U_i) = \prod_1^n f_i^{pre}(U_i)$$

    which is open since each $f_i$ is continuous. We denote this map by $\prod_1^n f_i$.

5. The product map of injective maps is injective: if $f(a) = f(b)$, then $f_i(a_i) = f_i(b_i)$ for all $i$, which implies that $a_i = b_i$ for all $i$ by injectivity. Similarly the product map of surjective maps is surjective: for any $y$ in the codomain of $f$, for all $i$ there is an $x_i$ such that $f_i(x_i) = y_i$ by surjectivity, so $f(x) = y$.

6. To prove that the product map of homeomorphisms is a homeomorphism between product spaces, it suffices to prove that the inverse of a product map is the product map of inverses. This can be seen through straightforward calculation. To illustrate one direction: if $g: \prod_1^n Y_i \to \prod_1^n X_i$ is defined by

    $$g(x) := (f_i^{-1}(x_i) : 1 \leq i \leq n)$$

    Then $g(f(x)) = (f_i^{-1}(f_i(x_i)) : 1 \leq i \leq n) = x$. The other direction is similar.

7. The finite product of Hausdorff spaces $X_i$ is also Hausdorff because for any two distinct points $x = (x_i : 1 \leq i \leq n), y = (y_i : 1 \leq i \leq n) \in \prod_1^n X_i$, then for some $i$ we have $x_i \neq y_i$, so we can find disjoint neighborhoods $U_i, V_i$ for $x_i$ and $y_i$, respectively, in $X_i$ (due to Hausdorffness). Pick any open sets $U_j, V_j$ in $X_j$ for $j \neq i$, each of which contains $x_j$ and $y_j$, respectively. Then $\prod_1^n U_i$ and $\prod_1^n V_i$ are disjoint.
