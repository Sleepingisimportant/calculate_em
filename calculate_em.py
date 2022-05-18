'''
Program written to calculate the specific charge e/m
The mean of the currents will be calculated first, then e/m and (e/m)^2
Written: 14.05.22
Author: Hanna Song
'''
import math
import numpy as np
import pandas as pd

pi = math.pi


def currentMean(i1, i2, i3, i4):
    imean = (i1 + i2 + i3 + i4)/4
    return imean

def calculate_em(u, i, r):
    uri2 = (u/((r*i)**2))
    mu = 4 * pi * 10**-7
    C = 2*(.20/(0.715*mu*154))**2
    em = (uri2 * C)/10**11
    return uri2, C, em

def call_Values(I, U, R):
    URI2, C, EM  = calculate_em(U, I, R)
    return I, EM

voltage = 200; meanCurrent = 3.4; radius = 0.02

uri2, C, em = calculate_em(voltage, meanCurrent, radius)

print(f"\nWhen the voltage is equal {voltage}, the meanCurrent is {meanCurrent},")
print(f"and the radius of the path of the electron beam is equal to 2cm then:\n")
print(f"U/(r*i)^2 is equal: {uri2}")
print(f"The constant C is equal: {C}")
print(f"e/m is equal: {em}")

