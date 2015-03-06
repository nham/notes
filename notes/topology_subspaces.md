---
title: "Topology: subspaces"
---

These notes depend on the [basic topology](topology_basic.html) notes and the [continuity](topology_continuity.html) notes.

1. For any topological space $(X, \mathcal{T})$ and any $A \subseteq X$, consider the set $\iota^{\ast} \mathcal{T} := \{\iota_A^{pre}(U) : U \in \mathcal{T} \}$, where $\iota_A: A \to X$ is the inclusion map. Then $\iota_^{\ast} \mathcal{T}$ is a topology for $A$: it clearly includes $\emptyset$ and $A$, the preimage of an arbitrary union is the union of preimages for any function (so it's closed under unions), and for any $B, C \in \mathcal{T}$, $x \in \iota_A^{pre}(B) \cap \iota_A^{pre}(C)$ iff $x \in A \cap B \cap C = \iota_A^{pre}(B \cap C)$, so it's closed under finite intersections. This topology is called the **subspace topology** on $A$, and it's not hard to see that it is exactly the collection of open sets in $\mathcal{T}$ intersected with $A$.

    We can say more than this though. If $\mathcal{S}$ is any topology on $A$ such that the inclusion $\iota_A$ is continuous, then it must be finer than the subspace topology. In other words, the subspace topology is the *coarsest* topology that makes the inclusion continuous. The proof is quite trivial: if the inclusion is continuous, the pre-image of any open set $U$ in $X$ is open in $\mathcal{S}$. But the preimage is just $U \cap A$.

2. The subspace topology on $A \subseteq X$ obeys what Lee calls the "characteristic property" of the subspace, which is that any map $f: Y \to A$ (where $Y$ is some topological space) is continuous iff $\iota_A \circ f$ is continuous. If $f$ is continuous, $\iota_A \circ f$ certainly must be as well since composition of continuous functions is continuous. Conversely, if $\iota_A \circ f$ is continuous, then for any $U$ open in $A$, $U = A \cap V$ for some $V$ open in $X$, so $(\iota_A \circ f)^{pre}(V) = f^{pre}(U)$ is also open in $Y$, proving $f$ is continuous.

    Presumably Lee calls it the "characteristic property" because the subspace topology is the *unique* topology on $A$ that has this property. If $A$ equipped with some topology $\mathcal{S}$ has the property that for any $Y$, $f: Y \to A$ is continuous iff $\iota_A \circ f$, by letting $f$ be the identity on $A$ (with same topology $\mathcal{S}$), we can see that $\iota_A$ is continuous, so $\mathcal{S}$ is finer than the subspace topology by (1).

    Conversely, consider $\phi: A \to A_S$, where $A_S$ is denoting $A$ with the topology $\mathcal{S}$ (this is technically an abuse of notation/nonsense, but it is suggestive!) and $A$ just denotes $A$ with the subspace topology. Then $\iota_A \circ \phi = \iota_A$, which is certainly continuous because $A$ is a subspace. By the characteristic property of $(A, \mathcal{S})$, this means $\phi$ is continuous, which implies (see basic topology notes) that the subspace topology is finer than $\mathcal{S}$. In other words, $\mathcal{S}$ *is* the subspace topology.

3. Above we've proved that the inclusion of a subspace into its superspace is continuous. It's also clearly injective, and what's more if we restrict the codomain to the image we just get the identity map on $A$. So the inclusion defined on a subspace is actually a topological embedding.

4. The closed subsets in a subspace topology on $A \subseteq X$ are exactly the closed subsets of $X$ intersected with $A$. Proof: $C$ is closed in $A$ iff $A - C$ is open iff $A - C = V \cap A$ for some $V$ open in $X$ iff $C = (X - V) \cap A$.

5. We can talk about transitivity of open and closed sets w.r.t. subspaces: if $U$ is open/closed w.r.t. a subspace $A$ that is open/closed in some space $X$, then $U$ is open/closed in $X$. This is because

    - the intersection of two open/closed sets is again open/closed
    - the subspace's open/closed sets are intersections of open/closed sets in $X$ with $A$


6. A question arises: If $X$ is some space, and $A \subseteq B$ are two subsets of $X$, then is the subspace topology on $A$ relative to (the subspace topology on) $B$ the same as the subspace topology on $A$ relative to $X$?

    The subspace topology relative to $X$ is all open sets of $X$ intersected with $A$. The subspace topology relative to $B$ is all open sets of $B$ intersected with $A$. But the open sets of $B$ are open sets of $X$ intersected with $B$. So they're the same since

    $$U \cap A = U \cap B \cap A$$

    owing to the fact that $B \cap A = A$.

    This means that if $B$ is any subspace of $X$, any subspace of $B$ is also a subspace of $X$.

7. The subspace $A$ of any Hausdorff space $X$ is also Hausdorff because for any two points in $A$ and any disjoint neighborhoods $U, V$ for the points in $X$, when you intersect $U$ and $V$ with $A$ they're still disjoint (and still neighborhoods, obv.)

8. The definition of the subspace basis implies that any subspace of a second countable space is also second countable, because a countable basis for $X$ induces a countable basis for the subspace topology on any subset.
