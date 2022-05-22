#!/usr/bin/python

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Ender3S1 with All Metal with 3950 Thermistor Type #13 upto 300°C
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3S1-F1-UBL-AM3950', ['S1F1','UBL','AM3950T13'])
CreateConfigs.Generate('Ender3S1-F4-UBL-AM3950', ['S1F4','UBL','AM3950T13'])

