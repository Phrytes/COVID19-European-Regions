import pandas as pd
import editDataFrance
import editDataItaly
import editDataNetherlands
import editDataSwitzerland
import editDataUnitedKingdom
import editDataGermany
import editDataSpain

import geopandas as gp
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

allDataFrames = []

#from importlib import reload

#editDataFrance = reload(editDataFrance)
dfFR = editDataFrance.editDataFR()
allDataFrames.append(dfFR)

dfIT = editDataItaly.editDataIT()
allDataFrames.append(dfIT)

#editDataNetherlands = reload(editDataNetherlands)
dfNL = editDataNetherlands.editDataNL()
allDataFrames.append(dfNL)

editDataSwitzerland.editDataCH()

dfUK = editDataUnitedKingdom.editDataUK()
allDataFrames.append(dfUK)

dfDE = editDataGermany.editDataDE()
allDataFrames.append(dfDE)

dfES = editDataSpain.editDataES()
allDataFrames.append(dfES)

combined_df = pd.concat(allDataFrames, ignore_index=True, sort=True)
outputLoc = ".\\"
outputFileName = outputLoc + 'Covid19_ALL_countries.csv'
#combined_df.to_csv(outputFileName, sep=',', encoding='utf-8', index=False)

# Read geodata
# Source: https://ec.europa.eu/eurostat/cache/GISCO/distribution/v1/nuts-2016.html
#geoData1 = gp.read_file("..\\Data\\Sources\\Geodata\\NUTS_RG_20M_2016_4326_LEVL_1.shp\\NUTS_RG_20M_2016_4326_LEVL_1.shp", encoding='utf-8')
geoData2 = gp.read_file("..\\Data\\Sources\\Geodata\\NUTS_RG_20M_2016_4326_LEVL_2.shp\\NUTS_RG_20M_2016_4326_LEVL_2.shp", encoding='utf-8')
geoData3 = gp.read_file("..\\Data\\Sources\\Geodata\\NUTS_RG_20M_2016_4326_LEVL_3.shp\\NUTS_RG_20M_2016_4326_LEVL_3.shp", encoding='utf-8')
#geoData = geoData3.append(geoData2.append(geoData1))
geoData = geoData3.append(geoData2)
# Check records
geoData.head()
geoData['NUTS_NAME']

combinedGeo = pd.merge(geoData, combined_df, left_on="NUTS_NAME", right_on="Region")

test = combinedGeo.plot(figsize=(10,20), color='#3B3C6E')