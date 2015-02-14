1. A topological space is **disconnected** if there are two disjoint, non-empty open subsets of $X$ that cover $X$, and **connected** otherwise. Equivalently, connected iff there are no proper clopen subsets. A subset $S$ of $X$ is a **connected subset** when $S$ is connected as a subspace.

2. The continuous image of any connected space is connected. Letting $f: X \to Y$ be continuous, if $f(X)$ is disconnected by $A, B \subseteq f(X)$, then there are $U, V$ open in $Y$ such that $A = U \cap f(X)$, $B = V \cap f(X)$. We have:

     - $f^{pre}(U) = f^{pre}(A)$ and $f^{pre}(V) = f^{pre}(B)$ are both open by continuity
     - they must be disjoint since $A$ and $B$ are.
     - they cover $X$ since $A$ and $B$ cover the image.

    That is, we have a disconnection of $X$, contrary to assumption.

3. We can define an equivalence relation on points of $X$ by $x \sim y$ iff there is a connected subset of $X$ containing both $x$ and $y$. It is obviously reflexive (singletons are connected) and symmetric. If $x \sim y$ and $y \sim z$, there is a $U$ containing $x, y$ and a $V$ containing $y, z$, both connected subsets of $X$. Then $W := U \cup V$ is also connected: if not, it has a disconnection $A, B$. If $A$ and $B$ both have non-empty intersections with $U$, then $A \cap U, B \cap U$ is a disconnection of $U$, which is impossible. The same goes for $V$. So we must have (WLOG) $A = U$, $B = V$, which contradicts that $U$ and $V$ share the point $y$.

    So $\sim$ is an equivalence relation, and the equivalence classes are called the **connected components** of $X$. Properties of the components include:

     - Each component is a *maximal* connected component, since being able to add any other element and still have it be connected would collapse two equivalence classes into one, which is contrary to the definition of $\sim$. 
     - Also, no connected subset crosses components for the same reason. 
     - Also, the union of connected subsets with a point in common is a connected subset, since by definition they must all belong to the same component.

4. A **path from $p$ to $q$** in a space $X$ is a continuous map $\phi: [0, 1] \to X$, where $[0, 1]$ is the closed interval in $\mathbb{R}$ and $\phi(0) = p$, $\phi(1) = q$. A space $X$ is **path-connected** if any two points in the space have some path between them.

5. We can again define an equivalence relation on a space $X$ by $x \sim y$ iff $x$ and $y$ have a path from $x$ to $y$. Reflexivity holds because the constant path $t \mapsto x$ works. The relation is also symmetric because for any path $p$ from $x$ to $y$, the path $q(t) := p(1-t)$ is a path from $y$ to $x$. Finally, if $p$ is a path from $x$ to $y$ and $q$ is a path from $y$ to $z$, then the path

    $$r(t) = \begin{cases}
        p(2t) & 0 \leq t \leq 1/2 \\
        q(2t - 1) & 1/2 < t \leq 1
        \end{cases}$$

    is a path by the gluing lemma.

    The equivalence classes of this relation are called the **path-components**. All the same properties as for connected components hold:

     - Each path-component is a *maximal* connected component
     - No path-connected subset crosses path-components.
     - The union of path-connected subsets with a point in common is a path-connected subset.

6. Every path-connected space is connected. If $X$ is path-connected but not connected, it has a disconnection $A, B$. Let $a \in A, b \in B$. There must be a path $p$ from $a$ to $b$, but the image of $p$ in $X$ must be connected since $p$ is continuous. However, $A \cap img p$ and $B \cap img p$ are open, disjoint and cover $img p$, so $img p$ is disconnected, which is a contradiction.

7. A space is **compact** if every open cover has a finite subcover. A **compact subset** of $X$ is one that is compact as a subspace.

8. The continuous image of any compact set is compact. Let $f: X \to Y$ be continuous and $X$ compact. If $\mathcal{U}$ is an open cover of $f(X)$, then

    $$\bigcup_{U \in \mathcal{U}} U \superseteq f(X)$$

    implies

    $$\bigcup_{U \in \mathcal{U}} f^{pre}(U) \superseteq f^{pre}(f(X)) \superseteq X$$

    That is, the collection of pre-images of sets in $\mathcal{U}$ is an open cover of $X$. So there's a finite collection of sets $U_1, \ldots, U_n$ such that the $f^{pre}(U_i)$'s cover $X$ by the compactness of $X$.

    Must $U_1, \ldots, U_n$ therefore be a finite subcover for $f(X)$? If $z \in f(X)$, there is an $x \in X$ and an $i$ such that $f(x) = z$ and $x \in f^{pre}(U_i)$. So $z \in U_i$.

9. Closed subsets of compact spaces are compact. Let $X$ be compact and $C$ closed in $X$. Any open cover for $C$ (under the subspace topology) can be expanded into an open cover for $X$, which has a finite subcover $U_1, \ldots, U_n$. This can be shrunk down into open sets in $C$, and they are a finite subcover for $C$.

10. Finite unions of compact sets are compact. If we have $C_1, \ldots, C_n$ compact subsets of $X$, any open cover $\mathcal{U}$ of $Z = \bigcup_1^n C_i$ can be "shrunk" down to an open cover $\mathcal{U}_i$ for each $C_i$. Each one of these has a finite subcover $\mathcal{S}_i$, and we can "expand" each of these subcover elements to a subcollection $\mathcal{S}$ of $\mathcal{U}$. But this must actually be a subcover since the elements collectively cover each $C_i$, hence cover $Z$. $\mathcal{S}$ is also finite, being a finite union of finite sets.


11. Compact subsets of Hausdorff spaces are closed. Let $X$ be a Hausdorff space and $A$ be a compact subset. We will aim to prove that $X - A$ is open.

    Pick an $x \in X - A$. Then for every $a \in A$, we can find neighborhoods in $X$ of $V_a$ of $x$ and $U_a$ of $a$ that are disjoint. The $U_a$'s are an open cover of $A$, so there's some finite subcover $U_{a_i}$ for $1 \leq i \leq n$. Since

    $$\bigcup_1^n U_{a_i} \superseteq A$$

    we have

    $$\bigcap_1^n X - U_{a_i} = X - \bigcup_1^n U_{a_i} \subseteq X - A$$

    By disjointness, however, $V_{a_i} \subseteq X - U_{a_i}$ for all $i$. So $\bigcap_1^n V_{a_i} \subseteq X - A$ is an open neighborhood of $x$ contained in $X - A$.

    Since $x$ was arbitrary, $X - A$ is open and therefore $A$ is closed.

12. Compact subsets of metric spaces are bounded. This one's pretty easy: suppose $X$ is a metric space and $A$ is a compact subset. Assuming $A$ is non-empty, let $x \in A$ and consider the open cover of all open balls centered at $x$. There's a finite subcover, that means there's one subcover element containing all the others (i.e. there's a *singleton* subcover). So $A$ is bounded.
