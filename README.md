# Special Configurations
In this repository there are the configuration files for several Marlin firmware features for the Ender3 V2/S1 printer, the main
project files are in the firmware repository: https://github.com/mriscoc/Ender3V2S1

#### These special configurations and releases are sponsored by donors.

## How to request a custom build
Please check the suscription levels on [Patreon](https://www.patreon.com/mriscoc), there are levels that allow to request custom compile. Patrons from [Patreon platform](https://www.patreon.com/mriscoc) can request a configuration sending a message. If you made a equivalent donation through [Paypal](https://www.paypal.com/donate/?business=85SPAAR6UZEE8&currency_code=USD), please reply the message that I sent you or use any of the other communication media (Facebook, Telegram) providing the name used in Paypal. I'm happy and grateful for the contributions but please don't confuse that with paid work. I do what is possible in my little free time, be aware that a donation does not give you the right more than my thanks, a specialized job like coding and compiling a custom firmware could be a work quoted in 3 digits. Github also have a [Sponsor platform](https://github.com/sponsors/mriscoc).

## Contributions
Thank you for your support, I receive donations through [Patreon](https://www.patreon.com/mriscoc) and [Paypal](https://www.paypal.com/paypalme/mriscoc)   

[<img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif">](https://www.paypal.com/donate?business=85SPAAR6UZEE8&currency_code=USD)

## Creating your own custom configuration
It is now possible to use an small Python GUI interface (Professional Firmware **Configurator**) for generate the configuration files,
after downloading the repository execute the Python file `Configurator.pyw`:

![image](https://github.com/mriscoc/Special_Configurations/raw/main/images/Configurator.png)

> On Windows, `.pyw` files should be opened by pythonw.exe by default.

Select the printer, board, leveling, thermistor (Ender's stock thermistor is T1), features and press the `set config` button; write a name for the configuration
or press `Auto` button for fill the name automatically, that name will be used as a folder for storage the configuration
files and also as a custom printer name in the firmware, then press the `Generate` button to start the creation of the configuration files. You can open the `.json`
files in _printers, _boards, _features, etc. folders to know how each option in the Configurator works.

| Board  |https://github.com/mriscoc/Ender3V2S1/wiki|
| -------- | ------- |
| 301F1 | Ender 3 S1 STM32F103 SoC mainboard |
| 301F4 | Ender 3 S1 STM32F401 SoC mainboard |
|422 | Creality Board v4.2.2 |
|423 | Creality Board v4.2.3 |
|427 | Creality Board v4.2.7 |
|G32 | Voxelab Aquila |
|SKRME3V3 | BTT SKR Mini E3 V3 |

| Leveling  ||
| -------- | ------- |
| AutoLev | AutoLev from Substancia3D |
| BLT | BLTouch |
| EZABLZI | EZABL from TH3DStudio, endstop low |
| EZABLZN | EZABL from TH3DStudio, endstop high |
| MM | Manual Mesh without probe |
| UBL | Unified Bed Leveling |

| Display  |https://github.com/mriscoc/Ender3V2S1/wiki/How-to-update-the-display|
| -------- | ------- |
||Identify the display that happpened to be included in your printer. 

| Thermistor  ||
| -------- | ------- |
| T1 | Ender's stock thermistor |
| T11 | Generic NTC 100K 3950 up to 300 Celcius |
| T13 | 100k Hisens 3950 1% up to 300 Celcius |
| T20 | PT100 type 20 thermistor |
| T5 | Volcano thermistor |

| Features  ||
| -------- | ------- |
| CVLM | Enable the Laser Feature |
| HomeOffs | Disable NO_WORKSPACE_OFFSETS https://github.com/mriscoc/Ender3V2S1/wiki/How-to-set-the-home-offsets|
| IS | Input Shaping|
| LA | Linear Advance |
| MPC | Model Predictive Temperature Control |
| NP | NeoPixel |
| Speake | Enable the speaker |

### Compiling your firmware flavor
From the created custom configuration folder, move Configuration.h and Configuration_adv.h files to the Marlin folder inside of your project folder downloaded from the repository https://github.com/mriscoc/Ender3V2S1; move the platform.io file to the root of your project folder.
Keep your path short, the compiling tools don't like large paths.

Follow any guide about Marlin compile to get your firmware binary: Install [VSCode](https://code.visualstudio.com/), then inside of VSCode install the extensions: [PlatformIO](https://platformio.org/install/ide?install=vscode) and [Auto Build Marlin](https://marlinfw.org/docs/basics/auto_build_marlin.html). Open your project folder in VSCode and compile by using Auto Build Marlin. Remember: RE -> RET6 with 512 kB flash, RC-> RCT6 with 256 kB flash, do not use xfer and maple is a deprecated framework for some incompatible STM clones.

### Custom features
Advanced user can create a custom configuration calling directly the `CreateConfigs.py` Python script with the following parameters:

```Python
CreateConfigs.Generate('CustomConfigName', ['Printer','Board','Features',...])
```
To create Ender3V2 Configuration files with a BLTouch and UBL support it is easy to write a little Python script to call the above function:

```Python
#!/usr/bin/python
import CreateConfigs
CreateConfigs.Generate('Ender3V2-422-BLTUBL', ['Ender3V2','422','BLT','UBL'])
```

For have a special build you can provide a config json with only your personal choices, for example: for get a
special build for a Ender3V2 printer that have a hotend volcano, bltouch and 4.2.2 board it is necessary only write a Volcano.json with this content:

```json
{
"Configuration_adv.h" : [
],
"Configuration.h" : [
  {
    "op": "CustomVal",
    "searchfor": "TEMP_SENSOR_0",
    "value": "5",
    "comment": "Volcano thermistor"
  },
  {
    "op": "CustomVal",
    "searchfor": "HEATER_0_MINTEMP",
    "value": "5",
    "comment": "Volcano thermistor"
  },
  {
    "op": "CustomVal",
    "searchfor": "HEATER_0_MAXTEMP",
    "value": "300",
    "comment": "Volcano thermistor"
  }
],
"Version.h" : [
]   
}
```

Put the Volcano.json file inside of the `_features` folder, then request to the `CreateConfigs.py` to build a configuration with `CreateConfigs.Generate('MyCustomConfigName', ['Ender3V2','422','BLT','Volcano'])`; the last "Volcano" will overwrite the necessary
values in the configuration file, you can also use the GUI, your custom .json file will be listed as a custom feature.

For write your json file take note that the `CreateConfigs.py` script supports these basic operations over the configuration files:

> **InsertAfter**: allows to insert text after match a given mask.  
> **Custom**: allows to replace text  after match a given mask.  
> **CustomVal**: allows to replace simple (numeric, booleans, etc.) values.  
> **Enable**: allows to enable a feature.  
> **Disable**: allows to disable a feature.  
> **Replace**: allows to replace a mask with other text.

For example to change the default tramming points you can write in the "Configuration_adv.h" section of the json the command:
```json
  {
    "op": "Custom",
    "searchfor": "TRAMMING_POINT_XY",
    "mask": "{.*}",
    "value":"{ { 29, 29 }, { 299, 29 }, { 299, 299 }, { 29, 299 } }"
  }
```

For disable Multiple probing you can write in the "Configuration.h" section of the json the command:
```json
  {
    "op": "Disable",
    "searchfor": "MULTIPLE_PROBING",
    "comment": "Custom disable"
  }
```
The comment line is optional. Masks are in regex format, use the provided json as examples.

## Debugging Configurator errors with IDLE
If the Configurator doesn't open, load it into the IDLE Python editor and run from there, the possible error will be displayed in the IDLE Shell.

![idle1](https://github.com/mriscoc/Special_Configurations/raw/main/images/idle_1.jpg)  
![idle2](https://github.com/mriscoc/Special_Configurations/raw/main/images/idle_2.jpg)  
![idle3](https://github.com/mriscoc/Special_Configurations/raw/main/images/idle_3.jpg)  

# Disclaimer
THIS FIRMWARE AND ALL OTHER FILES IN THE DOWNLOAD ARE PROVIDED FREE OF CHARGE WITH NO WARRANTY OR GUARANTEE. SUPPORT IS NOT INCLUDED JUST BECAUSE YOU DOWNLOADED THE FIRMWARE. WE ARE NOT LIABLE FOR ANY DAMAGE TO YOUR PRINTER, PERSON, OR ANY OTHER PROPERTY DUE TO USE OF THIS FIRMWARE. IF YOU DO NOT AGREE TO THESE TERMS THEN DO NOT USE THE FIRMWARE.

# LICENSE
For the license, check the header of each file, if the license is not specified there, the project license will be used. Marlin is licensed under the GPL.
