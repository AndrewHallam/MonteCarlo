# Compare the initial and the new energy and determine whether or not to accept the move.

def compare(energy_old, energy_new, T):

   from numpy import exp
   from numpy.random import uniform

   # Make sure the temperature is valid
   if T == 0:
      raise ValueError("Temperature must be a positive number")
   if T < 0:
      raise ValueError("Temperature must be a positive number")

   # Check whether the move is accepted as defined in the notes. 
   if energy_old > energy_new:
      return True
   elif exp(-(energy_new - energy_old) / T) > uniform():
      return True
   else:
      return False