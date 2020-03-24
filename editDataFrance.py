import pandas
import os


def editDataFR():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfFR = pandas.read_csv('../Data/Sources/FR/dist/chiffres-cles.csv')
    dfFR.columns = ['Date', 'RegionType', 'RegionCode', 'Region', 'Conf.Cases', 'Deceas.Cases', 'reanimation', 'Hosp.Cases', 'Cured.Cases', 'sourcenom', 'sourceurl', 'sourcetype']
    dfFR = dfFR.drop(['reanimation', 'sourcenom', 'sourceurl', 'sourcetype'], axis=1)
    dfFR = dfFR.melt(id_vars=['Date', 'RegionType', 'RegionCode', 'Region'])
    dfFR['Country'] = "FR"
    return dfFR

dfFR = editDataFR()