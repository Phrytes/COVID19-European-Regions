import pandas
import os


def editDataCH():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfCH = pandas.read_csv('../Data/Sources/CH/COVID19_Fallzahlen_CH_total.csv')
    # Load column names:
    colNames = pandas.read_csv('variableTable_ALL.csv', index_col="CH")[["Measure"]].to_dict()['Measure']
    dfCH = dfCH.rename(columns=colNames)
    dfCH = dfCH.drop(['time', 'source'], axis=1)
    # Create Region column (needed for merge with Geodata)
    dfCH['Region'] = dfCH['RegionCode']
    dfCH['RegionType'] = 'Canton'
    dfCH['Country'] = 'CH'
    dfCH = dfCH.melt(id_vars=['Country', 'Date', 'Region', 'RegionCode', 'RegionType'])
    # Define function for finding rows for Liechtenstein
    def CHorLI(row):
        if row['RegionCode'] == 'FL':
         country = "LI"
        else:
         country = "CH"
        return(country)

    dfCH['Country'] = dfCH.apply(lambda row: CHorLI(row), axis=1)
    return(dfCH)

dfCH = editDataCH()