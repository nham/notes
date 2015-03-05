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

6. Some facts about countability stated without proof (for now):

     - the finite product of countable sets is countable
     - countable union of countable sets is countable


7. $(A - B) \cap C = A \cap C - B \cap C$, because the left side says "in $A$, not in $B$, and in $C$" and the right side says "in $A and $C$, but not in $B$ and $C$", are the same.


8. I managed to study math for years without realizing the following: given any binary relation $R$ on $X$, the intersection of all equivalence relations containing $R$ is an equivalence relation. It's actually trivial to verify, so the proof is omitted here. Think about it.

    But this allows you to **generate** an equivalence relation from any binary relation $R$ on a set. The generated eqrel is the smallest eqrel containing $R$.


9. For any function $f: X \to Y$, $U \subseteq X$ is said to be **saturated with respect to $f$** if $U = f^{pre}(f(U)$. This means that the only points that $f$ maps into $f(U)$ are points in $U$.

    A set $U$ is saturated w.r.t. $f$ iff $U$ is a union of fibers. *Proof:* $U$ being saturated clearly implies that it's a union of the fibers of points in $f(U)$. Conversely, if $U$ is not saturated, there's at least one point $x \notin U$ such that $f(x) \in f(U)$, so the fiber of $f(x)$ is not contained in $U$, proving $U$ is not a union of fibers.
