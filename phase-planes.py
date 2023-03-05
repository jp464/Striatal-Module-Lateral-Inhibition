import numpy as np
import matplotlib.pyplot as plt
from phaseportrait import PhasePortrait2D

'''
Author: Stanley Park
Last updated: Mar 5 2023 
'''

# Initial parameters
tau_x = 1
tau_y = 1.5
beta = 0.1
lam = 100
thres = .4

# Transfer function
def phi(x):
    return 1 / (1 + np.exp(-lam * (x-thres)))

# Differential equation 1 and 2 
def dF(x1, x2,*, W=-1, I1=0, I2=0, y1=0, y2=0):
    return -x1 + phi(W*x2*y2 + I1), -x2 + phi(W*x1*y1 + I2)

modelpp = PhasePortrait2D(dF, [[-2,2], [-2,2]], color="Greys", Title="", xlabel=r'$M_1$', ylabel=r'$M_2$')
modelpp.add_nullclines(precision=.023, xcolor='mediumblue', ycolor='darkorange')
modelpp.add_slider("y1", valinit=0, valinterval=[0, 1], valstep=.1)
modelpp.add_slider("y2", valinit=0, valinterval=[0, 1], valstep=.1)
modelpp.add_slider("I1", valinit=0, valinterval=[0, 1], valstep=.1)
modelpp.add_slider("I2", valinit=0, valinterval=[0, 1], valstep=.1)
modelpp.plot()
plt.show()