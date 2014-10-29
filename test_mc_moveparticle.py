
from mc_moveparticle import moveparticle
from nose.tools import assert_raises, assert_equal
from numpy import sum
from numpy.random import random_integers

def test_zero_density():
   with assert_raises(ValueError) as exception: moveparticle([0, 0, 0, 0])
   
def test_negative_density():
   with assert_raises(ValueError) as exception: moveparticle([-1, 1, 1, 1])

def test_nonintegers():
   with assert_raises(TypeError) as exception: moveparticle([0.1, 'a', 1])

def test_particle_conservation():
  dtest1=random_integers(50, size=20)
  dtest2=moveparticle(dtest1)
  assert_equal(sum(dtest1),sum(dtest2), "Particle number must be conserved")
