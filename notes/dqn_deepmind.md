1. Some links:

     - Google Research blog post on the paper: http://googleresearch.blogspot.com/2015/02/from-pixels-to-actions-human-level.html
     - The source code that goes along with the paper: https://sites.google.com/a/deepmind.com/dqn/
     - Jürgen Schmidhuber has some doubts about how novel the result here actually is: http://people.idsia.ch/~juergen/naturedeepmind.html. Worth reading for the bibliography alone.
     - A ReadCube link to the paper: http://www.readcube.com/articles/10.1038%2Fnature14236 (I didn't find this to be very usable)

2. **Experience replay** seems to be important. The Google Research post says:

     >  DQN incorporated several key features...Foremost among these was a neurobiologically inspired mechanism, termed “experience replay,” whereby during the learning phase DQN was trained on samples drawn from a pool of stored episodes—a process physically realized in a brain structure called the hippocampus through the ultra-fast reactivation of recent experiences during rest periods (e.g., sleep). Indeed, the incorporation of experience replay was critical to the success of DQN: disabling this function caused a severe deterioration in performance.

    Schmidhuber also references "experience replay", and the reference is

        L. Lin. Reinforcement Learning for Robots Using Neural Networks. PhD thesis, Carnegie Mellon University, Pittsburgh, 1993. 

    which is available online here: http://www.dtic.mil/dtic/tr/fulltext/u2/a261434.pdf

3. DQN uses convolutional nets. I don't understand these yet, but here are some resources I found for understanding them:

     - http://colah.github.io/posts/2014-07-Conv-Nets-Modular/
     - http://colah.github.io/posts/2014-07-Understanding-Convolutions/
     - http://colah.github.io/posts/2014-12-Groups-Convolution/
     - The DQN paper references this paper for convolutional nets: *LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P. Gradient-based learning applied to document recognition. Proc. IEEE 86, 2278–2324 (1998).*
     - Referenced by Schmidhuber: *K. Fukushima, K. (1979). Neural network model for a mechanism of pattern recognition unaffected by shift in position - Neocognitron. Trans. IECE, J62-A(10):658-665.*
     - Also referenced by Schmidhuber: *Y. LeCun, B. Boser, J. S. Denker, D. Henderson, R. E. Howard, W. Hubbard, L. D. Jackel. Back-propagation applied to handwritten zip code recognition. Neural Computation, 1(4):541-551, 1989*

