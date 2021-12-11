# Marlin_Configurations
In this repository there are the configuration files for several Marlin firmware features for the Ender3v2 printer

For have a special build you must to provide a config json with only your personal choices, for example: for get a
special build that have a hotend volcano, bltouch and 4.2.2 board it is necessary only write a Volcano.json with this content:

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

Then, request to the `CreateConfigs.py` to build a configuration with Generate(['422','BLTouch','Volcano'])`; the last "Volcano" will overwrite the necessary values in the configuration file.
