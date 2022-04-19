#!/usr/bin/python

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Standard Volcano All Metal with thermistor #05 upto 300°C
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('Ender3V2-422MM-Volc', ['422','ManualMesh','Volcano'])
CreateConfigs.Generate('Ender3V2-422BLT-Volc', ['422','BLTouch','Volcano'])
CreateConfigs.Generate('Ender3V2-427MM-Volc', ['427','ManualMesh','Volcano'])
CreateConfigs.Generate('Ender3V2-427BLT-Volc', ['427','BLTouch','Volcano'])
CreateConfigs.Generate('Ender3V2-422BLTUBL-Volc', ['422','BLTouch','Volcano','UBL'])
CreateConfigs.Generate('Ender3V2-427BLTUBL-Volc', ['427','BLTouch','Volcano','UBL'])



