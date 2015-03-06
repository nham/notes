---
title: "Topology: continuity"
---
These notes depend on [basic topology](topology_basic.html) notes, the [subspace](topology_subspaces.html) notes, and the [bases and countability](topoloby_bases_countability.html) notes.

1. A **continuous map** is any function $f: X \to Y$ (where $X$ and $Y$ are topological spaces) such that every open $V \subseteq Y$ has $f^{pre}(V)$ open in $X$.

    If $f$ is bijective, continuous, with continuous inverse, it is called a **homeomorphism**. This is the notion of isomorphism for topological spaces.

2. There's a bunch of equivalent definitions for continuous maps. Here are three. Let $f: X \to Y$ be a map between topological spaces. Then $f$ is continuous exactly when either of these hold:

    1. For every $x \in X$ and any neighborhood $V$ of $f(x)$ in $Y$, there is a neighborhood $U$ of $x$ such that $f(U) \subseteq V$.
    2. $f^{pre}(C)$ is closed for every $C$ closed in $Y$
    3. For any $A \subseteq X$, $f$ maps closure points of $A$ to closure points of $f(A)$.

    If (1) is true, for any open $V$ in $Y$, either there is some $x \in X$ such that $f(x) \in V$, or $f^{pre}(V) = \emptyset$ and is hence open. In the former case by hypothesis there is some neighborhood of $x$ contained in $f^{pre}(V)$, so this set is open, proving $f$ is continuous. The converse is proved by noting that for every $x \in X$ and neighborhood $V$ of $f(x)$, $f^{pre}(V)$ is an open neighborhood of $x$ that works.

    For (2), note that $f^{pre}(Y - S) = X - f^{pre}(S)$ for any $S \subseteq Y$. So if preimages of open sets are all open, then so are preimages of closed sets, and vice versa.

    For (3), if $f$ is continuous and $A \subseteq X$, if $z$ is a closure point of $A$ such that $f(z)$ isn't a closure point of $f(A)$, then $f(z)$ has a neighborhood $V$ that is disjoint from $f(A)$. So $f^{pre}(V)$ is a neighborhood of $z$ by continuity, and it must not intersect $A$, since if it contained some $a \in A$, $f(a)$ would be in $V \cap f(A)$. But we assumed $z$ was a closure point, so it must intersect $A$. Conversely, if (3) holds and $C$ is closed in $Y$, every closure point of $f^{pre}(C)$ gets mapped into a closure point of $f(f^{pre}(C)) \subseteq C$, hence a closure point of $C$. $C$ being closed, this proves that $f^{pre}(C)$ contains its closure, so is closed.

3. It's actually improper to say that $f: X \to Y$ is a continuous map, since we have to specify topologies for $X$ and $Y$ as well. It's more accurate to say that $(f: X \to Y, \mathcal{T}, \mathcal{U})$ is a continuous map. Indeed, a given function $f: X \to Y$ can be continuous when $X$ is considered to have one topology, but not continuous when it has another. One way to see this has applications to coarseness of topologies:

    If $\mathcal{S}, \mathcal{T}$ are two topologies on $X$, then $\mathcal{S}$ is finer than $\mathcal{T}$ iff the identity on $X$ is continuous when the domain has topology $\mathcal{S}$ and the codomain has topology $\mathcal{T}$. (This follows immediately from the definition of continuity). Intuitively, if the codomain topology is finer, then the domain topology lacks the necessary "precision" needed for the output to be kept within any neighborhood in the codomain.


4. The composition of continuous maps is continuous: If $f: X \to Y$, $g: Y \to Z$ are continuous and $W$ is open in $Z$, then $g^{pre}(W)$ is open in $Y$, so $f^{pre}(g^{pre}(W))$ is open in $X$. But $f^{pre}(g^{pre}(S)) = (g \circ f)^{pre}(S)$ for all $S \subseteq Z$.

    A few simple examples of continuous maps are the **identity map** on any topological space, and any constant map (the pre-image of any set under a constant map is either the whole space or the empty set).

5. The restriction $f|S: S \to Y$ of any continuous map $f: X \to Y$ to a subset $S \subseteq X$ is still continuous due $(f|S)^{pre}(V) = f^{pre}(V) \cap S$, which is open by definition of the subspace.

