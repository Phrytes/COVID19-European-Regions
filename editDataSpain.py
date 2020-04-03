import os, glob
import pandas
import re


def editDataES():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    inputLoc = "../Data/Sources/ES/COVID 19/"

    all_files = glob.glob(os.path.join(inputLoc, "*long.csv"))
    all_df = []
    for f in all_files:
        df = pandas.read_csv(f, sep=',')
        df['variable'] = re.findall('(ccaa_covid19_)(.*)(_long)', f)[0][1]
        all_df.append(df)

    dfES = pandas.concat(all_df, ignore_index=True, sort=True)
    dfES['variable'] = pandas.Categorical( dfES['variable'])\
        .rename_categories({'altas': 'Cured.Cases', 'casos': 'Conf.Cases', 'fallecidos': 'Deceas.Cases', 'hospitalizados': 'Hosp.Cases', 'uci' : 'IC.Cases'})
    dfES.columns = ['Region', 'RegionCode', 'Date', 'value', 'variable']
    dfES['Country'] = 'ES'
    return dfES

dfES = editDataES()