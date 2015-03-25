
## Lebesgue outer measure on ``\mathbb{R}``

For any countable collection ``I`` of open intervals (of the form ``(a, b)``) in ``\mathbb{R}``, we can define the **amount** of ``I`` to be

```math
    |I| := \sum_k (b_k - a_k)
```

Now, for all ``A \subseteq \mathbb{R}``, we define ``\lambda^{\ast}(A)``, the **Lebesgue outer measure on ``A``**, by

```math
    \lambda^{\ast}(A) := \inf{ |I| : I \text{ is a countable collection of open intervals and covers } A}
```

``\lambda^{\ast}`` is a function from the power set of ``\mathbb{R}`` into ``[0, \infty]``.

### ``\lambda^{\ast}`` actually is an outer measure

To verify that ``\lambda^{\ast}`` is an outer measure, we must prove that ``\lambda^{\ast}(\emptyset) = 0`` and that ``\lambda^{\ast}`` is monotone and has countable sub-additivity.

First, ``\lambda^{\ast}(\emptyset) = 0`` is true because the empty interval is a countable cover (alternatively, any collection of a single open interval is a cover, and we can make the intervals arbitrarily small). Also, it is monotone since if ``A \subseteq B``, any cover for ``B`` is a cover for ``A``.

You can see it is countably sub-additive as follows: let ``\{A_k\}`` be some countable collection of subsets of ``\mathbb{R}``. For every ``\epsilon > 0``, for every ``k`` pick a cover ``I_k`` of ``A_k`` such that

```math
    |I_k| < \lambda^{\ast}(A_k) + \epsilon / 2^k
```

Then  ``\bigcup_k I_k`` is a countable cover by open intervals of ``\bigcup_k A_k``, and

```math
    |\bigcup_k I_k| = \sum_k |I_k| < \sum_k (\lambda^{\ast}(A_k) + \epsilon / 2^k) = (\sum_k \lambda^{\ast}(A_k)) + \epsilon
```

So ``\lambda^{\ast}(\bigcup_k A_k) < \sum_k \lambda^{\ast}(A_k) + \epsilon`` for all ``\epsilon``, which establishes countable sub-additivity.

### More Lebesgue outer measure on ``\mathbb{R}``

The Lebesgue outer measure assigns any interval ``[a, b]`` its length ``b - a``. It can be proved that ``\lambda^{\ast}([a, b]) \leq b - a`` since ``(a - 1/n, b + 1/n)`` is a cover of ``[a, b]`` whose total amount is ``b - a + 2/n``. In other words, there are covers of ``[a, b]`` that get arbitrarily close to ``b - a`` So ``\lambda^{\ast}([a, b]) \leq b - a`` (otherwise you could find a cover of ``[a, b]`` whose amount was less than ``\lambda^{\ast}([a, b])``).

For the reverse direction: ``[a, b]`` is compact, so any countable cover ``I`` of ``[a, b]`` by open intervals has a finite subcover, which means there is an `n` such that ``[a, b] \subseteq \bigcup_1^n (a_i, b_i)``. So ``b - a \leq \sum_1^n b_i - a_i`` (I think this is because we must have ``(a_{j_1}, b_{j_1}), \ldots, (a_{j_k}, b_{j_k})`` such that ``a_{j_{i+1}} < b_{j_i}`` for all ``j`` and ``a_{j_1} < a, b < b_{j_k}``). This proves that ``b - a \leq |I|``. So ``b - a`` is a lower bound of countable covers of ``[a, b]``, which establishes the other inequality.

### Lebesgue outer measure on ``\mathbb{R}^d``

To define the Lebesgue outer measure on ``\mathbb{R}^d``, define the **volume** of any open box ``I = \prod_1^d I_k`` to be ``\text{vol}(I) = \prod_1^d |I_k|``. Then the **amount** of any countable collection ``C`` of open boxes is defined to be

```math
    |I| := \sum_{k=1}^{\infty} \text{vol}(C_k)
```

And we define

```math
    \lambda^{\ast}(A) := \inf{ |I| : I \text{ is a countable collection of open boxes and covers } A}
```

### ``\lambda^{\ast}`` is actually an outer measure on ``\mathbb{R}^d``

The proof is virtually identical to the case for ``\mathbb{R}``.


## Lebesgue-measurable sets
Sets that are measurable w.r.t. the Lebesgue outer measure are called **Lebesgue measurable**.

