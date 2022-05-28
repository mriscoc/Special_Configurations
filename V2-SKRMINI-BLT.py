#!/usr/bin/python

# ------------------------------------------------------------------------------
# Ender3V2 SKR_MINI Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3V2-SKRMINI-MM', ['SKR_MINI','ManualMesh'])
CreateConfigs.Generate('Ender3V2-SKRMINI-BLT', ['SKR_MINI','BLTouch'])
CreateConfigs.Generate('Ender3V2-SKRMINI-BLTUBL', ['SKR_MINI','BLTouch','UBL'])
