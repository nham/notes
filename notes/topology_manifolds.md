1. A topological space $X$ is said to be **locally Euclidean of dimension $n$** if every $x \in X$ has a neighborhood $U$ that is homeomorphic to an open subset of $\mathbb{R}^n$. A pair $(U, \phi: U \to V)$ where $\phi$ is a homeomorphism and $V$ is open in $\mathbb{R}^n$ is called a **coordinate chart** or just **chart** on $X$. The set $U$ is called the **coordinate domain**. One way of restating the definition of "locally Euclidean of dimension $n$" is saying each point is contained in the domain of some coordinate chart. If $(U, \phi)$ is a chart and $\phi(p) = 0$, we say that the chart is **centered at $p$**. For any chart $(U, \phi)$ and any $p \in U$, we can make a chart on $U$ that has $p$ as its center by translating $\phi(U)$.

2. A space $X$ is locally Euclidean of dimension $n$ iff every point in $X$ has a neighborhood homeomorphic to (an open ball in | all of) $\mathbb{R}^n$. The notes on the topology of the reals establish that any two open balls are homeomorphic as well as that any open ball is isomorphic to all of $\mathbb{R}^n$. Also, clearly if a space has every point with a neighborhood homeomorphic to an open ball in $\mathbb{R}^n$, it is locally Euclidean. So it suffices to prove that any locally Euclidean space has each point with a neighborhood homeomorphic to open balls as well.

    So if $X$ is locally Euclidean of dimension $n$, for each $x \in X$, there is some neighborhood $U$ of $x$ such that some homeomorphism $f: U \to f(U)$ exists, where $f(U)$ is open. Now there must be some open ball $B$ centered at $f(x)$ and contained in $f(U)$ because $f(U)$ is open, and its pre-image $f^{pre}(B)$ is a neighborhood of $x$ since $f$ is continuous. So the restriction of $f$ to $f^{pre}(B) \to B$ is again a homeomorphism

3. A **topological manifold of dimension $n$** (according to Lee) is a second-countable, Hausdorff space that is locally Euclidean of dimension $n$.

4. The first example of a topological manifold of dimension $n$ is $\mathbb{R}^n$ itself: elsewhere in the notes it is proved that $\mathbb{R}^n$ is second-countable, it is certainly Hausdorff (being a metric space), and it is homeomorphic to itself. More generally, any open subset of $\mathbb{R}^n$ is a topological manifold of dimension $n$, since subspaces of Hausdorff/second-countable spaces are Hausdorff/second-countable.

5. If $U$ is an open subset of $\mathbb{R}^n$ and $f: U \to \mathbb{R}^k$ is a continuous map, then the graph of $f$, denoted

    $$\Gamma(f) := \{(x, y) \in \mathbb{R}^n \times \mathbb{R}^k : x \in U, y = f(x)\}$$

    is a topological manifold of dimension $n$ when considered to have the subspace topology relative to $\mathbb{R}^n \times \mathbb{R}^k$. (Defining $\Gamma(f)$ is really only done for emphasis, since set-theoretically a function is defined to *be* it's graph set). It is second countable and Hausdorff because the finite product of second-countable Hausdorff spaces is second-countable Hausdorff, and because $\Gamma(f)$ is a subspace of a second-countable Hausdorff space.

    To prove that $\Gamma(f)$ is locally Euclidean of dimension $n$, note that $\phi: \Gamma(f) \to U$ defined by $\phi(x, y) := x$ is a restriction of the projection $\mathbb{R}^n \times \mathbb{R}^k \to \mathbb{R}^n$, so $\phi$ is continuous. It is also bijective since it has an inverse: $\phi^{-1}(x) := (x, f(x))$.
