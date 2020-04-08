from importlib import reload
import geopandas as gp
import pandas as pd
import matplotlib
import geoplot as gplt
from matplotlib import cm
# import own files
import editDataAllCountries
reload(editDataAllCountries)

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

countryCodes = ['BE', 'FR', 'DE', 'IT', 'NL', 'ES', 'CH', 'LI', 'UK']

# Read geodata
# Source: https://ec.europa.eu/eurostat/cache/GISCO/distribution/v1/nuts-2016.html
geoData1 = gp.read_file("..\\Data\\Sources\\Geodata\\NUTS_RG_20M_2016_4326_LEVL_1.shp\\NUTS_RG_20M_2016_4326_LEVL_1.shp", encoding='utf-8')
geoData1['NUTS'] = 1
geoData2 = gp.read_file("..\\Data\\Sources\\Geodata\\NUTS_RG_20M_2016_4326_LEVL_2.shp\\NUTS_RG_20M_2016_4326_LEVL_2.shp", encoding='utf-8')
geoData2['NUTS'] = 2
geoData3 = gp.read_file("..\\Data\\Sources\\Geodata\\NUTS_RG_20M_2016_4326_LEVL_3.shp\\NUTS_RG_20M_2016_4326_LEVL_3.shp", encoding='utf-8')
geoData3['NUTS'] = 3
geoData = geoData3.append(geoData2.append(geoData1))

# Make list of all NUTS-regions from all levels in Geodata
outputLoc = ".\\"
geoData['NUTS_NAME'][geoData['CNTR_CODE'].isin(countryCodes)]
outputFileNUTS = outputLoc + 'countrySelection_Geo.csv'
geoData[['CNTR_CODE', 'NUTS', 'NUTS_NAME']][geoData['CNTR_CODE'].isin(countryCodes)].drop_duplicates().to_csv(outputFileNUTS, sep=',', encoding='utf-8', index=False)
# Make list of all regions from all levels in regional data
combined_df = editDataAllCountries.editDataALL()
outputFileData = outputLoc + 'countrySelection_Data.csv'
combined_df[['Country', 'Region', 'RegionType']].drop_duplicates().to_csv(outputFileData, sep=',', encoding='utf-8', index=False)
# Combine by hand

# Read linking table
linkTable = pd.read_csv(".\\countriesLinkTable.csv")
# Combine with data
combinedLinked = pd.merge(combined_df, linkTable, left_on="Region", right_on="ORIGINAL_NAME")
combinedGeo = pd.merge(geoData, combinedLinked, left_on="NUTS_NAME", right_on="NUTS_NAME")
#test = combinedGeo[combinedGeo['variable']=='Cumul.Cases'].plot(figsize=(10,20), color='#3B3C6E')

#plot the data
combinedGeo[(combinedGeo['Date']=='2020-04-02') & (combinedGeo['variable']=='Cumul.Cases')].plot(column='value', legend=True)

gplt.choropleth(
    combinedGeo[(combinedGeo['Date']=='2020-03-30') & (combinedGeo['variable']=='Cumul.Cases')],
    hue='value',
    legend=True
)

gplt.choropleth(
    combinedGeo[(combinedGeo['Date']=='2020-03-30') & (combinedGeo['variable']=='Cumul.Deceas.Cases')],
    hue='value',
    legend=True
)