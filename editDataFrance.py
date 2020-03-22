import pandas
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Aggregate the following file:
df = pandas.read_csv('../Data/Sources/FR/dist/chiffres-cles.csv')
print(df)
