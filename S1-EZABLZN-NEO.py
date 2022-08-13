#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# Ender3S1 Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3S1-F1-EZABLZN-NEO', ['Ender3S1','301F1','EZABLZN','NEO'])
CreateConfigs.Generate('Ender3S1-F1-EZABLZNUBL-NEO', ['Ender3S1','301F1','EZABLZN','UBL','NEO'])
CreateConfigs.Generate('Ender3S1-F4-EZABLZN-NEO', ['Ender3S1','301F4','EZABLZN','NEO'])

