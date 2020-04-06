import pandas
import os


def editDataDE():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfDE = pandas.read_csv('../Data/Sources/DE/RKI_Covid19_ALL.csv')
    # Load column names:
    colNames = pandas.read_csv('variableTable_ALL.csv', index_col="DE")[["Measure"]].to_dict()['Measure']
    dfDE = dfDE.rename(columns=colNames)
    dfDE = dfDE.drop(['Besonders betroffene Gebiete'], axis=1)

    dfDE = dfDE.melt(id_vars=['Date', 'Region'])
    dfDE['Country'] = 'DE'
    dfDE['RegionType'] = 'Bundesland'
    return dfDE

dfDE = editDataDE()
