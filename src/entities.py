from enum import Enum

class DeviceType (Enum):
    LIGHT = "light"
    SWITCH = "switch"
    INPUT_BOOLEAN = "input_boolean"

    def __new__(cls, service_type):
        obj = object.__new__(cls)
        obj._value_ = service_type
        obj.service_type = service_type
        return obj
    
    @staticmethod
    def get_from_string(string):
        for type in DeviceType:
            if type.service_type == string:
                return type


class Entity:
    def __init__(self, entity_id, device_type, name):
        self.entity_id = entity_id
        self.device_type = device_type
        self.name = name

