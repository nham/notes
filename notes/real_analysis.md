
1. The monotone convergence theorem says that every monotonically non-decreasing (non-increasing) sequence that is bounded above (below) converges to the least upper bound (greatest lower bound) of the set of terms. If we start out axiomatizing $\mathbb{R}$ with the least upper bound property, this can be proved as follows: the least upper bound $C$ of the term set exists, so we can find terms arbitrarily close to $C$. But the sequence is monotone, so once we find any term within an $\epsilon$, all other terms are as well. So it converges. The same proof works for non-increasing sequences bounded below.

2. The "peak point lemma" says that any sequence in $\mathbb{R}$ has a monotone subsequence. For any sequence $(x_n)$ let us say that $x_m$ is a "peak term" if it acts as an upper bound for the terms that follow ($x_m \geq x_n$ for all $n > m$). Then any sequence has either infinitely many or finitely many peak terms.

    If there are infinitely many, we can form a subsequence out of them that must be monotone non-increasing. If there are finitely many of them. every term after the last peak term is strictly dominated by some term that comes later (since they all must fail to be peak terms), so we can find a monotone increasing subsequence.

3. When $(x_n)$ is bounded, the peak point lemma has an interesting consequence: we have a bounded, monotone subsequence, hence convergent subsequence by the monotone convergence theorem. In other words, we have just proved the **Bolzano-Weierstrass** theorem for $\mathbb{R}$: every bounded sequence has a convergent subsequence.

4. What's the point of Bolzano-Weierstrass? Seems like a weird thing to care about on the surface, but this has to do with sequential compactness. BW says that for every closed, bounded subset $A$ of $\mathbb{R}$, every sequence in $A$ has a convergent subsequence. But $A$ must also contain the limit of the convergent subsequence since it is closed. In other words, $A$, as a subspace of $\mathbb{R}$, is sequentially compact (every sequence has a convergent subsequence).

5. Even if you don't see the fuss about compactness of closed, bounded subsets of $\mathbb{R}$, here's one important corollary: $\mathb{R}$ is complete. The proof is as follows: Cauchy sequences are bounded, so they have a convergent subsequence, and Cauchy sequences with convergent subsequences are themselves convergent. So every Cauchy sequence converges. Magic.

6. Can we extend the Bolzano-Weierstrass theorem to $\mathbb{R}^n$? The answer turns out to be yes! See the real inner product space notes and metric space notes for full details, but we have that $(x_n) \to c$ \in $\mathbb{R}^n$ iff each $(x_n^i) \to c_i$ in \mathbb{R}$.

    So if $(x_n)$ is bounded in $\mathbb{R}^n$, then it is contained in some open box in $\mathbb{R}^n$ (by topological equivalence of Euclidean and sup norms), so the sequence $(x_n^1)$ is bounded in $\mathbb{R}$ and hence has some convergent subsequence. If we take this subsequence of the original $(x_n)$, we now have a subsequence of $(x_n)$ whose first component-sequence converges to some $c_1$. Repeat the procedure with each of the other components. The result is a subsequence for which each component sequence converges in $\mathbb{R}$, so the whole sequence converges in $\mathbb{R}^n$.

7. Sequence convergence in the extended reals is just like in the reals, except now $\pm \infty$ may appear in sequences, and they may also be a limit of sequences.

8. The **extended monotone convergence theorem** is that every monotone nondecreasing/nonincreasing sequence of extended reals is bounded above/below, and so converges, either to the supremum/infimum for a finite bound, or to $\pm \infty$.

9. The **order limit theorem** for sequences of extended reals says that if $(a_n)$ and $(b_n)$ are sequences of extended reals and $a_n \leq b_n$ for all $n \geq N$ for some $N$, if the sequences converge then $\lim_{n \to \infty} a_n \leq \lim_{n \to \infty} b_n$.

    The proof is simple: if not, the limit $A$ of $(a_n)$ is strictly greater than $B := \lim_{n \to \infty} b_n$, which means we can find a point $k$ after which all terms of $(a_n)$ are strictly greater than terms of $(b_n)$, which is contrary to assumption.

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

