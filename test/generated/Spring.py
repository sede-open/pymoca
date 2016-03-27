
# do not edit, generated by pymola

from __future__ import print_function, division
import sympy
import sympy.physics.mechanics as mech
from pymola.sympy_runtime import OdeModel

class Spring(OdeModel):

    def __init__(self):

        super(Spring, self).__init__()

        # states
        x, v_x = mech.dynamicsymbols('x, v_x')
        self.x = sympy.Matrix([x, v_x])

        # inputs
        self.u = sympy.Matrix([])

        # outputs
        self.y = sympy.Matrix([])

        # constants
        self.c = sympy.Matrix([])
        self.c0 = {
            }

        # parameters
        c, k = sympy.symbols('c, k')
        self.p = sympy.Matrix([c, k])
        self.p0 = {
            'c' : 0.1,
            'k' : 2,
            }

        # variables
        self.v = sympy.Matrix([])
      
        # equations
        self.eqs = [
            (x).diff(self.t) - (v_x),
            (v_x).diff(self.t) - (- k * x - c * v_x),
            ]

        self.compute_fg()
    