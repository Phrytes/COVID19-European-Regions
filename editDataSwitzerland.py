import pandas
import os


def editDataCH():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfCH = pandas.read_csv('../Data/Sources/CH/COVID19_Fallzahlen_CH_total.csv')
    dfCH.columns = ['Date', 'Time', 'RegionCode', 'Screened', 'Conf.Cases', 'Hosp.Cases', 'IC.Cases', 'Hosp.Resp.Cases', 'new_out.Hosp.Cases', 'Deceas.Cases', 'sourceurl']
    dfCH = dfCH.drop(['Time', 'sourceurl'], axis=1)
    # Create Region column (needed for merge with Geodata)
    dfCH['Region'] = dfCH['RegionCode']
    dfCH = dfCH.melt(id_vars=['Date', 'RegionCode', 'Region'])
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