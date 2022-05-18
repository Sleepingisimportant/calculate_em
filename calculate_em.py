'''
Program written to calculate the specific charge e/m
The mean of the currents will be calculated first, then e/m and (e/m)^2
Written: 14.05.22
Author: Hanna Song
'''
import math

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


