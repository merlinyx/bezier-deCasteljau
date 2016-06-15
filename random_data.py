# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:55:14 2016

@author: Yuxuan Mei
Create random data points as control points for interpolation.
This small program only generate no more than 10 points, with coordinate values
within the range of 0~10. 
It does not check whether it generates two same points. So be aware.
"""

import random

filename = input("Please enter the name of the output data file: ")
if len(filename) < 1:
    filename = "data.txt"
out_file = open(filename, 'w')

d = int(10 * random.random())
out_file.write("{}\n".format(str(d)))
for i in range(d+1):
    x = int(10 * random.random())
    y = int(10 * random.random())
    out_file.write("{} {}\n".format(str(x),str(y)))
out_file.close()

print("{} is created under this directory. \n".format(filename))