#!/usr/bin/python

# ------------------------------------------------------------------------------
# Configurations generator for the Professional Firmware
# All Metal with PT100 #20 420°C
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3V2-422-MM-AMPT100', ['422','ManualMesh','AMPT100T20'])
CreateConfigs.Generate('Ender3V2-422-BLT-AMPT100', ['422','BLTouch','AMPT100T20'])
CreateConfigs.Generate('Ender3V2-427-MM-AMPT100', ['427','ManualMesh','AMPT100T20'])
CreateConfigs.Generate('Ender3V2-427-BLT-AMPT100', ['427','BLTouch','AMPT100T20'])

