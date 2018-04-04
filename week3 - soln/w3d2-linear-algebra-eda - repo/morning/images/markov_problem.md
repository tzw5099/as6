### Part 1 Markov process

The 2004 state of the land can be described as a vector:

![](images/x0.gif)

The state of the land in 2009 can be obtained by matrix multiplication:

![](images/x1.gif)

In 2009 the commercial area will be 19.5% (11.7 mi<sup>2</sup>), the industrial 34% (20.4 mi<sup>2</sup>)  and the residential 46.5% (29.9 mi<sup>2</sup>).  

Now, 2014 state can be obtained from 2009 state:

![](images/x2.gif)


To find the stationary state, we need to find the eigenvector corresponding to eigenvalue 1: i.e., **A x = x**:

![](images/eigen1.gif)

This gives us three linear equations:

![](images/equations.gif)

These can be solved by setting x<sub>3</sub> = 1, and then back propagation:

![](images/x.gif)
