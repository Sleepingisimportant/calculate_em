'''
Program written to input four current values for each radii then generate a csv file for each voltage.

Written; 14.05.22
Author: Hanna Song
'''
import os
import calculate_em
import pandas as pd


radii = [.02, .03, .04, .05]
voltage = [150, 200, 250, 300]

user = input("What's your name? ")

dirName = f'values_{user}'

try:
    # Create target directory
    os.makedirs(f"emValues/{dirName}")
    print(f"Directory {dirName} created")
except FileExistsError:
    print(f"Directory {dirName} already exists")

for u in voltage:
    print("----------------------")
    print(f"For {u}V")
    print("----------------------\n")

    df = pd.DataFrame(
        columns=['radius', 'current_1', 'current_2', 'current_3', 'current_4', 'currentMean', 'em(10^11C/kg)', 'emsqrt(10^11C/kg)^2']
    )

    for r in radii:
        print("----------------------")
        print(f"for radius {r}")
        print("----------------------")
        c = input('Enter the current values: ')
        currents = c.split(' ')

        mean = calculate_em.currentMean(float(currents[0]), float(currents[1]), float(currents[2]), float(currents[3]))

        iMean, eM, eMSqrt = calculate_em.call_Values(mean, u, r)
        print(calculate_em.call_Values(mean, u, r))

        radius = r*100

        df.loc[radius,:] = [r, currents[0], currents[1], currents[2], currents[3], iMean, eM]

    df.to_csv(f"emValues/values_{user}/{u}Volts.csv", sep=' ')
