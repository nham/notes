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