6. If $f: X \to Y$ is a map and $Y$ has some basis, then $f$ is continuous iff the inverse image of basis elements in $Y$ is open. This follows from the pre-image of a union being a union of pre-images.



7. A map $f: X \to Y$ is a homeomorphism iff $f$ is bijective and $U$ is open in $Y$ iff $f^{pre}(U)$ is open in $X$ for all $U$.

    If $f$ is a homeomorphism, then $f^{pre}(U) open in $X$ implies that $g^{pre}(f^{pre}(U) = U$, where $g := f^{-1}$, since $g^{pre}(S) = f(S)$ for all $S \subseteq X$ (and since $f(f^{pre}(S)) = S$ due to bijectivity).

    Conversely, assuming the latter condition we need to prove that $g := f^{-1}$ is continuous. Similar manipulations prove it.


8. There are a couple notions of continuous maps that we can define with the notion of subspaces.

     A **topological embedding** is an injective continuous map $f: X \to Y$ such that the codomain restriction $X \to f(X)$ is a homeomorphism (where $f(X)$ is a subspace of $Y$).

     A **local homeomorphism** is a function $f: X \to Y$ such that for every $x \in X$ there is a neighborhood $U$ of $x$ with

     - $f(U)$ open in $Y$
     - the two-sided restriction of $f$, $F: U \to f(U)$, is a homeomorphism

9. The two-sided restriction of any homeomorphism $f: X \to Y$ to $A \to f(A)$ is also a homeomorphism. *Proof:* The restriction $g$ is still bijective, for any $U$ open in $f(A)$, $U = V \cap f(A)$ for some $V$ open in $Y$, so $g^{pre}(U) = f^{pre}(U) \cap A = f^{pre}(V) \cap A$ since $U \subseteq A$ and since no element of $a$ can be mapped to any point in $V$ that is outside of $U$, and since $f^{pre}(V)$ is open in $X$ by continuity, $g^{pre}(U)$ is open in $A$.

    The inverse of $g$ is just the restriction of $f^{-1}$, so by the same argument $g^{-1}$ is continuous. This proves that $g$ is a homeomorphism.


10. Every homeomorphism $f: X \to Y$ is also a local homeomorphism (i.e. one can think of vanilla homeomorphisms as *global homeomorphisms*). This is immediate from the definitions, since for every $a \in X$ we can use $X$ itself as the neighborhood.

11. We can also characterize continuous maps locally: if $f: X \to Y$ and for every $x \in X$, there is a neighborhood $U_x$ of $x$ such that $f|U_x$ is continuous, then for every $V$ open in $Y$, $f^{pre}(V) \cap U_x$ is open in $U_x$, so $f^{pre}(V) \cap U_x \cap V_x$ is open in $X$ for some $V_x$ open in $X$. If we union these up for all $x$ we get $f^{pre}(V)$ being open.

    The converse is obviously true as well.


12. Here it is, that moment you've been waiting for: the gluing lemma(s?). If we have either:

     - $B_1, \ldots, B_n$ is a finite closed (w.r.t. $X$) cover of $X$
     - $\{B_i\} is an open (w.r.t. $X$) cover of $X$

    And for each cover element $B_i$ we have a map $f_i: B_i \to Y$ that is continuous, such that for each $i$ and $j$, $f_i$ and $f_j$ are the same on the restriction to $B_i \cap B_j$, then there's a unique continuous map $f: X \to Y$ such that $f|B_i = f_i$ for all $i$.

    *Proof:* In either case, for all $x \in X$, pick an $i$ such that $x \in B_i$. Then define $f(x) = f_i(x)$. This is not only well-defined since $f_i(x) = f_j(x)$ when $x \in B_i \cap B_j$, but $f$ is the only such way to have $f|B_i = f_i$ for all $i$.

    In the case of a finite closed cover we have

    $$f^{pre}(C) = \bigcup_{i=1}^n f_i^{pre}(C)$$

    which, in the case of closed $C$, is a finite union of closed sets (since each $f_i$ is continuous), hence closed in $X$.

    In the case of an open cover we have

    $$f^{pre}(U) = \bigcup_i f_i^{pre}(U)$$

    which, in the case of open $U$, is a union of open sets, hence open in $X$.
