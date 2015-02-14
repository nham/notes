---
title: "Topology: compact spaces"
---

1. A space is **compact** if every open cover has a finite subcover. A **compact subset** of $X$ is one that is compact as a subspace.

2. The continuous image of any compact set is compact. Let $f: X \to Y$ be continuous and $X$ compact. If $\mathcal{U}$ is an open cover of $f(X)$, then

    $$\bigcup_{U \in \mathcal{U}} U \superseteq f(X)$$

    implies

    $$\bigcup_{U \in \mathcal{U}} f^{pre}(U) \superseteq f^{pre}(f(X)) \superseteq X$$

    That is, the collection of pre-images of sets in $\mathcal{U}$ is an open cover of $X$. So there's a finite collection of sets $U_1, \ldots, U_n$ such that the $f^{pre}(U_i)$'s cover $X$ by the compactness of $X$.

    Must $U_1, \ldots, U_n$ therefore be a finite subcover for $f(X)$? If $z \in f(X)$, there is an $x \in X$ and an $i$ such that $f(x) = z$ and $x \in f^{pre}(U_i)$. So $z \in U_i$.

3. Closed subsets of compact spaces are compact. Let $X$ be compact and $C$ closed in $X$. Any open cover for $C$ (under the subspace topology) can be expanded into an open cover for $X$, which has a finite subcover $U_1, \ldots, U_n$. This can be shrunk down into open sets in $C$, and they are a finite subcover for $C$.

4. Finite unions of compact sets are compact. If we have $C_1, \ldots, C_n$ compact subsets of $X$, any open cover $\mathcal{U}$ of $Z = \bigcup_1^n C_i$ can be "shrunk" down to an open cover $\mathcal{U}_i$ for each $C_i$. Each one of these has a finite subcover $\mathcal{S}_i$, and we can "expand" each of these subcover elements to a subcollection $\mathcal{S}$ of $\mathcal{U}$. But this must actually be a subcover since the elements collectively cover each $C_i$, hence cover $Z$. $\mathcal{S}$ is also finite, being a finite union of finite sets.

5. Compact subsets of Hausdorff spaces are closed. Let $X$ be a Hausdorff space and $A$ be a compact subset. We will aim to prove that $X - A$ is open.

    Pick an $x \in X - A$. Then for every $a \in A$, we can find neighborhoods in $X$ of $V_a$ of $x$ and $U_a$ of $a$ that are disjoint. The $U_a$'s are an open cover of $A$, so there's some finite subcover $U_{a_i}$ for $1 \leq i \leq n$. Since

    $$\bigcup_1^n U_{a_i} \superseteq A$$

    we have

    $$\bigcap_1^n X - U_{a_i} = X - \bigcup_1^n U_{a_i} \subseteq X - A$$

    By disjointness, however, $V_{a_i} \subseteq X - U_{a_i}$ for all $i$. So $\bigcap_1^n V_{a_i} \subseteq X - A$ is an open neighborhood of $x$ contained in $X - A$.

    Since $x$ was arbitrary, $X - A$ is open and therefore $A$ is closed.

6. Compact subsets of metric spaces are bounded. This one's pretty easy: suppose $X$ is a metric space and $A$ is a compact subset. Assuming $A$ is non-empty, let $x \in A$ and consider the open cover of all open balls centered at $x$. There's a finite subcover, that means there's one subcover element containing all the others (i.e. there's a *singleton* subcover). So $A$ is bounded.
