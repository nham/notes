6. Can we extend the Bolzano-Weierstrass theorem to $\mathbb{R}^n$? The answer turns out to be yes! See the real inner product space notes and metric space notes for full details, but we have that $(x_n) \to c$ \in $\mathbb{R}^n$ iff each $(x_n^i) \to c_i$ in \mathbb{R}$.

    So if $(x_n)$ is bounded in $\mathbb{R}^n$, then it is contained in some open box in $\mathbb{R}^n$ (by topological equivalence of Euclidean and sup norms), so the sequence $(x_n^1)$ is bounded in $\mathbb{R}$ and hence has some convergent subsequence. If we take this subsequence of the original $(x_n)$, we now have a subsequence of $(x_n)$ whose first component-sequence converges to some $c_1$. Repeat the procedure with each of the other components. The result is a subsequence for which each component sequence converges in $\mathbb{R}$, so the whole sequence converges in $\mathbb{R}^n$.

10. An **infinite series** is when for some real sequence $(x_n)$, the limit

    $$\lim_{n \to \infty} \sum_1^n x_k$$

    exists. In this case the series is said to **converge** and the limit of the series is denoted $\sum_1^{\infty} x_k$. The sequence $(S_n)$ for $S_n := \sum_1^n x_k$ is the **sequence of partial sums** for the series.

11. The **Cauchy criterion** for infinite series says that an infinite series $\sum_1^{\infty} x_k$ converges iff for every $\epsilon$ there's an $N$ such that for all $m \geq n \geq N$ we have

    $$| \sum_n^m x_k | < \epsilon$.

    This is just an application of the fact that a sequence in $\mathbb{R}$ converges iff it is Cauchy to the sequences of partial sums.

    A way of re-phrasing this: an infinite series converges iff for every $\epsilon$ there's a tail sequence such that by starting partial sums at any point in the tail, the absolute value of any partial sum is strictly bounded above by $\epsilon$.

12. One corollary of the Cauchy criterion for series is that if an infinite series converges, we must have for all $\epsilon > 0$, some $N$ such that $|a_n| < \epsilon$ for all $n \geq N$. Equivalently,

    $$lim_{n \to \infty} x_n = 0$$

    is a necessary condition for $\sum_1^{\infty} x_n$ to converge.

13. It is not sufficient, however. The famous example we use here is that of the harmonic series, $\sum_1^{\infty} \frac{1}{n}$. This series diverges despite $\lim_{n \to \infty} \frac{1}{n} = 0$.

    To see this, note that

    $$\frac{1}{3} + \frac{1}{4} > 2 * \frac{1}{4} = \frac{1}{2}$$

    Similarly,

    $$\frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} > 4 * \frac{1}{8} = \frac{1}{2}$$

    In general,

    $$\sum_{j = 2^{k-1} + 1}^{2^k} \frac{1}{j} > 2^{k-1} * \frac{1}{2^k} = \frac{1}{2}$$

    But if $S_n$ is the $n$-partial sum, this means that $S_4 > S_2 + \frac{1}{2}$, $S_8 > S_4 + \frac{1}{2}$, and so on, so the sequence of partial sums could not be Cauchy (the difference between a a power-of-two term and the next biggest power-of-two term will always exceed $1/2$).


14. A convergent series $\sum_1^{\infty} x_k$ is **absolutely convergent** if $\sum_1^{\infty} |x_k|$ converges, and **conditionally convergent** otherwise.

15. The significance of absolutely convergent series, it seems to me, is that they are the proper notion of "infinite addition" of numbers. For finite addition, due to associativity and commutativity, any rearrangement of the numbers results in the same sum. So for some construction to be an infinite addition, one would (perhaps naively) expect that any rearrangement of the terms would result in the same sum.

    By the Riemann rearrangement theorem, however, it is not true for convergent infinite series in general: conditionally convergent series can be arranged to converge to any finite or infinite limit, or to diverge. The proof of that theorem is omitted here for now (TODO), but we will prove...

