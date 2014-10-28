# Move a particle left or right one space.

def moveparticle(density)

   from numpy import array, as array
   from numpy.random import randint, choice

   density=asarray(density)

   # Choose the range over which a random particle will be selected.
   size=density.size

   # Choose the location the particle will move from.
   loc=randint(size)