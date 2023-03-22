# Config generator for the virtual vacuums

For the Yandex Alice, which don't know how to have vacuum clean specific room or spot, 
the virtual vacuums should be created and configured for each room.
In this case, the vacuum will be able to clean the room/zone from the Alice.

In order to use this plugin you need to add package to the Home Assistant configuration.yaml file:

```yaml
  packages:
    vac_automation: !include appdaemon/apps/vac_config/hass_config/config.yml
```
And configure app config:

```yaml
  config:
    kitchen_clean:
# The real vacuum ID. You can find it in the Developer Tools -> States 
      vac: vacuum.roborock_a15_a5ce_robot_cleaner
# The vacuum zone
      zone: [ 16514, 23173, 21371, 26402 ]
# Fan mode (not used now)      
      fan: silent
# Virtual vacuum ID. Please note, that all vacuums will be named as "Vacuum" for the Alice      
      name: "f1_kitchen_clean"
```