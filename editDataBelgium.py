import os
import pandas as pd

# Connect to variable table
# Combine general, hosp and mort data
# split provinces and subregions
# capitalize columnnames; REGIONTYPE
# Sum TOTALIN_IN_RESP and TOTAL_IN_ECMO cases
# Ref: https://epistat.sciensano.be/COVID19BE_codebook.pdf

def editDataBE():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Read files
    dataFilesBE = '../Data/Sources/BE/Raw/COVID19BE_Source.xlsx'
    dfBE_Hosp = pd.read_excel(dataFilesBE, sheet_name='HOSP')
    dfBE_Hosp['DATE']=dfBE_Hosp['DATE'].astype(str)
    dfBE_Mort = pd.read_excel(dataFilesBE, sheet_name='MORT')
    #dfBE_Cases_Cum = pd.read_excel(dataFilesBE, sheet_name='CASES_MUNI_CUM')
    # Aggregate files
    # 1. By region
    dfBE_Hosp_Regions = dfBE_Hosp.groupby(['DATE', 'REGION'], as_index=False).sum()
    dfBE_Mort_Regions = dfBE_Mort.groupby(['DATE', 'REGION'], as_index=False).sum()
    #dfBE_Cases_Cum = dfBE_Cases_Cum.groupby(['DATE', 'TX_PROV_DESCR_NL'], as_index=False).sum()
    #dfBE_Cases_Cum.columns = {'TX_PROV_DESCR_NL': 'REGION'}
    dfBE_Regions = pd.merge(dfBE_Mort_Regions, dfBE_Hosp_Regions, on=['DATE', 'REGION'])
    dfBE_Regions.columns = ['Date', 'Region', 'Deceas.Cases', 'reportingHospitals', 'Hosp.Cases', 'IC.Cases', 'Hosp.Resp.Cases',
                    'ecmoCases', 'new_in.Hosp.Cases', 'new_out.Hosp.Cases']
    dfBE_Regions['RegionType'] = "Region"
    dfBE_Regions = dfBE_Regions.melt(id_vars=['Date', 'RegionType', 'Region'])
    # 2. By province
    dfBE_Hosp_Provs = dfBE_Hosp.groupby(['DATE', 'PROVINCE'], as_index=False).sum()
    dfBE_Hosp_Provs.columns = ['Date', 'Region', 'reportingHospitals', 'Hosp.Cases', 'IC.Cases',
                            'Hosp.Resp.Cases', 'ecmoCases', 'new_in.Hosp.Cases', 'new_out.Hosp.Cases']
    dfBE_Hosp_Provs['RegionType'] = "Province"
    dfBE_Hosp_Provs = dfBE_Hosp_Provs.melt(id_vars=['Date', 'RegionType', 'Region'])
    # Put files together
    dfBE = dfBE_Hosp_Provs.append(dfBE_Regions)
    dfBE['Country'] = "BE"

    return dfBE

dfBE = editDataBE()