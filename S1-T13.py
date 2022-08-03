#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# Ender3S1 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3S1-F1-T13', ['Ender3S1','301F1','BLT','T13'])
CreateConfigs.Generate('Ender3S1-F1-UBL-T13', ['Ender3S1','301F1','BLT','UBL','T13'])
CreateConfigs.Generate('Ender3S1-F4-T13', ['Ender3S1','301F4','BLT','T13'])

