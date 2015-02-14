---
title: "Topology: disjoint union spaces"
---

1. The set-theoretic disjoint union of some indexed collection of sets $\{X_i : i \in I\}$ is defined to be

    $$\coprod_{i \in I} X_i = \{(x, i) : i \in I, x \in X_i\}$$

    (actually there's a way, I think, to characterize the disjoint union via a universal property, but I'm currently thinking "why bother". This concrete representation works)

    This is a "tagged union". Similar to how subsets have the inclusion map and product sets have the projection maps, disjoint union sets have the **injection maps** $$\iota_i: X_i \to \coprod_i X_i$$ mapping

    $$\iota_i(x) = (x, i)$$

    This is obviously an injective map.

2. Now we may consider the **disjoint union topology**, which we define to be the finest topology on $\coprod_i X_i$ such that each injection map $\iota_i$ is continuous. For any $V$ open in $\coprod_i X_i$ we must have $\iota_i^{pre}(V)$ be open in $X_i$ for all $i$. In other words, every open set is a disjoint union of open sets.

    Indeed, the disjoint union topology is all disjoint unions of open sets, for any set that is a disjoint union of at least one non-open set will have one of the canonical injections fail to be continuous.

3. The reason that the subspace and product topologies are defined to be "the coarsest topology such that X" and the disjoint union topology is defined to be "the finest topology such that X" is that the subspace and product spaces' distinguished functions all have the subspace/product space as the domain, whereas the disjoint union space is the codomain of the injection maps. Note that the coarsest topology on any space is the trivial topology, and *any* function into such a space will be continuous.

4. We have, once again, a characteristic property for the disjoint union topology: a map $f: \coprod_i X_i \to Y$ is continuous iff each $f \circ \iota_i$ is continuous.

    Once again, one direction is immediate, so assume that $f$ is some such function and that each $f \circ \iota_i$ is continuous. Then if $V$ is open in $Y$, we have

    $$f^{pre}(V) = \bigcup_i [\iota_i(X_i) \cap f^{pre}(V)] = \bigcup_i \iota_i^{pre}(f^{pre}(V))$$

    So it's open.

5. To prove that the disjoint union topology is the unique topology on $\coprod_i X_i$ with this property, we proceed in much the same way as before: let $\mathcal{S}$ be some topology on $\coprod_i X_i$ with the property, and consider $\phi$, the identity map on $\coprod_i X_i$. if we consider the domain to have topology $\mathcal{S}$ and the codomain to have the disjoint union topology, then each $\phi \circ \iota_i$ is continuous since this is just the standard $i$-th injection into the disjoint union topology. By the characteristic property we then have that $\mathcal{S}$ is finer than the disjoint union topology.

    The converse is already proved since the disjoint union topology is the *finest* topology that makes all the injections continuous, and $\mathcal{S}$ is certainly one of the topologies that makes the injections continuous (the identity map on $\coprod_i X_i$ with topology $\mathcal{S}$ on both domain and codomain is continuous).

6. By continuity of the injections we have that closed sets in $\coprod_i X_i$ are disjoint unions of closed sets.

7. Each canonical injection is not just an injective continuous map, but also a topological embedding. The proof here is that the open sets in $\iota_i(X_i)$ as a subspace of $\coprod_i X_i$ are exactly the sets $U_i$ where $U$ is any open set in $X_i$ and $U_i$ is defined by $(x, i) \in U_i$ iff $x \in U$.

8. The disjoint union of Hausdorff spaces is again Hausdorff. If $a, b \in \coprod_i X_i$ are distinct, then $a \in X_j$ and $b \in X_k$ for some $j, k$. If $j \neq k$ we're done since $\iota_j(X_j)$ and $\iota_k(X_k)$ are disjoint. Otherwise we can find disjoint neighborhoods $A$ and $B$ and $\iota_i(A)$ and $\iota_i(B)$ are disjoint.
