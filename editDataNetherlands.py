import pandas
import os


def editDataNL():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    # 1. Hospitalized cases
    ## A. Municpilaties
    dfNL_Hosp = pandas.read_csv('../Data/Sources/NL/data/rivm_NL_covid19_hosp_municipality.csv')
    dfNL_Hosp.RegionType = "Municipality"
    # Load column names:
    colNames = pandas.read_csv('variableTable_ALL.csv', index_col="NL")[["Measure"]].to_dict()['Measure']
    dfNL_Hosp = dfNL_Hosp.rename(columns=colNames)
    dfNL_Hosp = dfNL_Hosp.rename(columns={"Aantal": "value"})
    dfNL_Hosp["variable"] = "New.Hosp.Cases"
    ## B. Provinces
    # Create dictionary of province names
    provincieCodes = {"Groningen": "PV20",
        "Friesland": "PV21",
        "Drenthe": "PV22",
        "Overijssel": "PV23",
        "Flevoland": "PV24",
        "Gelderland": "PV25",
        "Utrecht": "PV26",
        "Noord-Holland": "PV27",
        "Zuid-Holland": "PV28",
        "Zeeland": "PV29",
        "Noord-Brabant": "PV30",
        "Limburg": "PV31"
    }
    # Aggregate municipalities to provinces
    dfNL_Hosp_Provs = dfNL_Hosp.groupby(['Date', 'Provincienaam'], as_index=False).sum()
    dfNL_Hosp_Provs.RegionType = "Province"
    dfNL_Hosp_Provs = dfNL_Hosp_Provs.rename(columns={"Provincienaam": "Region"})
    # Add province codes
    dfNL_Hosp_Provs["RegionCode"] = pandas.Categorical(dfNL_Hosp_Provs['Region']) \
        .rename_categories(provincieCodes)
    # Combine municipality and province data into one dataframe
    dfNL_Hosp = dfNL_Hosp.drop("Provincienaam", axis=1)
    dfNL_Hosp = dfNL_Hosp.append(dfNL_Hosp_Provs)

    # 2. All cases (province only)
    dfNL_Cases = pandas.read_csv('../Data/Sources/NL/data/rivm_NL_covid19_province.csv')
    dfNL_Cases = dfNL_Cases.rename(columns={"Datum": "Date", "Provincienaam": "Region", "Aantal": "value"})
    dfNL_Cases["variable"] = "Cumul.Cases"
    dfNL_Cases["RegionCode"] = pandas.Categorical(dfNL_Cases['Region']).rename_categories(provincieCodes)
    # add everything to one dataframe
    dfNL = dfNL_Hosp.append(dfNL_Cases)
    dfNL['Country'] = 'NL'
    return dfNL

dfNL = editDataNL()

