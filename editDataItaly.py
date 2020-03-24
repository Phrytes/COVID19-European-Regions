import pandas
import os


def editDataIT():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfIT = pandas.read_csv('../Data/Sources/IT/dati-province/dpc-covid19-ita-province.csv')
    dfIT = dfIT.groupby(['data', 'codice_regione', 'denominazione_regione'], as_index=False)[['totale_casi']].sum()
    dfIT.columns = ['Date', 'RegionCode', 'Region', 'value']
    dfIT['variable'] = 'Conf.Cases'
    dfIT['RegionType'] = 'Region'
    dfIT['Country'] = 'IT'
    return dfIT

dfIT = editDataIT()
