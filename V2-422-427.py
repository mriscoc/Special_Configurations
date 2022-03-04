#!/usr/bin/python

# ------------------------------------------------------------------------------
# Ender3V2 422-427 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('', ['422','ManualMesh'])
CreateConfigs.Generate('', ['422','BLTouch'])
CreateConfigs.Generate('', ['427','ManualMesh'])
CreateConfigs.Generate('', ['427','BLTouch'])
