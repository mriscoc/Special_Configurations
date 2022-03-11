#!/usr/bin/python

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Stock heat break with 3950 Thermistor Type #13
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('', ['422','BLTouch','AM3950T13'])
CreateConfigs.Generate('', ['427','BLTouch','AM3950T13'])


