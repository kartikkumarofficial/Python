import numpy as np
import pandas as pd

df =pd.DataFrame(np.arange(0,20).reshape(5,4),index=['R1','R2','R3','R4','R5'],columns=['C1','C2','C3','C4'])
# print(df.head())

# to export this as csv file
# df.to_csv('t.csv')

# print(df.loc[['R1','R3'],['C1','C2']])
# print(type(df['C1']))
# print(df.isnull().sum())

print(type(df[['C1','C2']]))

