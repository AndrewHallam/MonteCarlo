# This is the main monte carlo script which will repeat the process a number of times.
# T is the temperature of the system.

def montecarlo(density, T=100, imax=20):

   import diffusion_model, mc_comparison, mc_moveparticle

   # Import the energy from the diffusion_model. If you wanted a different function
   # then another function could be defined here. 

   energy=diffusion_model.energy(density)
   
   # Iterate up to imax
   for i in range(imax):

      density_new=mc_moveparticle.moveparticle(density)
      energy_new=diffusion_model.energy(density_new)

      if mc_comparison.compare(energy, energy_new, T) == True:
         density=density_new
         energy=energy_new

      # Prints the density and energy at each step.
      print "Density is {}, and the energy is {}".format(density, energy)

   # Montecarlo returns both the energy and the density since both might be handy. 
   return (energy, density)

print montecarlo([10, 2, 1, 10, 1])
