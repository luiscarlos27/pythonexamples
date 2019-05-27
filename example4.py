import pandas as pd

d = pd.read_csv('FL_insurance_sample.csv')

x = d[0:5]['county'].isnull()

print(x)
