# This is the main monte carlo script which will repeat the process a number of times.
# T is the temperature of the system.

def montecarlo(density, T):

   import diffusion_model, mc_comparison, mc_moveparticle

   energy=diffusion_model.energy(density)
   for i in range(10):

      density_new=mc_moveparticle.moveparticle(density)
      energy_new=diffusion_model.energy(density_new)

      if mc_comparison.compare(energy, energy_new, T) == True:
         density=density_new
         energy=energy_new

      print "Density is {}, and the energy is {}".format(density, energy)

   return energy

print montecarlo([3, 7, 4], 10)