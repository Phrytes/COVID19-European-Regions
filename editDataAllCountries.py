# TODO
# add Denmark, Portugal, Austria

import pandas as pd
from importlib import reload
import matplotlib
import matplotlib.pyplot as plt
# import own files
import editDataFrance
import editDataItaly
import editDataNetherlands
import editDataSwitzerland
import editDataUnitedKingdom
import editDataGermany
import editDataSpain
import editDataBelgium

matplotlib.use('TkAgg')

def reloadEditDataFiles():
    reload(editDataFrance)
    reload(editDataItaly)
    reload(editDataNetherlands)
    reload(editDataSwitzerland)
    reload(editDataUnitedKingdom)
    reload(editDataGermany)
    reload(editDataSpain)
    reload(editDataBelgium)

def editDataALL():
    reloadEditDataFiles()
    allDataFrames = []
    dfFR = editDataFrance.editDataFR()
    dfIT = editDataItaly.editDataIT()
    dfNL = editDataNetherlands.editDataNL()
    dfCH = editDataSwitzerland.editDataCH()
    dfUK = editDataUnitedKingdom.editDataUK()
    dfDE = editDataGermany.editDataDE()
    dfES = editDataSpain.editDataES()
    dfBE = editDataBelgium.editDataBE()

    allDataFrames.append(dfFR)
    allDataFrames.append(dfIT)
    allDataFrames.append(dfNL)
    allDataFrames.append(dfCH)
    allDataFrames.append(dfUK)
    allDataFrames.append(dfDE)
    allDataFrames.append(dfES)
    allDataFrames.append(dfBE)

    combined_df = pd.concat(allDataFrames, ignore_index=True, sort=True)
    return combined_df

countryCodes = ['BE', 'FR', 'DE', 'IT', 'NL', 'ES', 'CH', 'UK']

combined_df = editDataALL()
outputLoc = ".\\"
outputFileName = outputLoc + 'Covid19_ALL_countries.csv'
combined_df.to_csv(outputFileName, sep=',', encoding='utf-8', index=False)