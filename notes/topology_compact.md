---
title: "Topology: compact spaces"
---

1. A space is **compact** if every open cover has a finite subcover. A **compact subset** of $X$ is one that is compact as a subspace.

2. The continuous image of any compact set is compact. Let $f: X \to Y$ be continuous and $X$ compact. If $\mathcal{U}$ is an open cover of $f(X)$, then

    $$\bigcup_{U \in \mathcal{U}} U \supseteq f(X)$$

    implies

    $$\bigcup_{U \in \mathcal{U}} f^{pre}(U) \supseteq f^{pre}(f(X)) \supseteq X$$

    That is, the collection of pre-images of sets in $\mathcal{U}$ is an open cover of $X$. So there's a finite collection of sets $U_1, \ldots, U_n$ such that the $f^{pre}(U_i)$'s cover $X$ by the compactness of $X$.

    Must $U_1, \ldots, U_n$ therefore be a finite subcover for $f(X)$? If $z \in f(X)$, there is an $x \in X$ and an $i$ such that $f(x) = z$ and $x \in f^{pre}(U_i)$. So $z \in U_i$.

3. An immediate corollary of this is that if two spaces $X$ and $Y$ are homeomorphic, then $X$ is compact iff $Y$ is. That is, compactness is a topological property.

4. Closed subsets of compact spaces are compact. Let $X$ be compact and $C$ closed in $X$. Any open cover for $C$ (under the subspace topology) can be expanded into an open cover for $X$, which has a finite subcover $U_1, \ldots, U_n$. This can be shrunk down into open sets in $C$, and they are a finite subcover for $C$.

5. Finite unions of compact sets are compact. If we have $C_1, \ldots, C_n$ compact subsets of $X$, any open cover $\mathcal{U}$ of $Z = \bigcup_1^n C_i$ can be "shrunk" down to an open cover $\mathcal{U}_i$ for each $C_i$. Each one of these has a finite subcover $\mathcal{S}_i$, and we can "expand" each of these subcover elements to a subcollection $\mathcal{S}$ of $\mathcal{U}$. But this must actually be a subcover since the elements collectively cover each $C_i$, hence cover $Z$. $\mathcal{S}$ is also finite, being a finite union of finite sets.

6. Example that infinite unions of compact sets are not necessarily compact: in $\mathbb{R}$, the union of closed intervals $[n - 1/4, n + 1/4]$ for all $n \in \mathbb{N}$. Consider the open cover $(n - 1/2, n + 1/2)$ for all $n$. Each cover element consists exactly one closed interval, so no finite subcollection could cover the whole.

7. Compact subsets of Hausdorff spaces are closed. Let $X$ be a Hausdorff space and $A$ be a compact subset. We will aim to prove that $X - A$ is open.

    Pick an $x \in X - A$. Then for every $a \in A$, we can find neighborhoods in $X$ of $V_a$ of $x$ and $U_a$ of $a$ that are disjoint. The $U_a$'s are an open cover of $A$, so there's some finite subcover $U_{a_i}$ for $1 \leq i \leq n$. Since

    $$\bigcup_1^n U_{a_i} \supseteq A$$

    we have

    $$\bigcap_1^n X - U_{a_i} = X - \bigcup_1^n U_{a_i} \subseteq X - A$$

    By disjointness, however, $V_{a_i} \subseteq X - U_{a_i}$ for all $i$. So $\bigcap_1^n V_{a_i} \subseteq X - A$ is an open neighborhood of $x$ contained in $X - A$.

    Since $x$ was arbitrary, $X - A$ is open and therefore $A$ is closed.

8. Compact subsets of metric spaces are bounded. This one's pretty easy: suppose $X$ is a metric space and $A$ is a compact subset. Assuming $A$ is non-empty, let $x \in A$ and consider the open cover of all open balls centered at $x$. There's a finite subcover, that means there's one subcover element containing all the others (i.e. there's a *singleton* subcover). So $A$ is bounded.

    By (5), compact subsets of metric spaces are also closed, since metric spaces are Hausdorff.

9. Note that compact subsets are defined as being those subsets that are compact as subspaces. This means to prove something is compact we need to work with an open cover *with respect to the subspace topology*. Sometimes it's convenient to work with an open cover with respect to the original space, however.

    Luckily we can prove that a subset $A$ of some space $X$ is compact iff for every $X$-open cover of $A$, there is a finite subcover. If $X$ is compact, any $X$-open cover can be restricted to an $A$-open cover which has a finite subcover by compactness and can be expanded to a subcover of the $X$-open cover. Conversely, if every $X$-open cover of $A$ has a finite subcover, then any $A$-open cover has an associated $X$-open cover, and its finite subcover is associated with a finite subcover of the $A$-open cover.

    Essentially, the nature of the subspace topology allows us to pass easily between $X$-open covers and $A$-open covers.

10. A space is **sequentially compact** if every infinite sequence has a convergent subsequence. A space is **limit point compact** if every infinite subset of the space has a limit point in the space.

