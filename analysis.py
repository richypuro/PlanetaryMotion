# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:41:09 2023

@author: richy
"""
# This file is for visualizing planetary orbits, calculated in main.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import functions as fc

#%% Plot planetary orbits in xy-plane

plt.figure(figsize=(6,6))
for i in range(9):
    plt.plot(positions[:,3*i], positions[:,3*i+2])
bound = 5e4
plt.xlim(-bound, bound)
plt.ylim(-bound, bound)
plt.show()

#%% Plot radial distance of planets from the origin

plt.figure(figsize=(8,6))
x = np.linspace(0, 200, 365*200)
#for i in range(9):
i=8
plt.plot(x, distances[:,i], markersize=0, color=(1-i/8,0,i/8,1))
#plt.ylim(np.max(distances[:,i])-1, np.max(distances[:,i])+0.1)
plt.show()

print(np.max(distances[:,i])+np.min(distances[:,i]))
local_max = fc.local_max(distances[:,i])
for i in range(20):
    print(x[local_max[i+1]]-x[local_max[i]])

#%% Plot isolated planetary orbits in xy-plane

plt.figure(figsize=(6,6))
plt.plot(positions_ven[:,0], positions_ven[:,1], color=(1,0,0,1))
bound = 2e3
plt.xlim(-bound, bound)
plt.ylim(-bound, bound)
plt.show()

#%% Plot radial distance of isolated planets from the sun

plt.figure()
x = np.linspace(0, 200, 365*200)
for i in range(2):
    plt.plot(x, distances_earth[:], markersize=0, color=(1-i/8,0,i/8,1))
plt.xlim(0,200)
#plt.ylim(1.4e3, 1.6e3)
plt.show()

#%%
def sine(x, a, k, phi, d):
    return a*np.sin(k*x + phi) + d

'''
Fit parameter initial guesses:
    Sun - N/A
    Mercury - p0=(100, (2*np.pi)/(0.241), np.pi/6, 550)
    Venus - p0=(10, (2*np.pi)/(0.65), np.pi/2, 1080)
    Earth - p0=(30, (2*np.pi)/(1), 0, 1500)
    Mars - p0=(200, (2*np.pi)/(1.88), np.pi, 2300)
    Jupiter - p0=(350, (2*np.pi)/(12), np.pi/3, 7800)
    Saturn - p0=(1600, (2*np.pi)/(30), np.pi/4, 14200)
    Uranus - p0=(2500, (2*np.pi)/(80), np.pi/4, 28500)
    Neptune - p0=(700, 1/(150*(2*np.pi)), np.pi, 45000)
'''

x = np.linspace(0, 200, 365*200)
plt.figure()
plt.plot(x,distances[:,1])
#popt, pcov = curve_fit(sine, x, distances[:,1], p0=(100, (2*np.pi)/(0.2408), np.pi/4, 550))
print(popt)
#plt.plot(x, sine(x, popt[0], popt[1], popt[2], popt[3]))
#plt.plot(x, distances[:,1] - sine(x, popt[0], popt[1], popt[2], popt[3]))
plt.xlim(0,200)
plt.show()

#%% Fourier transform radial distance of each planet to see if it breaks down into the frequencies ot the other planets' orbits

from numpy.fft import fft, fftfreq

planet_num = 1
d = distances[:,planet_num] - np.mean(distances[:,planet_num])
ft = fft(d)
freq = fftfreq(d.shape[-1])

plt.plot(freq, ft)
plt.ylim(0,1e4)
plt.xlim(0,0.01)

