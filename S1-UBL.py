#!/usr/bin/python

# ------------------------------------------------------------------------------
# Ender3V2 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3S1-F1-UBL', ['Ender3S1','301F1','BLT','UBL'])
CreateConfigs.Generate('Ender3S1-F4-UBL', ['Ender3S1','301F4','BLT','UBL','FreeFlash'])
