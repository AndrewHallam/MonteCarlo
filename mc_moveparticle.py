# Move a particle left or right one space.

def moveparticle(density):

   from numpy import array, asarray, arange
   from numpy.random import randint, choice

   density=asarray(density)

   if density.ndim != 1:
      raise ValueError("Density must be one dimensional")

   if density.dtype.kind != 'i': 
      raise TypeError('Density must be an array of integers')

   nonzero=arange(density.size)[density != 0]
   
   loc = choice(nonzero)

   if len(nonzero) == 0: raise ValueError("We can't move particles if there aren't any to move!")

   if loc == 0: move = 1
   elif loc == density.size- 1: move = -1
   else: move = choice([-1, 1])

   newdensity= density.copy()
   newdensity[loc] -= 1
   newdensity[loc + move] += 1

   return newdensity