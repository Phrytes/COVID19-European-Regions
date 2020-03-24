import pandas
import os


def editDataUK():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Aggregate the following file:
    dfUK = pandas.read_csv('../Data/Sources/UK/Data/cases_by_utla.csv')
    dfUK.columns = ['Date', 'Region', 'value', 'RegionType', 'RegionCode']
    dfUK['variable'] = 'Conf.Cases'
    dfUK['Country'] = 'UK'
    dfUK['Date'] = dfUK['Date'].str.replace('/', '-')
    return dfUK

dfUK = editDataUK()
