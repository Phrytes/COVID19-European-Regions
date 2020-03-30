import pandas
import os


def editDataDE():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfDE = pandas.read_csv('../Data/Sources/DE/RKI_Covid19_ALL.csv')
    dfDE.columns = ['Conf.Cases', 'specialAreas', 'Region', 'Date', 'NewCases', 'Conf.Cases.Rel', 'Deceas.Cases']
    dfDE = dfDE.drop(['specialAreas', 'Conf.Cases.Rel'], axis=1)
    dfDE = dfDE.melt(id_vars=['Date', 'Region'])
    dfDE['Country'] = 'DE'
    dfDE['RegionType'] = 'Bundesland'
    return dfDE

dfDE = editDataDE()
