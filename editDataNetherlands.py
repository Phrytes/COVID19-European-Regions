import pandas
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Aggregate the following file:
df = pandas.read_csv('../Data/Sources/NL/data/rivm_corona_in_nl_daily.csv')
print(df)