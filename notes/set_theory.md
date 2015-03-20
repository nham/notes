1. Preimages perserve arbitrary union and arbitrary intersection. Intersection is used in the proof of the characteristic property holding for the product topology. The union fact is used in proving that it suffices to show inverse images of basis elements are open to establish that a map is continuous.

    There is an asymmetry when considering the case of images. The image of a union is the union of images, but not so for intersections. Consider

    $$f: \{0, 1} \to \{1\}$$

    (which is constant by necessity) and let $A = \{0\}$, $B = \{1\}$. Then $A \cap B = \emptyset$ and $f(A \cap B) = \emptyset$, but $f(A) \cap f(B) = \{1\}$.

2. $f(f^{pre}(A))$ is the image of $f^{pre}(A)$ under $f$, which has

    $$f(f^{pre}(A) \subseteq A$$

    (not every element of $A$ may be mapped to by $f$).

    $f^{pre}(f(A))$ is all the points that $f$ maps to $f(A)$, which in general is a superset of $A$ (there may be points outside of $A$ that get mapped into $f(A)$)

    Surjectivity implies equality in the first case, and injectivity implies it in the second.

3. If $f: X \to Y$ is a bijection then $f(U) = (f^{-1})^{pre}(U)$. Since by (2) we have that $f^{pre}(f(U)) = U$ and $f(f^{pre}(V)) = V$ for all $U \subseteq X$ and $V \subseteq Y$, we have that

    $$f^{pre}(f(U)) = f^{-1}((f^{-1})^{pre}(U)$$

    for all $U \subseteq X$ whenver $f$ is bijective.

    This comes up in the proof that $f: X \to Y$ is a homeomorphism iff $f$ is bijective and $U$ is open in $Y$ iff $f^{pre}(U)$ open in $X$ for all $U \subseteq Y$.

4. The pre-image of a complement is the complement of the pre-image: For any $f: X \to Y$ and $B \subseteq Y$, $x \notin f^{pre}(B)$ iff $f(x) \notin B$. So $f^{pre}(Y - B) = X - f^{pre}(B)$.


5. The product of arbitrary intersections w.r.t. some common index set is the intersection of products. This fact is needed to prove that the collection of products of open sets is a basis. The same is *not* true for unions though. Consider the case of singletons, $(a \times b) \cup (c \times d) = \{(a, b), (c, d)\} \neq (a \cup b) \times (c \cup d)$. The latter contains $(b, c)$, for example. The best we can do here is (probably?):

    $$(\bigcup_i (S_i \times T) = (\bigcup_i S_i) \times T$$

6. $(A - B) \cap C = A \cap C - B \cap C$, because the left side says "in $A$, not in $B$, and in $C$" and the right side says "in $A and $C$, but not in $B$ and $C$", are the same.


7. I managed to study math for years without realizing the following: given any binary relation $R$ on $X$, the intersection of all equivalence relations containing $R$ is an equivalence relation. It's actually trivial to verify, so the proof is omitted here. Think about it.

    But this allows you to **generate** an equivalence relation from any binary relation $R$ on a set. The generated eqrel is the smallest eqrel containing $R$.


8. A set $X$ is **countable** if it is bijective with a subset of $\mathbb{N}$. You might also say countable = finite or countably infinite.

9. The **axiom of countable choice** states that for any $X$ and any surjective $f: X \to \mathbb{N}$, there is a $g: \mathbb{N} \to X$ such that $f \circ g$ is the identity. (In other words, $g$ is a section for $f$. In other other words, $g$ is a function that assigns to each $n$ some element of its fiber under $f$).

10. Equivalent characterizations:

    - a set $X$ is countable
    - there's an injective map $X \to \mathbb{N}$.
    - there's a surjective map $\mathbb{N} \to X$.

    $X$ countable clearly implies both. If $f: X \to \mathbb{N}$ is injective, just restrict $f$ (on the codomain side) to it's image to obtain a bijection with a subset of $\mathbb{N}$. If $g: \mathbb{N} \to X$ is surjective, pick one element from each fiber of $g$ (axiom of countable choice), collect them all in a set $S \subseteq \mathbb{N}$, and now we have a bijection by restricting $g$ to $S$.

11. The integers $\mathbb{Z}$ are countable: the function $f: \mathbb{Z} \to \mathbb{N}$ defined by $f(0) = 0$, $f(n) = 2n - 1$ for positive $n$ and $f(m) = -2m$ for negative $m$ is a bijection (the image of the positive integers is the odd naturals, the image of the negative integers is the positive even naturals).

12. The rationals $\mathbb{Q}$ are countable. Without getting too bogged down with technicalities: we know $\mathbb{Z}$ is countable, so there's an injective $f: \mathbb{Z} \to \mathbb{N}$. So we can prove $\mathbb{Z} \times \mathbb{Z}$ is countable by definition of the function $g(i, j) := 2^{f(i)} 3^{f(j)}. This is injective by basic number theory: integers have unique prime factorizations, so if $g(i, j) = g(a, b)$, then $f(i) = f(a)$ and $f(j) = f(b)$, which means $(i, j) = (a, b)$ by injectivity of $f$.

    Now we just show there's an injective map $\mathbb{Q} \to \mathbb{Z}^2$. For any rational $q$, just pick one of the pairs of integers $(m, n)$ such that $m/n = q$. This is injective by definition. Now compose this with the above map to get an injective map $\mathbb{Q} \to \mathbb{N}$.

    We just need an injection $\mathbb{Q} \to \mathbb{N}$. First label the rational $0$ with integer $0$. Now label rationals formed by pairs of positive integers odd naturals, so $1/1, 1/2, 2/1, 1/3, 2/2, 3/1, \ldots$ with odds $1, 3, 5, 7, 9, 11, \ldots$, and similarly label $-1/1, -1/2, -2/1, -1/3, -2/2, -3/1, \ldots$ with $2, 4, 6, 8, 10, 12, \ldots$. The injective map can be constructed by, for all $q \in \mathbb{Q}$, reduce $q$ to lowest terms and map it to the corresponding label.


13. Some facts about countability stated without proof (for now):

     - the finite product of countable sets is countable
     - countable union of countable sets is countable
