# Move a particle left or right one space.

def moveparticle(density):

   from numpy import array, asarray, arange, any
   from numpy.random import randint, choice

   density=asarray(density)
   # Check the density array is only 1d.
   if density.ndim != 1:
      raise ValueError("Density must be one dimensional")

   # Check the density is only integers
   if density.dtype.kind != 'i': 
      raise TypeError('Density must be an array of integers')

   # Check the density is only positive
   if any(density < 0):
      raise ValueError("Density must contain only positive integers")

   # Find the elements of the density which are nonzero
   # so you don't decrease an element which is already zero
   nonzero=arange(density.size)[density != 0]
   
   # Raise error if it's just an array of zeros
   if len(nonzero) == 0:
      raise ValueError("We can't move particles if there aren't any to move.")

   # Choose a position to move a particle from
   loc = choice(nonzero)

   # If the location is either end of the array then move it towards the middle
   # otherwise just move it left or right.
   if loc == 0: move = 1
   elif loc == density.size- 1: move = -1
   else: move = choice([-1, 1])

   # A new density is then created. 
   newdensity= density.copy()
   newdensity[loc] -= 1
   newdensity[loc + move] += 1

   return newdensity