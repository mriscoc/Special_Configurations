#!/usr/bin/python

# ------------------------------------------------------------------------------
# Standard Volcano Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('', ['422','ManualMesh','Volcano'])
CreateConfigs.Generate('', ['422','BLTouch','Volcano'])
CreateConfigs.Generate('', ['427','ManualMesh','Volcano'])
CreateConfigs.Generate('', ['427','BLTouch','Volcano'])


