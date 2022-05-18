'''
Program written to calculate the standard deviation
Written: 16.05.22
Author: Hanna Song
'''

import numpy as np
import pandas as pd
import calculate_em

data = pd.read_csv('emValues/values_Song/150Volts.csv', sep=' ')

df = pd.DataFrame(data, columns=['radius', 'em'])

print(data)
print(df)
