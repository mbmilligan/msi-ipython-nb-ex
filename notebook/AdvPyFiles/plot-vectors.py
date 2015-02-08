#!python

import numpy as np 
from pylab import * 
from numpy import ma 
X,Y = meshgrid( arange(0,2*pi,.2),arange(0,2*pi,.2) ) 
U = cos(X) 
V = sin(Y)

figure() 
Q = quiver( X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3], 
                  pivot='mid', color='r', units='inches' ) 
qk = quiverkey(Q, 0.5, 0.03, 1, r'$1 \frac{m}{s}$', 
                  fontproperties={'weight': 'bold'}) 
plot( X[::3, ::3], Y[::3, ::3], 'k.') 
axis([-1, 7, -1, 7]) 
title("pivot='mid'; every third arrow; units='inches'")
show()
