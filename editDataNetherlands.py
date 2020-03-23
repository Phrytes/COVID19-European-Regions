import pandas
import os


def editDataNL():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfNL = pandas.read_csv('../Data/Sources/NL/data/rivm_corona_in_nl.csv')
    dfNL = dfNL.groupby(['Datum', 'Provincienaam'], as_index=False)[['Aantal']].sum()
    dfNL.columns = ['Date', 'Region', 'value']
    dfNL['variable'] = 'Conf.Cases'
    dfNL['RegionType'] = 'Province'
    dfNL['Country'] = 'NL'
    return dfNL

dfNL = editDataNL()

