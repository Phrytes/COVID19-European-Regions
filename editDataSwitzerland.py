import pandas
import os


def editDataCH():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfCH = pandas.read_csv('../Data/Sources/CH/COVID19_Fallzahlen_CH_total.csv')
    print(dfCH)
