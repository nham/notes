1. An **interval** of $\mathbb{R}$ is a subset $I$ such that for all $a, b \in I$, $a < x < b$ implies that $x \in I$. This includes as degenerate cases singletons and the empty set.

2. Every interval is connected. *Proof:* We can clearly ignore degenerate cases, they are connected. Suppose $A$ and $B$ are a disconnection of $I$. There is some $a \in A$, $b \in B$. WLOG we assume $a < b$. Then interval $[a, b]$ has to be contained in $I$.
Consider $c := \inf \{ x \in B : a < x \}$, which is valid since $a$ is a lower bound of the set. $c$ has to be a boundary point of $A$ (and $B$), because

     - every open ball centered at $c$ must intersect $A$ (if one did not,it would contradict the definition of $c$ since we could find elements of the set smaller than $c$)

     - every open ball centered at $c$ must also intersect $B$ by definition of infimum (if one did not, we could find a greater lower bound)

    But $A$ and $B$ are open, and so do not contain boundary points. But they also cover $I$, so one of them must contain $c$. This is a contradiction.

3. Conversely, any connected subset $S$ of $\mathbb{R}$ must be an interval. We again neglect the case of $S$ with less than two points. If $S$ is connected and contains $a, b$ with $a < b$ and is missing some $x$ with $a < x < b$, then $(- \infty, x) \cap I$ and $(x, \infty) \cap I$ are together a disconnection of $I$.
