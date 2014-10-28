# Move a particle left or right one space.

def moveparticle(density):

   from numpy import array, asarray, arange, any
   from numpy.random import randint, choice

   density=asarray(density)

   if density.ndim != 1:
      raise ValueError("Density must be one dimensional")

   if density.dtype.kind != 'i': 
      raise TypeError('Density must be an array of integers')

   if any(density < 0):
      raise ValueError("Density must contain only positive integers")

   nonzero=arange(density.size)[density != 0]
   
   if len(nonzero) == 0:
      raise ValueError("We can't move particles if there aren't any to move.")

   loc = choice(nonzero)

   if loc == 0: move = 1
   elif loc == density.size- 1: move = -1
   else: move = choice([-1, 1])

   newdensity= density.copy()
   newdensity[loc] -= 1
   newdensity[loc + move] += 1

   return newdensity