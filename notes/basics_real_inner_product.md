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

7.
