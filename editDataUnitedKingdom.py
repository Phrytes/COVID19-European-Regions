import pandas
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Aggregate the following file:
df = pandas.read_csv('../Data/Sources/UK/Data/cases_by_utla.csv')
print(df)