from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item

import config
import hass_api
from entities import Entity, DeviceType

import webbrowser


# Set up tray icon
tray_icon = icon('Home Assistant')
tray_icon.icon = Image.open(config.TRAY_ICON_PATH)


# Set up menu items for each entity in config
entity_items = map(lambda entity: item(entity.name, lambda: hass_api.toggleEntity(entity), checked=lambda item: False), config.entities)


tray_icon.menu = menu(
    *entity_items,
    menu.SEPARATOR,
    item('Open Home Assistant', lambda: webbrowser.open(config.SERVER_URL)),
    menu.SEPARATOR,
    item('Quit', lambda:tray_icon.stop())
)

tray_icon.run()
