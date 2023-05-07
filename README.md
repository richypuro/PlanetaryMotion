# PlanetaryMotion
'''
This code is for calculating and plotting the motion of the planets in our solar system
The main file initializes a y matrix, which contains the positions and velocities of the planets on a random day (data from JPL)
The script then used the functions defined in the functions file to fill the y matrix row-by-row until the total number of iterations specified has been reached,
using the specified time step h. Time steps of ~ 1day (8.6e+4 seconds) are stable for >200 years. Once the y matrix has been calculated, the analysis file
plots the trajectories or radial distances of the planets. The isolated planet file does the same thing for just one planet and the sun for comparison, and the 
animation file animates the planetary trajectories using turtle independent of the main file (the y matrix does not need to be compoted before running an animation).
'''
