# Compare the initial and the new energy and determine whether or not to accept the move.

def compare(energy_old, energy_new)

   from numpy import exp
   from numpy.random import uniform

   if energy_old > energy_new:
      return True
   elif exp(-(energy_new - energy_old) / 1.) > uniform():
      return True
   else:
      return False