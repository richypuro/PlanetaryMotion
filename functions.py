# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 18:25:02 2023

@author: richy
"""
# This file is for defining functions associated with calculating a single RK4 step

import numpy as np

# Define the distance between two 3D vectors
def distance(r1, r2):
    return np.sqrt((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2 + (r1[2] - r2[2])**2)

# Calculate the acceleration of a single planet along a single axis
def acceleration(y, x, p, mass):  # x indicates x,y,z (0,1,2), p indicates planet number (sun is 0)
    G = 6.6743e-12  # Gravitational constant in the units that give acceleration as 1e8 m/s^2    
    planet_pos = y[p*6+x]
    planet_r = y[p*6:p*6+3]
    total_force = 0
    for i in range(int(len(y)/6)):
        if i != p:
            interacting_planet_pos = y[i*6+x]
            interacting_planet_r = y[i*6:i*6+3]
            total_force += G*mass[i]*(interacting_planet_pos - planet_pos)/distance(planet_r, interacting_planet_r)**3
    return total_force 
 
# Calculate dy/dt for a given set of positions and velocities
def dydt(y, mass):
    f = np.roll(y, -3)  # The derivative of position is velocity, so start by moving all the velocities where the positions are
    for p in range(int(len(y)/6)):
        for x in range(3):
            f[6*p+3+x] = acceleration(y, x, p, mass)
    return f

# Calculate a single step of the RK4 algorithm
def runge_kutta_step(y, h, mass):
    k1 = dydt(y, mass)
    k2 = dydt(y + k1*h/2, mass)
    k3 = dydt(y + k2*h/2, mass)
    k4 = dydt(y + k3*h, mass)
    
    return y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*h

# Find local maxima (peaks of elliptical orbits)
def local_max(r):
    local_max = []
    for i in range(len(r)-2):
        if r[i-1] < r[i] and r[i+1] < r[i]:
            local_max.append(i)
    return local_max
        