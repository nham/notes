## Connected spaces

A topological space is **disconnected** if there are two disjoint, non-empty open subsets of $X$ that cover $X$, and **connected** otherwise. Equivalently, connected iff there are no proper clopen subsets. A subset $S$ of $X$ is a **connected subset** when $S$ is connected as a subspace.

### Continuous images of connected spaces

The continuous image of any connected space is connected. Letting $f: X \to Y$ be continuous, if $f(X)$ is disconnected by $A, B \subseteq f(X)$, then there are $U, V$ open in $Y$ such that $A = U \cap f(X)$, $B = V \cap f(X)$. We have:

 - $f^{pre}(U) = f^{pre}(A)$ and $f^{pre}(V) = f^{pre}(B)$ are both open by continuity
 - they must be disjoint since $A$ and $B$ are.
 - they are non-empty since $A$ and $B$ are, again
 - they cover $X$ since $A$ and $B$ cover the image.

That is, we have a disconnection of $X$, contrary to assumption.

An immediate corollary of this is that if two spaces $X$ and $Y$ are homeomorphic, then $X$ is connected iff $Y$ is. That is, connectedness is a topological property.

### Connected components

Let $X$ be a topological space, and let $U$ and $V$ be two connected, non-disjoint subsets. Then $U \cup V$ is also connected.

Suppose $U \cup V$ has a disconnection by $A$ and $B$, instead. Then $A$ and $B$ are open in $U \cup V$, so by the definition of the subspace topology there are $X$-open sets $C, D$ that yield $A$ and $B$ when intersected with $U \cup V$ (respectively).

If both $C \cap U$ and $D \cap U$ are non-empty, then they form a disconnection of $U$ ($C \cap U$ and $D \cap U$ are disjoint. Also they cover $U \cup V$, so certainly cover $U$). This is contrary to assumption. Similarly, if both $C \cap V$ and $D \cap V$ are non-empty, then $V$ is disconnected. So we must actually have $C = A, D = B$ or $C = B, D = A$. But this can't be a disconnection of $U \cup V$ since $U$ and $V$ are non-disjoint by hypothesis.

We can define an equivalence relation on points of $X$ by $x \sim y$ iff there is a connected subset of $X$ containing both $x$ and $y$. It is obviously reflexive (singletons are connected just because it's not possible to disconnect them) and symmetric. If $x \sim y$ and $y \sim z$, there is a $U$ containing $x, y$ and a $V$ containing $y, z$, both connected subsets of $X$. So $U \cup V$ is connected by the previous proposition, and contains both $x$ and $z$, which establishes $x \sim z$.

So $\sim$ is an equivalence relation, and the equivalence classes are called the **connected components** of $X$. Properties of the components include:

 - Each component is a *maximal* connected subset since no connected subset can contain elements from more than one component (points that are in two different components are by definition points that do not have a connected set containing them)
 - Restating this: no connected subset crosses components.
 - Also, the union of connected subsets with a point in common is a connected subset, since by definition they must all belong to the same component.

## Path-connected spaces

A **path from $p$ to $q$** in a space $X$ is a continuous map $\phi: [0, 1] \to X$, where $[0, 1]$ is the closed interval in $\mathbb{R}$ and $\phi(0) = p$, $\phi(1) = q$. A space $X$ is **path-connected** if any two points in the space have some path between them.

### Continuous images of path-connected spaces

The continuous image of any path-connected space is path-connected. Suppose $f: X \to Y$ is continuous and $X$ is path-connected. Let $u, v \in f(X)$. Then there are $a, b \in X$ such that $f(a) = u, f(b) = v$. $X$ is path-connected, so there is a path $p$ from $a$ to $b$. Then $f \circ p$ is a path in $f(X)$ from $u$ to $v$.

An immediately corollary is that if $X$ and $Y$ are homeomorphic, then $X$ is path-connected iff $Y$ is.

### Path components

We can again define an equivalence relation on a space $X$ by $x \sim y$ iff $x$ and $y$ have a path from $x$ to $y$. Reflexivity holds because the constant path $t \mapsto x$ works. The relation is also symmetric because for any path $p$ from $x$ to $y$, the path $q(t) := p(1-t)$ is a path from $y$ to $x$. Finally, if $p$ is a path from $x$ to $y$ and $q$ is a path from $y$ to $z$, then the path

$$r(t) = \begin{cases}
    p(2t) & 0 \leq t \leq 1/2 \\
    q(2t - 1) & 1/2 < t \leq 1
\end{cases}$$

is a path by the gluing lemma.

The equivalence classes of this relation are called the **path-components**. All the same properties as for connected components hold:

 - Each path-component is a *maximal* connected component
 - No path-connected subset crosses path-components.
 - The union of path-connected subsets with a point in common is a path-connected subset.


### Path-connected implies connected

Every path-connected space is connected. If $X$ is path-connected but not connected, it has a disconnection $A, B$. Let $a \in A, b \in B$. There must be a path $p$ from $a$ to $b$, but the image of $p$ in $X$ must be connected since $p$ is continuous. However, $A \cap img p$ and $B \cap img p$ are open, disjoint and cover $img p$, so $img p$ is disconnected, which is a contradiction.

## Locally path-connected spaces

A space is **locally path-connected** if it has a basis for which each basis element is path connected.

### Facts about locally path-connected spaces

1. All the components of a locally path-connected space are open. Suppose that $C$ is one of the components, and suppose it contains a boundary point $b$. Then there is some basis element containing $b$. That basis element $B$ is path-connected, hence connected. So $C \cup B$ is a union of non-disjoint connected subsets, hence connected. But C \cup B$ is a strict superset of $C$ since every neighborhood of $b$ intersects both $C$ and $X - C$, which contradicts that $C$ is a maximal connected subset.

    It's actually somewhat easier to prove that path components are open? If $P$ is a path component of a locally path-connected space and it contains a boundary point $B$, we can find a neighborhood $V$ of $b$ that is path-connected. So $P \cup V$ is a union of non-disjoint path-connected subsets, hence path-connected, and it is strictly larger than $P$, which contradicts that $P$ is a maximal path-connected subset.

2. If $X$ is locally path-connected, then its path-components are the same as the components. The proof goes a little something like this: Note that since path-components are all connected, every path component lies in a component.

    Now suppose $C$ is any component and let $x \in C$. Let $P$ be $x$'s  path component. $C$ is actually partitioned by path components by what was just said. If there's more than one path component, it's a disconnection of $C$ due to path components being open. So not only does this prove that every component is a path component, but every path component is a component as well.

3. In a locally path-connected space, a subset is connected iff it is path connected. One direction (path-connected implies connected) was proven above for all topological spaces, but if $A$ is any connected subset, it lies in a path-component (since components and path-components coincide, as shown in (9)) and hence is path-connected.