11. Every compact space is limit point compact. Suppose $X$ is compact and $S$ is an infinite subset with no limit points in $X$. Then necessarily $S$ is closed (see basic topology notes), and so is a compact subset of $X$. Due to lack of limit points it consists entirely of isolated points, so each point in the set has a neighborhood disjoint from the other points. These collectively form an open cover of $S$, so by compactness there is a finite subcover. But each cover element contains only one point of $S$ and there are infinitely many points, a contradiction.

12. Sequentially compact metric spaces are totally bounded. *Proof:* If not there's some $r > 0$ such that $X$ is not covered by any finite number of balls of radius $r$. So we can pick $x_1 \in X$ arbitrarily, $x_2 \notin B(x_1; r)$, $x_3 \notin B(x_1; r) \cup B(x_2; r)$, and so on, indefinitely. If this sequence had a convergent subsequence with limit $c$ you'd be able to find two terms (infinitely many actually, but at least two) that are within $r/2$ of $c$, implying that terms are within $r$ of one another. This is baloney according to how the sequence was constructed.

13. Any sequentially compact metric space is second-countable. Suppose $X$ is a sequentially compact metric space. It suffices to prove that $X$ is separable (since they are equivalent for metric spaces). We know $X$ is totally bounded (by the previous proposition) so for every $n \in \mathbb{N}$, there are a finite collection of points $x^n = \{ x_1^n, \ldots, x_{m_n}^n\}$ for which the open balls of radius $1/n$ centered at the points cover the space. Then the set $C := \bigcup_n x^n$ is countable, and for any $a \in X$ and any open ball $B(a; \epsilon)$, just find an $n$ such that $1/n < \epsilon$ and choose one element $x_k^n$ such that $a \in B(x_k^n; 1/n)$. This element will be in $B(a; \epsilon)$, so $C$ is dense in $X$.

14. Any second countable, sequentially compact space is compact. First, second countable spaces are Lindelöf, so any open cover of $X$ has a countable subcover $\{U_n : n \in \mathbb{N}\}$. If there's no finite subcover, then make a sequence by picking arbitrary $x_1$, $x_2 \notin U_1$, \ldots, $x_{k+1} \notin \bigcup_1^k U_i$ for all $k$. If this sequence has a convergent subsequence converging to $a$. There is some $U_k$ that is a neighborhood of $a$, so we can find infinitely many sequence terms in $U_k$, which contradicts that at most finitely many are.

15. For any second-countable space or metric space, sequential compactness implies compactness. This is just combining the previous three propositions, since sequentially compact metric spaces are second-countable.

16. For first-countable $T_1$ spaces, limit point compactness implies sequential compactness. *Proof:* If $(x_n)$ is any sequence, we assume it has infinitely many distinct terms (otherwise it is eventually constant and therefore converges). The set of terms is therefore infinite, and so by limit point compactness has a limit point $a$. We can furthermore suppose that $a$ is at most finitely many different terms of the sequence, otherwise it is once again eventually constant. Then chop off the finite terms to obtain a subsequence, call it $(y_n)$, of $(x_n)$ for which no term is equal to $a$.

    By first-countability, there is a countable neighborhood basis $\{U_n : n \in \mathbb{N}\}$ for $a$. Now we make a nested sequence of neighborhoods of $a$ by defining $V_n := \bigcup_1^n U_i$ for all $n$, so $V_k \supseteq V_{k+1}$ for all $k$. Note that the $V_i$'s are still a neighborhood basis for $a$ since they are each subsets of neighborhood basis elements.

    Note that if we have any subsequence $(y_{n_k})$ such that each $y_{n_k} \in V_k$, for any neighborhood $A$ of $a$, there is some $V_j$ contained in $A$, and all subsequent terms of the subsequence are also contained in $V_j$ by nestedness. So any such subsequence $(y_{n_k})$ is convergent.

    Now we pick $n_1$ such that $y_{n_1} \in V_1$. Suppose by induction that we have $n_1, \ldots, n_k$ with $n_i < n_{i+1}$ for $1 \leq i < k$, such that $y_{n_i} \in V_i$. The neighborhood $V_{k+1}$ intersects the term set in infinitely many points distinct from $a$ (because the space is $T_1$), so we can find a $n_{k+1} > n_k$ such that $y_{n_{k+1}} \in V_{k+1}$. Thus we have a convergent subsequence, which establishes sequential compactness.


17. We have proved that for second-countable Hausdorff spaces or metric spaces, the following 3 conditions are equivalent:

     1. $M$ is compact
     2. $M$ is limit point compact
     3. $M$ is sequentially compact

    where (2) => (3) holds because because metric spaces and second-countable Hausdorff spaces are both first-countable $T_1$ spaces.

    Great job.


18. Any compact metric space is complete. This is actually real easy to do using (11): A metric space is compact iff it is sequentially compact, so any Cauchy sequence $(x_n)$ in a compact metric space has a convergent subsequence (by sequential compactness), which implies that $(x_n)$ converges.

19. A **compactification** of a space $X$ is any superset $Y$ equipped with a topology that makes $Y$ compact, makes $X$ a dense subset of $Y$, and makes the subspace topology on $X$ (w.r.t. $Y$) the original topology on $X$.
