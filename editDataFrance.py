import pandas
import os


def editDataFR():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfFR = pandas.read_csv('../Data/Sources/FR/dist/chiffres-cles.csv')

    # Load column names:
    colNames = pandas.read_csv('variableTable_ALL.csv', index_col="FR")[["Measure"]].to_dict()['Measure']
    dfFR = dfFR.rename(columns=colNames)
    dfFR = dfFR.drop(["source_nom", "source_url", "source_type", "source_archive"], axis=1)
    dfFR['RegionType'] = 'Region'
    dfFR['Country'] = 'FR'
    dfFR = dfFR.melt(id_vars=['Country', 'Date', 'Region', 'RegionCode', 'RegionType'])
    dfFR['Country'] = "FR"
    return dfFR

dfFR = editDataFR()