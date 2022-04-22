#!/usr/bin/python

# ------------------------------------------------------------------------------
# Ender3V2 422-427 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3V2-422MM', ['422','ManualMesh'])
CreateConfigs.Generate('Ender3V2-422BLT', ['422','BLTouch'])
CreateConfigs.Generate('Ender3V2-427MM', ['427','ManualMesh'])
CreateConfigs.Generate('Ender3V2-427BLT', ['427','BLTouch'])
