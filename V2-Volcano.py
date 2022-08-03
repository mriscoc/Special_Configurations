#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Standard Volcano All Metal with thermistor #05 upto 300°C
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3V2-422-MM-Volc', ['Ender3V2','422','MM','T5'])
CreateConfigs.Generate('Ender3V2-427-MM-Volc', ['Ender3V2','427','MM','T5'])
CreateConfigs.Generate('Ender3V2-422-BLTUBL-Volc', ['Ender3V2','422','BLT','UBL','T5'])
CreateConfigs.Generate('Ender3V2-427-BLTUBL-Volc', ['Ender3V2','427','BLT','UBL','T5'])
