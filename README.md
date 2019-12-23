# HA Taskbar

A taskbar app to toggle Home Assistant entities.  
Currently supports turning available switches, lights and input_boolean's on and off. 


## Installation
For now, there is no installation process. Run the executable directly from the download.

You can grab the latest executable from [Releases](https://github.com/adriancampos/ha-taskbar/releases). For now, I've only built a Windows binary. More to come in the future. For the time being, please build the project if you're on another platform. 


## Setup
For now, all configuration is done through `hataskbar.yaml`. To start, you'll need to include your **server url**, **long lived access token** and some **entities**.

### Token
To create a token within HA, login to HA and click on your profile.
Under Long Lived Access Tokens, create a new token, give it a name place this token into the config.


### Entities
Entity configuration should look similar to that of Home Assistant. Each entity should have a(n):
* entity_id. This needs to match your HA config exactly.
* name. This is currently required. In the future, it will be optional and override the name pulled from HA.
* device_type. This is also required. It will be pulled from HA in the future.

### Example config
```yaml
desktop:
    server_url: https://demo.home-assistant.io/
    access_token: long-lived-page-access-token-abcdef-123456
entities:
  - entity_id: light.led_strip
    name: LED Strip
    device_type: light
  - entity_id: light.desk
    name: Desk Lamp
    device_type: light
  - entity_id: light.ceiling
    name: Ceiling Lights
    device_type: light
  - entity_id: switch.plug01
    name: Christmas Tree
    device_type: switch
```

## Building

## TODO
- [ ] Support scenes
- [ ] Pull check states from HA
- [ ] Pull entity names and types from HA
- [ ] Error checking for config
- [ ] Fix onefile dist (we want tray.ico to be inside the package but configuration.yaml to be outside, for instance)
- [ ] Use websockets for HA connection?

## Credits
This project is inspired by an OSX version of the same thing: [HA Menu](https://github.com/andrew-codechimp/ha-menu). If you're on OSX, I encourage you to check it out!