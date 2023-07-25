'''
filename: circleArea.py             
                                                     
This program asks the user to input a               
number for the radius of a circle.  The program     
then calculates and output the area of the circle.
'''

import math
import sys

def computeArea(r):
    return(math.pi * r **2)

radius = float(input( "Enter radius in feet : " )) 
 
sys.stdout.write("The radius you provided was " + format(radius,'.2f') +
                " feet and the area is about " + format(computeArea(radius),'.2f') + " sq feet" )
