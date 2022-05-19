'''
Program written to calculate the propagation error.
Written: 18.05.22
Author: Hanna Song
'''
import pandas as pd

error_R = 0.002  # 2 mm in meters
R = .20          # 20 cm in meters
error_U = 6      # volts
error_r = 0.0005 # 0.5 mm in meters
error_I = 0.09   # 90 mA in Amperes

# function to calculate the largest possible relative error
def calculateLargestPossibleRelativeError(U, r, I):
    relError_R = abs(2*error_R/R)
    relError_U = abs(error_U/U)
    relError_r = abs(2*error_r/r)
    relError_I = abs(2*error_I/I)

    lprerror = relError_R + relError_U + relError_r + relError_I
    return relError_R, relError_U, relError_r, relError_I, lprerror

voltages = [150, 200, 250, 300]
radii = [0.02, 0.03, 0.04, 0.05]

lprErrorDF = pd.DataFrame(columns=['relError_R', 'relError_U', 'relError_r', 'relError_I', 'lprerror'])

i = 0

# for loops takes values that are already generated and stored in emValues
for v in voltages:
    for r in radii:
        df = pd.read_csv(f"emValues/byVoltRadius/{v}_{r}_values.csv", sep=' ')
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        mean_I = df['currentMean'].mean()

        r = r*100; int(r)

        relError_R, relError_U, relError_r, relError_I, lprerror = calculateLargestPossibleRelativeError(v, r, mean_I)

        lprErrorDF.loc[i,:] = [relError_R, relError_U, relError_r, relError_I, lprerror]

        i += 1

lprErrorDF.to_csv(f"errorValues/relErrorValues.csv")
print("Error values stored in errorValues/relErrorValues.csv")