16. Any rearrangement of an absolutely convergent series converges to the same limit. (To be clear, we say $\sum_1^{\infty} b_k$ is a rearrangement of $\sum_1^{\infty} a_k$ when there's a bijection $f: \mathbb{N} \to \mathbb{N}$ such that $b_{f(k)} = a_k$ for all $k$.) Let $\sum_1^{\infty} a_n$ be a series converging to $A$, and let $\sum_1^{\infty} b_n$ be a rearrangement, with bijection $f$ such that $b_{f(k)} = a_k$ for all $k$.

    Also, let $A_n$ and $B_n$ be the $n$-partial sum of $(a_n)$ and $(b_n)$, respectively. The idea is, for every $\epsilon$, to find an $M$ such that for all $m \geq M$, $|B_m - A| < \epsilon$. We will (as usual) use the triangle inequality. We can clearly make $|A_n - A|$ as small as we like. Specifically, we can find an $N_1$ such that for all $n \geq N_1$, $|A_n - A| < \epsilon/2$. Can we find certain $m$ and $n$ such that $|B_m - A_n|$ gets arbitrarily small as well?

    By hypothesis, $\sum_1^{\infty} a_k$ is absolutely convergent, so there's an $N_2$ such that for all $m \geq n \geq N_2$, $\sum_n^m |a_k| < \epsilon/2$.

    Consider defining $N := \max{N_1, N_2}$. One idea here is to define $M := \max(f(i) : 1 \leq i \leq N)$, so that $B_M$ contains every term of $A_N$, and that for all $m \geq M$, $|B_m - A_N|$ is less than or equal to (by the triangle inequality) some finite sum of absolute values of terms of $(a_n)$. This means it is less than or equal to some contiguous some of absolute values of terms of $(a_n)$, where the "lower index" comes after $N+1$. But due to how we defined $N$, this sum is strictly less than $\epsilon/2$.

    We have just proven that for any $m \geq M$ $|B_m - A| < \epsilon$. So the rearrangement $\sum_1^{\infty} b_n$ converges to $A$ as well.


----
TODO: these things need to be reorganized

2. A **geometric series** is something of the form $$\sum_0^{\infty} x^k$$ for $0 \leq x < 1$. (Actually it probably works for $-1 < x < 0$ as well, but I don't need them for defining $e$). Each series of this form converges. Clearly this is true for $x = 0$. For $x \neq 0$, the sequence of partial sums:

    $$s_n := \sum_0^n x^k = \frac{1 - x^{n+1}}{1-x}$$

    is true using that one weird trick. The sequence converges since, letting $C := \frac{1}{1-x}$, we have $C - s_n = \frac{x^{n+1}}{1-x} > 0$ for all $n$, meaning $(s_n)$ is monotone increasing and bounded above by $C$. $C$ is also the limit since $(C - s_n) \to 0$ as $n \to \infty$ (owing to $x^{n+1} < x^n$ for all $n$)



5. Big O notation: if $f$ and $g$ are functions, we say $f \sim O(g)$ at $a \in dom f$ (pronounced "$f$ is Big O of $g$ near $a$") if there is a neighborhood $N$ of $a$ and a positive $C$ such that

    $$|f(x)| \leq C |g(x)|$$

    whenever $x \in N$. What is a neighborhood, you ask? Well, if $a$ is a real number, then it's just some open ball centered at $a$. If $a = \infty$, then it is the collection of points greater than some $x_0 \in \mathbb{R}$.

6. Big O is kinda counter-intuitive. $f(x) = x$ and $g(x) = 10^9 x$ are Big O of each other near $\infty$, for example. Also, $f(x) = x$ and $g(x) = -10^9 x$ are Big O of each other near $\infty$. Another example: $f(x) = 1$ is Big O of $g(x) = 2^x$ because $1 \leq 2^x$ for all $x > 0$ The converse is not true, however.

    If $f \sim O(g)$ at $a$ and $g(x)$ is nonzero in some neighborhood of $a$, then the Big O condition can be rewritten

    $$|\frac{f(x)}{g(x)}| \leq C$$

    for all $x$ in some neighborhood. So the ratio of the functions' output is bounded by some constant. It's not that it *is* constant, it's that it's *no more than constant*.

