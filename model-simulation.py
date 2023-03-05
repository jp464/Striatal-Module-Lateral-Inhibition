import numpy as np
import matplotlib.pyplot as plt

'''
Author: Stanley Park
Last updated: Mar 5 2023 
'''

# Stimulation parameters -- adjust input current values that range from 0 to 1
dt = 0.01
timesteps = 4000
I1 = []
I2 = []
for t in range(timesteps):
    # When I=0, add noise to input current 
    I1.append(np.random.poisson()*.1)
    I2.append(np.random.poisson()*.1)

    # Add current at t=5
    if 500 < t < 1500:
        I1[-1] += 0
        I2[-1] += 0

    # Add current at t=25
    if 2500 < t < 3500:
        I1[-1] += 0
        I2[-1] += 0

# Initial parameters
tau_x = 1
tau_y = 1.5
W = -1
beta = 0.1
lam = 100
thres = .4

# Transfer function
def phi(x):
    return 1 / (1 + np.exp(-(x-thres) * lam))

# Initialize x's and y's 
x1 = [0]
x2 = [0]
y1 = [0]
y2 = [0]

# Update values in each iteration of Euler's method 
def update(t, I1, I2):
    # Update x1 and x2
    x1_dot = (-x1[-1] + phi((W * x2[-1] * y2[-1] + I1))) / tau_x
    x2_dot = (-x2[-1] + phi((W * x1[-1] * y1[-1] + I2))) / tau_x
    x1.append(x1[-1] + x1_dot * t)
    x2.append(x2[-1] + x2_dot * t)
    
    # Update y1 and y2
    y1_dot = (-(y1[-1] - 1) * x1[-1]) - (y1[-1] - beta) * (1 - x1[-1]) / tau_y
    y2_dot = (-(y2[-1] - 1) * x2[-1]) - (y2[-1] - beta) * (1 - x2[-1]) / tau_y
    y1.append(y1[-1] + y1_dot * t)
    y2.append(y2[-1] + y2_dot * t)

# Run simulation
for i in range(timesteps-1):
    update(dt, I1[i], I2[i])

# Plot results
t = np.arange(0, timesteps*dt, dt)
fig, axes = plt.subplots(3)
[axes[i].set_ylim(ymax=1.1, ymin=0) for i in range(len(axes))]
axes[0].plot(t, x1, color='mediumblue', label="Module 1")
axes[0].plot(t, x2, '--', color='darkorange', label="Module 2")
axes[0].set_ylabel(r'$x_i$')
axes[1].plot(t, y1, color='mediumblue')
axes[1].plot(t, y2, '--', color='darkorange')
axes[1].set_ylabel(r'$y_i$')
axes[2].plot(t, I1, color='mediumblue')
axes[2].plot(t, I2, '--', color='darkorange')
axes[2].set_xlabel("Time")
axes[2].set_ylabel(r'$I_i$')
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right')
plt.show()