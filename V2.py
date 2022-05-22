#!/usr/bin/python

# ------------------------------------------------------------------------------
# Ender3V2 422-427 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3V2-422-MM', ['422','ManualMesh'])
CreateConfigs.Generate('Ender3V2-422-BLT', ['422','BLTouch'])
CreateConfigs.Generate('Ender3V2-423-MM', ['423','ManualMesh'])
CreateConfigs.Generate('Ender3V2-423-BLT', ['423','BLTouch'])
CreateConfigs.Generate('Ender3V2-427-MM', ['427','ManualMesh'])
CreateConfigs.Generate('Ender3V2-427-BLT', ['427','BLTouch'])
