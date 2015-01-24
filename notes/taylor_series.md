
1. For any metric spaces $X$ and $Y$, a sequence $(f_n)$ of functions $f_n: X \to Y$ is said to **converge pointwise** to $g: X \to Y$ if each sequence $(f_n(x))$ for $x \in X$ converges to $g(x)$. Think of it like slicing the functions in the sequence by input value. If each sliced sequence converges to each value of $g$, then $(f_n)$ converges pointwise to $g$.

    A sequence $(f_n)$ is alternatively said to **converge uniformly** to $g: X \to Y$ if $\forall \epsilon > 0$ there is an $N \in \mathbb{N}$ such that $\sup \{d_Y(f_n(x), g(x)) : x \in X\} < \epsilon$ for all $n \geq N$. The value $\sup \{d_Y(f_n(x), g(x)) : x \in X\}$ can be thought of as the max distance between outputs of $f_n$ and $g$ across all inputs.

    In fact we can define $U[f, g] := \sup \{d_Y(f(x), g(x)) : x \in X\}$ for all $f, g: X \to Y$. Note that this is not quite a metric, since $U[f, g]$ might not be finite. Still, we can reformulate our definition above using the idea behind Cauchy sequences: $(f_n)$ converges uniformly to $g$ iff for all $\epsilon > 0$ there is an $N \in \mathbb{N}$ such that $U[f_n, f_m] < \epsilon$ for all $m, n \geq N$.
