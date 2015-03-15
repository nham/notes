1. A sufficient (but not necessary) condition for ensuring uniqueness of limits is the **Hausdorff** property, which says that any two distinct points in a topological space have disjoint neighborhoods. Any space with this property is called a **Hausdorff space**. This ensures uniqueness of limits since two tail sequences of one sequence could not be contained in two disjoint sets (the smaller of the tail sequences would have to be contained in two disjoint sets, which is crazy talk).

2. TODO: An example of a non-Hausdorff space where limits are unique.

3. Another separation axiom that has come up: A space is ``T_1`` if for any pair of distinct points ``a`` and ``b``, there are neighborhoods ``U`` and ``V`` of ``a`` and ``b``, respectively, such that ``U`` doesn't contain ``b`` and ``V`` doesn't contain ``a``. Clearly Hausdorff spaces are ``T_1``, since they actually impose a stronger condition: that the neighborhoods are *disjoint*.

4. A space ``X`` is ``T_1`` iff singleton sets are closed. If ``T_1``, for any ``x`` and any ``y \neq x``, there is a neighborhood ``U_y`` of ``y`` that does not contain ``x`` by the ``T_1`` property, so the union of them all is ``X - x`` and is open since it is a union of open sets. (Alternate proof: if ``\{x\}`` is not closed, there is some ``a \neq x`` and every neighborhood of ``a`` contains ``x``, contradicting ``T_1``). Conversely, if all singletons are closed, then for ``x \neq y``, ``X - x`` is a neighborhood of ``y`` and ``X - y`` is a neighborhood of ``x``, and these mutually exclude each other.

5. ``T_1`` spaces do not necessarily have the unique limits property. TODO: example. Finite complement topology on ``\mathbb{N}``?

6. Random fact that I'm sticking here: In a ``T_1`` space, if ``a`` is a limit point of some subset ``S``, then for any neighborhood ``U`` of ``a`` there must be infinitely many points distinct from ``a`` that are in ``U \cap S``, because if there are only finitely many, we can find a neighborhood of ``a`` that does not intersect ``S - a``, contradicting that it's a limit point.
