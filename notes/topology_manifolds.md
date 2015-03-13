1. A topological space $X$ is said to be **locally Euclidean of dimension $n$** if every $x \in X$ has a neighborhood $U$ that is homeomorphic to an open subset of $\mathbb{R}^n$.

2. A space $X$ is locally Euclidean of dimension $n$ iff every point in $X$ has a neighborhood homeomorphic to (an open ball in | all of) $\mathbb{R}^n$. The notes on the topology of the reals establish that any two open balls are homeomorphic as well as that any open ball is isomorphic to all of $\mathbb{R}^n$. Also, clearly if a space has every point with a neighborhood homeomorphic to an open ball in $\mathbb{R}^n$, it is locally Euclidean. So it suffices to prove that any locally Euclidean space has each point with a neighborhood homeomorphic to open balls as well.

    So if $X$ is locally Euclidean of dimension $n$, for each $x \in X$, there is some neighborhood $U$ of $x$ such that some homeomorphism $f: U \to f(U)$ exists, where $f(U)$ is open. Now there must be some open ball $B$ centered at $f(x)$ and contained in $f(U)$ because $f(U)$ is open, and its pre-image $f^{pre}(B)$ is a neighborhood of $x$ since $f$ is continuous. So the restriction of $f$ to $f^{pre}(B) \to B$ is again a homeomorphism

3. A **topological manifold of dimension $n$** (according to Lee) is a second-countable, Hausdorff space that is locally Euclidean of dimension $n$.

4. The first example of a topological manifold of dimension $n$ is $\mathbb{R}^n$ itself: elsewhere in the notes it is proved that $\mathbb{R}^n$ is second-countable, it is certainly Hausdorff (being a metric space), and it is homeomorphic to itself.
