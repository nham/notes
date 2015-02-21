1. A group $G$ is a set equipped with a binary product $\cdot$ that obeys these properties:

     - associativity: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c$
     - identity: there is some group element $e$ such that $a \cdot e = e \cdot a = a$ for all $a$
     - inverses: every group element $g$ has some other element $h$ such that $g \cdot h = h \cdot g = e$

    By associativity we don't need to worry about parentheses ($(a \cdot b) \cdot c = a \cdot b \cdot c$). Also, the "$\cdot$" is often omitted, so we just write $abc$.

2. It is simple to prove that the identity element is unique, and that each element's inverse is also unique. Another crucial fact is that for all group elements $a$ and $b$, there is a unique $x$ such that $ax = b$ and a unique $y$ such that $ya = b$ (namely, $x = a^{-1} b$ and $y = b a^{-1}$), which is sometimes called the **unique solvability** property. One more fact is that $(ab)^{-1} = b^{-1} a^{-1}$ for all $a, b \in G$.

3. The group product isn't necessarily commutative. When it is, the group is called **commutative** or **abelian**. When this happens, typically "additive notation" for the group operation is used: $g + h$ instead of $g \cdot h$.

3. A **subgroup** is any subset $S$ of a group $G$ that is a group when the group product is restricted to $S$. It is sufficient to prove that $S$ 1) is closed under the product, and 2) contains all the inverses for each element. (An equivalent characterization of the subgroup (the "categorical" characterization) is that the inclusion map $S \to G$ is a homomorphism, which we define below)

4. For any subgroup $H$ we can define **left** and **right cosets**, defined by
    
    $$gH := \{gh : h \in H\}$$

    $$Hg := \{hg : h \in H\}$$

5. Each coset is bijective with the subgroup that generates it. The proof for left cosets is as follows: the map $\phi_g: x \mapsto gx$ is a bijection on $G$ due to unique solvability (alternatively, a bijection because $\phi_{g^{-1}}$ is its inverse). But $\phi_g(H) = gH$, so restricting $\phi_g: G \to G$ to $H \to gH$ is still a bijection. This proof is obviously adaptable to right cosets.

6. (This point is mostly technical. I'm introducing it to easily prove things below.) More generally we can define two-sided cosets $aHb := \{ahb : h \in H\}$. This is more general because the left and right cosets can be seen as two-sided cosets where one side is the identity element. We can also more generally define "left and right multiplications" (not sure what to call this) of two-sided cosets by

    $$g(aHb) := \{ gz : z \in aHb\}$$

    $$(aHb)g := \{ zg : z \in aHb\}$$

    It can be proved that $g(aHb) = (ga)Hb$, $(aHb)g = aH(bg), and that $aHb = a(Hb) = (aH)b$ for all $a, b, g, H$. Also, if $x, y \in H$, then $H = xHy$.

7. All the left (right) cosets of a subgroup are disjoint, which means the left (right) cosets of any subgroup partition the group into bijective equivalence classes. The proof: $aH$ and $bH$ are distinct left cosets that share an element $g$, we must have $g = ax = by$ for some $x, y \in H$. This proves that $a = b y x^{-1}$. But this implies $aH = b (y x^{-1} H) = b H$, contradicting that they're distinct.

8. A subgroup $H$ of $G$ is said to be **normal** (think of it as "self-conjugate") when $gH = Hg$ for all $g$. Equivalently, when $gHg^{-1} = H$. The major point of normal subgroups is they allow you to define the **quotient group** $G/H$, which is a group whose elements are cosets of $H$. The group operation is defined by

    $$aH \cdot bH = (ab)H$$

    which is well-defined since if $aH = xH$ and $bH = yH$, then $abH = aHb = xHb = xbH = xyH$.

9. Another way of thinking about normal subgroups is that they are exactly the subgroups that ensure that left and right cosets coincide, meaning we can just talk about "cosets" instead.

10. A **group homomorphism** is a map $\phi: G \to H$ between two groups $G$ and $H$ such that $\phi(xy) = \phi(x) \phi(y)$. This defining condition gives us a few desirable properties:

     - homomorphisms map identity elements to identity elements
     - homomorphisms map the inverse of any $g$ to the inverse of $\phi(g)$.

    The image of any group homomorphism $\phi: G \to H$ is a subgroup of $H$ since it is closed under the product by definition of homomorphism and closed under inverses by the second point above.

    A bijective homomorphism is called a **group isomorphism**.

11. The **kernel** of a homomorphism $\phi: G \to H$ is the set of elements that $\phi$ maps to the identity of $H$. This is a subgroup of $G$. What's more, it's a *normal subgroup*. We prove this by proving that 

    $$g (ker \phi) = \phi^{pre}(\phi(g)) = (ker \phi) g$$

    where $\phi^{pre}(\phi(g))$ is the fiber of $\phi(g)$. We have $\phi(gx) = \phi(g)$ for all $x \in ker \phi$, and if $\phi(a) = \phi(g)$, then $g^{-1} a$ is in the kernel too, so $a \in g ker \phi$. The same proof holds for the other coset, so $ker \phi$ is normal.

12. The fundamental group homomorphism theorem (what we've been working towards this whole time) is that any group homomorphism $\phi: G \to H$ gives an isomorphism between the image of $\phi$ and the quotient group $G / ker \phi$. This is actually proved from the last proposition, where we proved that the cosets of the kernel were exactly the fibers of the homomorphism.

13. The **symmetric group** on a set $X$ is the collection of all bijections $X \to X$. We denote this $Sym X$.

14. A **group action** of a group $G$ on some set $X$ is a homomorphism $G \to Sym X$.

15. If $G$ is a group and $\phi$ a group action on $X$, the **stabilizer subgroup** or **isotropy subgroup** of $x \in X$ is the collection of group elements whose maps fix $x$. It's a subgroup because if $g, h$'s maps fix $x$, their composition, which is $gh$'s map, does too, and also $g^{-1}$'s map, which is the inverse of $g$'s map, also fixes $x$.
