import editDataFrance
import editDataItaly
import editDataNetherlands
import editDataSwitzerland
import editDataUnitedKingdom

from importlib import reload

#editDataFrance = reload(editDataFrance)
dfFR = editDataFrance.editDataFR()

editDataItaly.editDataIT()

#editDataNetherlands = reload(editDataNetherlands)
dfNL = editDataNetherlands.editDataNL()

editDataSwitzerland.editDataCH()

editDataUnitedKingdom.editDataUK()
