---
title: "Topology: continuity"
---
These notes depend on [basic topology](topology_basic.html) notes, the [subspace](topology_subspaces.html) notes, and the [bases and countability](topoloby_bases_countability.html) notes.


4. The composition of continuous maps is continuous: If $f: X \to Y$, $g: Y \to Z$ are continuous and $W$ is open in $Z$, then $g^{pre}(W)$ is open in $Y$, so $f^{pre}(g^{pre}(W))$ is open in $X$. But $f^{pre}(g^{pre}(S)) = (g \circ f)^{pre}(S)$ for all $S \subseteq Z$.

    A few simple examples of continuous maps are the **identity map** on any topological space, and any constant map (the pre-image of any set under a constant map is either the whole space or the empty set).

5. The restriction $f|S: S \to Y$ of any continuous map $f: X \to Y$ to a subset $S \subseteq X$ is still continuous due $(f|S)^{pre}(V) = f^{pre}(V) \cap S$, which is open by definition of the subspace.

6. If $f: X \to Y$ is a map and $Y$ has some basis, then $f$ is continuous iff the inverse image of basis elements in $Y$ is open. This follows from the pre-image of a union being a union of pre-images.


7. Here are a couple equivalent characterizations of homeomorphisms, similar to what was done for continuous maps. For any bijective $f: X \to Y$, the following are equivalent:

     a. $f$ is a homeomorphism
     b. $U$ is open in $Y$ iff $f^{pre}(U)$ is open in $X$ for all $U$
     c. $C$ is closed in $Y$ iff $f^{pre}(C)$ is closed in $X$ for all $U$
     d. $f(\text{clo}(A)) = clo(f(A))$ for all $A \subseteq X$

    *Proof:* To prove (a) implies (b), if $f$ is a homeomorphism, then $f^{pre}(U) open in $X$ implies that $g^{pre}(f^{pre}(U) = U$ is open, where $g := f^{-1}$, since $g^{pre}(S) = f(S)$ for all $S \subseteq X$ (and since $f(f^{pre}(S)) = S$ due to bijectivity).

    If (b) holds, then for $C \subseteq Y$, $C$ is closed iff $Y - C$ is open iff $f^{pre}(Y - C) = X - f^{pre}(C)$ is open iff $f^{pre}(C)$ is closed.

    If (c) holds, for any $A$ we have $f(\text{clo}(A))$ must be closed and containing $f(A)$, so $\text{clo}(f(A)) \subseteq f(\text{clo}(A))$. We also know that $f^{pre}(\text{clo}(f(A)))$ is closed in $X$ and contains $A$, so $\text{clo}(A) \subseteq f^{pre}(\text{clo}(f(A)))$ and thus $f(\text{clo}(A)) \subseteq \text{clo}(f(A))$.

    Finally, if (d) holds, then we immediately have that $f$ is closed (using the closure points characterization of continuity). It remains to prove that $f^{-1}(\text{clo}(B)) \subseteq \text{clo}(f^{-1}(B))$ for all $B \subseteq Y$. But $f^{-1}(B) \subseteq X$, so $f(\text{clo} f^{-1}(B)) = \text{clo}(B)$, so applying $f^{-1}$ to both sides gives the desired inequality.


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
