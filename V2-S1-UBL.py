#!/usr/bin/python

# ------------------------------------------------------------------------------
# Ender3V2 422-427 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3V2-422BLT-UBL', ['422','BLTouch','UBL'])
CreateConfigs.Generate('Ender3V2-427BLT-UBL', ['427','BLTouch','UBL'])
CreateConfigs.Generate('Ender3S1-UBL', ['S1','UBL'])
