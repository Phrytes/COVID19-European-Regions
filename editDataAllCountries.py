import pandas as pd
import editDataFrance
import editDataItaly
import editDataNetherlands
import editDataSwitzerland
import editDataUnitedKingdom

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

combined_df = pd.concat(allDataFrames, ignore_index=True, sort=True)
outputLoc = ".\\"
outputFileName = outputLoc + 'Covid19_ALL_countries.csv'
combined_df.to_csv(outputFileName, sep=',', encoding='utf-8', index=False)
