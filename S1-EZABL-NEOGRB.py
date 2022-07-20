#!/usr/bin/python

# ------------------------------------------------------------------------------
# Ender3S1 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3S1-F1-EZABL-NEO', ['Ender3S1','301F1','EZABLZN','NEOGRB'])
CreateConfigs.Generate('Ender3S1-F1-EZABLUBL-NEO', ['Ender3S1','301F1','EZABLZN','UBL','NEOGRB'])
CreateConfigs.Generate('Ender3S1-F4-EZABL-NEO', ['Ender3S1','301F4','EZABLZN','NEOGRB'])

