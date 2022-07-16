#!/usr/bin/python

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Ender3S1 with Adafruit Neopixels NEO_GRB
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3S1-F1-NEOGRB', ['Ender3S1','301F1','BLT','UBL','NEOGRB'])
CreateConfigs.Generate('Ender3S1-F4-NEOGRB', ['Ender3S1','301F4','BLT','NEOGRB'])
