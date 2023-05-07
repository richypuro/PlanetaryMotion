# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 18:23:47 2023

@author: richy
"""
# This script is for calculating the motion of the planets in our solar system

import numpy as np
import functions as fc

#%% This part of the script sets all the initial parameters and initializes the y array

# y = [x_planet1, y_planet1, z_planet1, vx_planet1, vy_planet1, vz_planet1, x_planet2, ...]
# Mass units are 1e+23 kg
# Length units are 1e+8 meters
# Time units are 1 s  (so velocity and acceleration are 1e+8 m/s and m/s^2)

# Define initial conditions as given by JPL HORIZONS (April 6th, 2018)
num_planets = 9

#                   Sun,         Mercury,     Venus,       Earth,       Mars,        Jupiter,     Saturn,      Uranus,      Neptune
planet_mass =      [1.98854e+7,  3.302,       4.8685e+1,   5.97219e+1,  6.4185,      1.89813e+4,  5.68319e+3,  8.68103e+2,  1.0241e+3]
planet_xinitial =  [1.81899,    -5.67576e+2,  4.2848e+2,  -1.43778e+3, -1.14746e+3, -5.66899e+3,  8.20513e+2,  2.62506e+4,  4.303e+4]
planet_yinitial =  [9.8363,     -2.73592e+2,  1.00073e+3, -4.00067e+2, -1.96294e+3, -5.77495e+3, -1.50241e+4,  1.40273e+4, -1.24223e+4]
planet_zinitial =  [-0.15878,    2.89173e+1, -1.11972e+1, -0.13888,    -1.32908e+1,  1.50755e+2,  2.28565e+2, -2.87982e+2, -7.35857e+2]
planet_vxinitial = [-1.12474e-7, 1.16497e-4, -3.2293e-4,   7.65151e-5,  2.18369e-4,  9.16793e-5,  9.11312e-5, -3.25937e-5,  1.47132e-5]
planet_vyinitial = [7.54876e-8, -4.14793e-4,  1.3696e-4,  -2.87514e-4, -1.01132e-4, -8.53244e-5,  4.96372e-6,  5.68878e-5,  5.25363e-5]
planet_vzinitial = [2.68723e-9, -4.45952e-5,  2.05091e-5,  2.08354e-8, -7.47957e-6, -1.69767e-6, -3.71643e-6,  6.32569e-7, -1.42701e-6]

y = np.zeros((365*200, 54))  # initialize array with 54 columns (one for each of the 8 planets and the suns' positions and velocities)

# First row of array is the initial positions and velocities of the planets
for i in range(num_planets):
    y[0,6*i] = planet_xinitial[i]
    y[0,6*i+1] = planet_yinitial[i]
    y[0,6*i+2] = planet_zinitial[i]
    y[0,6*i+3] = planet_vxinitial[i]
    y[0,6*i+4] = planet_vyinitial[i]
    y[0,6*i+5] = planet_vzinitial[i]

#%% Now that the y array is initialized, use the functions in functions.py to calculate y(t) using RK4

# h - time steps in units of seconds; 8.64e+4 = 1 day
for i in range(len(y[:,0])-1):
    y[i+1,:] = fc.runge_kutta_step(y[i,:], h=8.64e+4, mass=planet_mass)


#%% Make arrays containing just the positions (in cartesian coordinates) as well as the total distance from our origin

positions = np.zeros((len(y[:,0]), 3*num_planets))
distances = np.zeros((len(y[:,0]), num_planets))
for i in range(len(y[:,0])):
    for j in range(num_planets):
        positions[i,3*j] = y[i,6*j]
        positions[i,3*j+1] = y[i,6*j+1]
        positions[i,3*j+2] = y[i,6*j+2]
        distances[i,j] = fc.distance(y[i,6*0:6*0+3],y[i,6*j:6*j+3])


