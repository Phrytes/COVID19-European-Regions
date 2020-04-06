import pandas
import os


def editDataNL():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfNL = pandas.read_csv('../Data/Sources/NL/data/rivm_corona_in_nl.csv')
    # Load column names:
    colNames = pandas.read_csv('variableTable_ALL.csv', index_col="NL")[["Measure"]].to_dict()['Measure']
    dfNL = dfNL.rename(columns=colNames)
    dfNL = dfNL.groupby(['Date', 'Region'], as_index=False)[['Cumul.Cases']].sum()
    dfNL = dfNL.melt(id_vars=['Date', 'Region'])
    dfNL['RegionType'] = 'Province'
    dfNL['Country'] = 'NL'
    return dfNL

dfNL = editDataNL()

