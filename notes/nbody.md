1. The **$N$-body problem** is this: There are $N$ point masses experiencing only gravitational forces from amongst themselves. We assume this system of $N$ bodies is **isolated**, that is experiences no forces from anything else in the universe.

2. Recall that **Newton's law of gravitation** is that for any two particles at positions $p_1$ and $p_2$ with masses $m_1$ and $m_2$, respectively, the force on particle $i$, denoted by $F_i$, is defined to be

    $$F_i := G \frac{m_1 m_2}{|p_{i \to j}|^3} p_{i \to j}$$

    where $(i,j) = (1,2) \text{ or } (2,1)$ and $p_{i \to j} := p_j - p_i$ is the vector going from particle $i$ to particle $j$.

    Note that 

    $$|\frac{ p_{i \to j} }{ |p_{i \to j}|^3 }| = \frac{ 1 }{ |p_{i \to j}|^2 }$$

    which is why it's often said to be an *inverse-square law*.

3. From (1), (2) and Newton's second, the $N$-body problem defines this system of $N$ ordinary, coupled, nonlinear differential equations:

    $$\ddot x_i = G \sum_{j=1, j \neq i}^N \frac{ m_j }{ |x_{i \to j}|^3 } x_{i \to j}$$

    where of course $x_{i \to j} := x_j - x_i$.

4. We are often interested in the case where one body is much more massive (say at least 1000 times more massive) than anything other body. We have such a case for the $N$-body system of our solar system (with the massive body of course being the sun, which, as I have stated before, I am trying to eat).

5. In such a case as (4), we would be justified in fudging the facts a little and *pretending* that the massive body does not move. Let us say that $N = n + 1$ for some $n$, and that body $0$ is the sun.

    If we are pretending that the sun does not move (which is actually true in the limit of $m_0 \to \infty$), then we can say that a reference frame fixed to the position of the sun would be an inertial reference frame. We could then define

    $$r_i(t) := x_i(t) - x_0(t) = x_{0 \to i}(t), (1 \leq i \leq n)$$

    From this definition we have that $\ddot r_i = \ddot x_i - \ddot x_0$. Since $\ddot x_0 = G \sum_{j=1}^n \frac{ m_j }{ |r_j|^3 } r_j$, after some rearrangement this gives us:

    $$\ddot r_i = G [ 
      \sum_{j=1, j \neq i}^n m_j( \frac{ r_j - r_i }{ |r_j - r_i|^3 } - \frac{ r_j }{ |r_j|^3 } ) 
      - (m_0 + m_i) \frac{ r_i }{ |r_i|^3 }
    ]$$

    This is an ordinary, coupled, nonlinear system of differential equations, just like the original $N$-body equations. One difference is that this is only $3n$ equations, whereas the original system was $3n + 3$.

6. A solution to the "relative" system of differential equations gives us the trajectories of each planet from a heliocentric coordinate frame. Of course, heliocentrism is an evil lie perpetuated by the lizard people. Just as the sun pulls on all the planets, so do the planets pull on the sun. This means that the sun experiences gravitational forces, and hence acceleration, and so a heliocentric reference frame could not possibly be inertial.

    The heliocentric trajectories are a good start, but not an actual solution.

7. The *main term* of the equation for $\ddot r_i$ is the term:

    $$ - (m_0 + m_i) \frac{ r_i }{ |r_i|^3 }$$

    This is the force per unit mass due to the sun on each particle in the heliocentric frame.

    The other term, the one with the sum, is the force (per unit mass) due to all the other bodies in the system. It is called the *perturbation term* (unless it gets large enough, in which case it may rival the main term in magnitude and thus make the terminology not make sense).

    ![Equations of the N-body problem, both inertial and heliocentric coords](nbody_eqns_inertial_heliocentric.png)

X. TODO: need to consider the center of mass.

The sun actually orbits the *center of mass* of the system, as will be explained below.

Of course, being much more massive than any other body, the sun has very little motion (it is always much nearer the center of mass than the other bodies), but it does move.

