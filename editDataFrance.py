import pandas
import os


def editDataFR():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfFR = pandas.read_csv('../Data/Sources/FR/dist/chiffres-cles.csv')
    dfFR.columns = ['Date', 'RegionType', 'RegionCode', 'Region', 'Conf.Cases', 'Deceas.Cases', 'Deceas.Cases.NursingHome', 'Hosp.Resp.Cases', 'Hosp.Cases', 'Cured.Cases', 'Screened', 'sourcenom', 'sourceurl', 'sourcearchive', 'sourcetype']
    dfFR = dfFR.drop(['sourcenom', 'sourceurl', 'sourcearchive', 'sourcetype'], axis=1)
    dfFR = dfFR.melt(id_vars=['Date', 'RegionType', 'RegionCode', 'Region'])
    dfFR['Country'] = "FR"
    return dfFR

dfFR = editDataFR()