#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# Ender3V2 422-427 Configurations generator script for the Professional Firmware
# For Marlin #13 (3950) temperature sensor 
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3V2-422-BLTUBL-T13', ['Ender3V2','422','BLT','UBL','T13'])
CreateConfigs.Generate('Ender3V2-427-BLTUBL-T13', ['Ender3V2','427','BLT','UBL','T13'])
