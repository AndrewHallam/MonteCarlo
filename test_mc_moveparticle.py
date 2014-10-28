
from mc_moveparticle import moveparticle
from nose.tools import assert_raises

def test_zero_density():
   with assert_raises(ValueError) as exception: moveparticle([0, 0, 0, 0])
   
def test_negative_density():
   with assert_raises(ValueError) as exception: moveparticle([-1, 1, 1, 1])

def test_nonintegers():
   with assert_raises(TypeError) as exception: moveparticle([0.1, 'a', 1])