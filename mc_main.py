# This is the main monte carlo script which will repeat the process a number of times.

def montecarlo(density)

   import diffusion_model, mc_comparison, mc_moveparticle
   from numpy import 

   i=0
   energy1=diffusion_model.energy(density)
   while i < 10

      density_new=mc_moveparticle.moveparticle(density)
      energy2=diffusion_model.energy(density_new)

      if mc_comparison.compare(energy1, energy2) = true
      density=density_new

      else break

      i += 1
   
   
print montecarlo([1 1 1]