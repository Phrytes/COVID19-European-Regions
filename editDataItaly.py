import pandas
import os


def editDataIT():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfIT = pandas.read_csv('../Data/Sources/IT/dati-regioni/dpc-covid19-ita-regioni.csv')
    # Load column names:
    colNames = pandas.read_csv('variableTable_ALL.csv', index_col="IT")[["Measure"]].to_dict()['Measure']
    dfIT = dfIT.rename(columns=colNames)
    dfIT = dfIT.drop(["lat", "long", "note_it", "note_en"], axis=1)
    dfIT['RegionType'] = 'Region'
    dfIT['Country'] = 'IT'
    dfIT['Date'] = pandas.to_datetime(dfIT['Date']).dt.date
    dfIT = dfIT.melt(id_vars=['Country', 'Date', 'Region', 'RegionCode', 'RegionType'])
    return dfIT

dfIT = editDataIT()
