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

5. Example that infinite unions of compact sets are not necessarily compact: in $\mathbb{R}$, the union of closed intervals $[n - 1/4, n + 1/4]$ for all $n \in \mathbb{N}$. Consider the open cover $(n - 1/2, n + 1/2)$ for all $n$. Each cover element consists exactly one closed interval, so no finite subcollection could cover the whole.

6. Compact subsets of Hausdorff spaces are closed. Let $X$ be a Hausdorff space and $A$ be a compact subset. We will aim to prove that $X - A$ is open.

    Pick an $x \in X - A$. Then for every $a \in A$, we can find neighborhoods in $X$ of $V_a$ of $x$ and $U_a$ of $a$ that are disjoint. The $U_a$'s are an open cover of $A$, so there's some finite subcover $U_{a_i}$ for $1 \leq i \leq n$. Since

    $$\bigcup_1^n U_{a_i} \superseteq A$$

    we have

    $$\bigcap_1^n X - U_{a_i} = X - \bigcup_1^n U_{a_i} \subseteq X - A$$

    By disjointness, however, $V_{a_i} \subseteq X - U_{a_i}$ for all $i$. So $\bigcap_1^n V_{a_i} \subseteq X - A$ is an open neighborhood of $x$ contained in $X - A$.

    Since $x$ was arbitrary, $X - A$ is open and therefore $A$ is closed.

7. Compact subsets of metric spaces are bounded. This one's pretty easy: suppose $X$ is a metric space and $A$ is a compact subset. Assuming $A$ is non-empty, let $x \in A$ and consider the open cover of all open balls centered at $x$. There's a finite subcover, that means there's one subcover element containing all the others (i.e. there's a *singleton* subcover). So $A$ is bounded.

    By (5), compact subsets of metric spaces are also closed, since metric spaces are Hausdorff.

8. Note that compact subsets are defined as being those subsets that are compact as subspaces. This means to prove something is compact we need to work with an open cover *with respect to the subspace topology*. Sometimes it's convenient to work with an open cover with respect to the original space, however.

    Luckily we can prove that a subset $A$ of some space $X$ is compact iff for every $X$-open cover of $A$, there is a finite subcover. If $X$ is compact, any $X$-open cover can be restricted to an $A$-open cover which has a finite subcover by compactness and can be expanded to a subcover of the $X$-open cover. Conversely, if every $X$-open cover of $A$ has a finite subcover, then any $A$-open cover has an associated $X$-open cover, and its finite subcover is associated with a finite subcover of the $A$-open cover.

    Essentially, the nature of the subspace topology allows us to pass easily between $X$-open covers and $A$-open covers.

9. A space is **sequentially compact** if every infinite sequence has a convergent subsequence. A space is **limit point compact** if every infinite subset of the space has a limit point in the space.

10. Every compact space is limit point compact. Suppose $X$ is compact and $S$ is an infinite subset with no limit points in $X$. Then necessarily $S$ is closed (see basic topology notes), and so is a compact subset of $X$. Due to lack of limit points it consists entirely of isolated points, so each point in the set has a neighborhood disjoint from the other points. These collectively form an open cover of $S$, so by compactness there is a finite subcover. But each cover element contains only one point of $S$ and there are infinitely many points, a contradiction.

11. If $M$ is either a second-countable Hausdorff space or a metric space, then the following 3 conditions are equivalent:

    1. $M$ is compact
    2. $M$ is limit point compact
    3. $M$ is sequentially compact

    *Proof for metric spaces:* By the previous proposition (1) implies (2)

    We now prove (2) implies (3). If (2) holds and $M$ is not sequentially compact, some sequence $(x_n)$ has no convergent subsequence. There must be infinitely different values in the sequence, for if there were not you could extract an eventually constant (hence convergent) subsequence. By assumption the term set has an accumulation point $c$. Since this is a metric space, every open ball around the accumulation point contains infinitely many elements of the term set, so we construct a sequence inductively: $B(c; 1)$ contains some $x_{n_1}$, $B(c; 1/2)$ contains some $x_{n_2}$ with $n_2 > n_1$, and if $x_{n_k}$ is chosen, $x_{n_{k+1}}$ is some point in $B(c; 1/k)$ with $n_{k+1} > n_k$. This is a subsequence converging to $c$.

    To complete the proof we assume (3) and prove (1). We need two dumb things first:

    **Proposition:** Sequentially compact metric spaces are totally bounded. *Proof:* If not there's some $r > 0$ such that $X$ is not covered by any finite number of balls of radius $r$. So we can pick $x_1 \in X$ arbitrarily, $x_2 \notin B(x_1; r)$, $x_3 \notin B(x_1; r) \cup B(x_2; r)$, and so on, indefinitely. If this sequence had a convergent subsequence with limit $c$ you'd be able to find two terms (infinitely many actually, but at least two) that are within $r/4$ of $c$, implying that terms are within $r/2$ of one another. This is baloney according to how the sequence was constructed.

    **Proposition:** If $X$ is a sequentially compact metric space, any open cover $\mathcal{U}$ has some $r > 0$ such that for each $x \in X$, $B(x; r)$ is contained in a cover element. *Proof:* Assume the contrary, so that $\forall r$ there is some $x_r$ with $B(x_r; r)$ not contained in any single cover element. By sequential compactness there's some subsequence converging to a limit $c$. But $c$ is in some cover element, so there's a ball $B(c; \epsilon)$ contained in that cover element, so by convergence some tail sequence starting at $n_j$ is contained in $B(c; \epsilon/2)$. At some point the subsequence's terms $n_k$ are such that both a) $1/n_k$ is smaller than $\epsilon/2$ and b) $n_k > n_j$, so that $B(n_k; 1/n_k)$ is contained in $B(c; \epsilon)$ and hence in a cover element, contrary to our construction of the terms of $(x_n)$.

    Now for the main event: If $X$ is sequentially compact and $\mathcal{U}$ any open cover for it, by the second proposition we can find an $r > 0$ with every $D_x := B(x; r)$ contained in some cover element. But by totally boundedness, finitely many $D_{x_1}, \ldots, D_{x_n}$ cover the space. So a finite number of cover elements contain these balls, and hence cover the space. This is a finite subcover and yayyyyy it's over.


12. Any compact metric space is complete. This is actually real easy to do using (8): A metric space is compact iff it is sequentially compact, so any Cauchy sequence $(x_n)$ in a compact metric space has a convergent subsequence (by sequential compactness), which implies that $(x_n)$ converges.
