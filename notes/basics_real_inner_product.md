1. A **real orthogonal space** is a real vector space $V$ equipped with a symmetric, bilinear form $\phi: V^2 \to V$ called the **scalar product**. 

    Two vectors $v, w \in V$ are said to be **orthogonal** when $\phi(v, w) = 0$, and two subsets $A, B \subseteq V$ are said to be **mutually orthogonal** if every pair $(a, b) \in A \times B$ is orthogonal.

    We are usually interested in real orthogonal spaces where the scalar product is *positive-definite*: for all  $v \in V$, \phi(v, v) \geq 0$, and $\phi(w, w) = 0$ iff $w = 0$. Such a space is called a **real inner product space**, (alternatively, **Euclidean vector space**). We will denote the scalar product of a Euclidean vector space by $\cdot$.

2. Positive-definiteness of the inner product means you can define a **norm** on any real inner product space, which is any map $\psi: V \to \mathbb{R}$ satisfying

     - *positive-definite:* $\psi(v) \geq 0$ for all $v$ and $\psi(v) = 0$ iff $v = 0$
     - *homogeneous:* $\psi(av) = |a| \psi(v)$ for all $a \in \mathbb{R}$, $v \in V$
     - *triangle inequality:* $\psi(v + w) \leq \psi(v) + \psi(w)$ for all $v, w$

    It is straightforward to prove the first two work for any real inner product space, but the last one requires a bit of work...

3. Which we will omit here, unfortunately. One proof I have written elsewhere uses the Pythagorean property.

    **Pythagorean  property:** $|a + b|^2 = |a|^2 + |b|^2$ whenever $a, b$ are orthogonal members of a real inner product space. $\Box$

    With this one can prove:

    **Cauchy-Schwarz inequality:** In any real inner product space,
    
    $$|a \cdot b| \leq |a| |b|$$

    for all $a, b$. $\Box$

4. With the Cauchy-Schwarz inequality in hand, one can prove the triangle inequality for any real inner product space. It's actually quite simple:

    $$\begin{align}
      |x + y|^2 &= (x + y) \cdot (x + y) \\
                &= x \cdot x + y \cdot y + 2(x \cdot y) \\
                &\leq x \cdot x + y \cdot y + 2|x||y| \\
                &= (|x| + |y|)^2 \\
      \end{align}$$

5. The triangle inequality (along with the other properties of the norm) enables us to use the norm to define a metric on any normed vector space. If $| \cdot |$ is the norm, then we can define

    $$d(v, w) := |v - w|$$

    This satisfies all the metric axioms, as you can easily verify.

6. Before we said that two vectors could be orthogonal, or that two sets of vectors could be mutually orthogonal. Now we say that a single set of vectors is **orthogonal** if any two vectors in it are orthogonal (i.e. $v \cdot w = 0$ for all $v, w$). If all the vectors additionally have unit norm ($|v| = 1$), then the set is said to be **orthonormal**. Usually we talk about orthogonal and orthnormal bases for a vector space. 

    You can prove that any orthogonal collection of vectors is linearly independent.

7. Two norms are said to be **equivalent** if there are positive reals $C, D$, with $C \leq D$, such that $C \|v\|_1 \leq \|v\|_2 \leq D \|v\|_1$ for all $v$. This relation between norms on a given vector space is clearly reflexive and symmetric, and fairly easy to see that it's transitive. Equivalent norms induce the same topology since this condition implies that the induced metrics have nesting open balls (see metric space notes).

8. If $V$ and $W$ are normed vector spaces, a linear map $T: V \to W$ is **bounded** when there is a $C > 0$ such that $|Tx|_W \leq C |x|_V$ for all $x \in V$.

    Relatedly, the **operator norm** of a linear map $T$ is defined to be

    $$\inf \{ C > 0 : \forall x |Tx| \leq C |x|\}$$

    So when a linear operator is bounded, it has finite operator norm. If a linear operator is not bounded, then the set is empty, and the infimum of an empty set is customarily defined (using the extended reals) as $\infty$. That is, a linear operator's norm is finite iff it is bounded.

9. An interesting fact about linear operators between normed vector spaces is that they are bounded iff continuous. If $T: V \to W$ is a linear map between normed vector spaces, supposing $T$ is bounded we have for any $x \in V$, $|Tx - Ta| = |T(x - a)| \leq C |x - a|$. So whenever $a$ is within $C \epsilon$ of $x$, $Ta$ will be within $\epsilon of $Tx$, which proves continuity. Conversely, if $T$ is continuous it's certainly continuous at $0$. So we can find some $\delta > 0$ such that $|Tx| < 1$ for all $|x| < \delta$. We use this fact as a stepping stone to the final proof: if $v \neq 0$, we can define $z_v := \frac{\delta v}{2 |v|}$. Then $|z_v| = \delta/2$, so $|T z_v| < 1$. But this implies $|Tv| < \frac{2}{\delta} |v|$.

10. A corollary of (9) is that if norm $\phi$ is equivalent to norm $\psi$, then $\phi$ is bounded (hence continuous) w.r.t. $\psi$, and vice versa.
