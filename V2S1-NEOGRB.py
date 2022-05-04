#!/usr/bin/python

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Adafruit Neopixels NEO_GRB
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3S1-NEOGRB', ['S1','NEOGRB'])
CreateConfigs.Generate('Ender3V2-422BLT-NEOGRB', ['422','BLTouch','NEOGRB'])
CreateConfigs.Generate('Ender3V2-427BLT-NEOGRB', ['427','BLTouch','NEOGRB'])
