# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:38:22 2016

@author: Yuxuan Mei
A program to compute Bezier curves.
But note that higher degrees do not guarantee good interpolation. 
Use composite Bezier curves for cases with more control points. 
"""

import numpy as np
import matplotlib.pyplot as plt

def deCasteljau(d, control_points, t):
    '''
    Use the de Casteljau Algorithm to calculate Bezier curves.
    Reference: Spline Methods Draft by Tom Lyche and Knut Mørken  
    '''
    bezier = [[None for _ in range(d+1)] for _ in range(d+1)]
    tt = 1 - t
    for i in range(d+1):
        bezier[i][0] = np.array(control_points[i])
    for r in range(1, d+1):
        for i in range(r, d+1):
            bezier[i][r] = tt * bezier[i-1][r-1] + t * bezier[i][r-1]
    return bezier[d][d]

def main():
    # get data from text file
    filename = input("Please enter the name of the input data file: ")
    if len(filename) < 1:
        filename = "input.txt"
    in_file = open(filename, "r")
    d = int(in_file.readline().rstrip())
    control_points = []
    for i in range(d+1):
        x, y = in_file.readline().rstrip().split(" ")
        x, y = float(x), float(y)
        control_points.append([x,y])
        plt.plot(x,y,'ko')
    in_file.close()
    
    # calculate points on the curve
    step = 0.01 # change the step to get finer/coarser curves
    x_data, y_data = [], []
    coordinate = []
    for i in range(int(1/step)):
        t = i * step
        coordinate = deCasteljau(d, control_points, t)
        x_data.append(coordinate[0])
        y_data.append(coordinate[1])
    
    # plot the curve
    plt.plot(x_data, y_data, 'b.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bezier curve of degree {}'.format(str(d)))
    plt.show()

# run the main
main()