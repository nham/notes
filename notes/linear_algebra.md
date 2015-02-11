1. A **vector space** is a pair $(V, \mathbb{F})$ where $V$ is an abelian group and $\mathbb{F}$ is a field, along with two operations $+$, called *vector addition* and $\cdot$, called *scalar multiplication*, which satisfy:

     - scalar multiplication distributes over both vector addition and field addition
     - the field multiplicative identity is an identity for scalar multiplication
     - scalar multiplication is associative: $a \cdot (b \cdot v) = (ab) \cdot v$

2. Basic facts that we state and don't bother to prove:

     - $c \cdot v = 0$ whenever $v$ is the zero vector or $c$ is the zero scalar
     - the converse too: if $c \cdot v = 0$ then we must have either $c = 0$ or $v = 0$
     - $-1 \cdot v = -v$ for all $v$
     - and of course, all the facts about abelian groups pertain to $V$.

3. A **coefficient system** for any collection $S \subseteq V$ of vectors with respect to some vector space $(V, \mathbb{F})$ is a pair $(S, \phi)$, where $\phi$ is a map $S \to \mathbb{F}$ (i.e. an assignment of scalars to every vector in the set). When the set $S$ is finite we say the coefficient system is finite. For every finite coefficient system $(S, \phi)$ of some finite collection $S$ of vectors, we can define their sum:

    $$\sum_{v \in S} \phi(v) \cdot v$$

    This is just the vector sum of each of the $\phi(v) \cdot v$'s. This is well-defined because addition is both commutative and associative, so parentheses and order don't matter, and because $S$ is finite. A vector $z$ is said to be a **linear combination** of a finite set $S$ when there is some coefficient system for $S$ that sums to $z$.

    The above is arguably overblown. The custom is to just label the vectors in $S$ with the numbers $1$ through $n = |S|$. A linear combination of $S$ is then the sum
    
    $$\sum_1^n a_i v_i$$

    Since we can only sum finite collections of vectors, we lose no generality here.

4. Let's call a coefficient system with no zero coefficients a *non-zero coefficient system*. (Needed because adding a vector with a zero coefficient does not change the sum.) A subset $G$ of $V$ is said to **generate** a vector space $V$ if every vector in $V$ is the sum of some non-zero coefficient system. A subset $I$ of $V$ is said to be **independent** in $V$ if every vector in $V$ is the sum of at most one non-zero coefficient system.

    Notice the duality in these statements. Generating set: for every vector there is at least one non-zero coefficient system that sums to it. Independent set: for every vector there is at most one non-zero coefficient system that sums to it.

    If a set is *not* independent, we say it is **dependent**.

    The **span** of a collection $S$ of vectors is all vectors that are linear combinations of (finite subsets of) vectors in $S$.

5. A convenient equivalent formulation of independent set is this: the only coefficient system that sums to the zero vector is the trivial coefficient system (all zeros). Also, a convenient equivalent formulation of dependent set is this: one vector in the set is in the span of the others. 

    Note that this latter fact easily implies that if $v \in S$ is dependent on the others, then removing $v$ from $S$ will not change the span (in any linear combination involving $v$, we can be replace $v$ by a linear combination of the remaining vectors). Proofs omitted here because they're boring, duh.

6. A **basis** for a $V$ is any set that is simultaneously generating and independent.

    There are two equivalent characterizations of bases. But first, more definitions! A **maximal independent set** is an independent set that becomes dependent when any other vector (not already in the set) is added to it. A **minimal generating set** is a generating set that fails to generate the space when you take any vector away. (So "maximal" and "minimal" are w.r.t. the poset of subsets under set inclusion)

    Then a set is a basis iff it is a maximal independent set iff it is a minimal generating set. First, assume that $B$ is a basis. It is independent by definition, and since it spans the set, adding any other element would make it linearly dependent (by the equivalent characterization of dependent sets in (5)), so $B$ must be maximal independent. Now, if $C$ is any maximal independent set, adding any element makes it dependent, which means every other element must be in the span, so it must also be generating. But no element in $C$ is in the span of the others by independence, so the removal of any element would make it fail to generate, meaning $C$ is also a minimal generating set. Finally, if $D$ is any minimal generating set, no element could be in the span of the others, otherwise we would be able to remove it without affecting the span.
