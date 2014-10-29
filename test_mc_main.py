from mc_main import montecarlo
from nose.tools import assert_equal
from numpy import sum 
from numpy.random import random_integers

# Check that the particle number is conserved over the whole process.
def test_particle_conservation_interation():
  mctest1=random_integers(50, size=20)
  _ , mctest2=montecarlo(mctest1)
  assert_equal(sum(mctest1),sum(mctest2), "Particle number must be conserved")