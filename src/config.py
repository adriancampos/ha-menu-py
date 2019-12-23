import yaml
import os
import sys
from entities import Entity, DeviceType

ACCESS_TOKEN = None
SERVER_URL = None

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

TRAY_ICON_PATH = resource_path("assets/tray.ico")

# Load config from yaml
try:
    with open(r'hataskbar.yaml') as file:
        config = yaml.safe_load(file)

        SERVER_URL = config['desktop']['server_url']
        ACCESS_TOKEN = config['desktop']['access_token']
        if 'icon' in config['desktop']:
            TRAY_ICON_PATH = config['desktop']['icon_path']

        # Load entities
        entities = [Entity(entity['entity_id'], DeviceType.get_from_string(
            entity['device_type']), entity['name']) for entity in config['entities']]
except FileNotFoundError:
    print("hataskbar.yaml not found; creating one...")
    with open(r'hataskbar.yaml', 'w') as file:
        file.writelines([
            'desktop:\n',
            '    server_url: \n',
            '    access_token: \n',
            'entities:\n',
            '  # TODO: Eventually, I\'ll pull name and device_type from HA\n',
            '  - entity_id: light.desk_lamp\n',
            '    name: Desk Lamp\n',
            '    device_type: light\n',
            '  - entity_id: light.other_lamp\n',
            '    name: Other Lamp\n',
            '    device_type: light\n',
            ''
        ])
