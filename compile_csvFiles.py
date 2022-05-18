'''
Program written to read csv files and them compile all the values sorted by voltage and radius
Written: 16.05.22
Author: Hanna Song
'''

import numpy as np
import pandas as pd
import calculate_em

members =[]
names = input("Who are in your group? ")
members = names.split(' ')

voltages = [150, 200, 250, 300]
radii = [0.02, 0.03, 0.04, 0.05]


# Combine all the tables from each member to make a meta table
metaDF = pd.DataFrame()
for m in members:
    for v in voltages:
        data = pd.read_csv(f"emValues/values_{m}/{v}Volts.csv", sep=' ')
        df = pd.DataFrame(data, columns=['radius','currentMean', 'em(10^11C/kg)'])
        df.insert(0, "volt", v, True); df.insert(0, "name", m, True)

        metaDF = metaDF.append(df)

# Sort by their voltages and radii
compliedDF = pd.DataFrame()
for v in voltages:
    df = metaDF[metaDF['volt'] == v]
    df = df.sort_values(by=['radius'])

    compliedDF = compliedDF.append(df)

    compliedDF.to_csv(f"emValues/CompliedValues.csv", sep=' ')

# Split the dataframe by voltage and radii
# Then save into csv files
for v in voltages:
    vdf = compliedDF[compliedDF['volt']==v]
    for r in radii:
        rdf = vdf[vdf['radius']==r]
        rdf.to_csv(f"emValues/{v}_{r}_values.csv", sep=' ')
        #print(rdf)

