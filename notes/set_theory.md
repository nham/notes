1. Preimages perserve arbitrary union and arbitrary intersection. Intersection is used in the proof of the characteristic property holding for the product topology. The union fact is used in proving that it suffices to show inverse images of basis elements are open to establish that a map is continuous.

2. $f(f^{pre}(A))$ is the image of $f^{pre}(A)$ under $f$, which has

    $$f(f^{pre}(A) \subseteq A$$

    (not every element of $A$ may be mapped to by $f$).

    $f^{pre}(f(A))$ is all the points that $f$ maps to $f(A)$, which in general is a superset of $A$ (there may be points outside of $A$ that get mapped into $f(A)$)

    Surjectivity implies equality in the first case, and injectivity implies it in the second.


3. The product of arbitrary intersections w.r.t. some common index set is the intersection of products. This fact is needed to prove that the collection of products of open sets is a basis. The same is *not* true for unions though. Consider the case of singletons, $(a \times b) \cup (c \times d) = \{(a, b), (c, d)\} \neq (a \cup b) \times (c \cup d)$. The latter contains $(b, c)$, for example. The best we can do here is (probably?):

    $$(\bigcup_i (S_i \times T) = (\bigcup_i S_i) \times T$$

4. Some facts about countability stated without proof (for now):

     - the finite product of countable sets is countable
     - countable union of countable sets is countable
