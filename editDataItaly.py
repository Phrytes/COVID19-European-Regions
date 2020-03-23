import pandas
import os


def editDataIT():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfIT = pandas.read_csv('../Data/Sources/IT/dati-province/dpc-covid19-ita-province.csv')
    print(dfIT)
