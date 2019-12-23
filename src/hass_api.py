import asyncio
import json
from requests import get, post, Request
import config
from entities import Entity, DeviceType


def getHeaders():
    return {
        'Authorization': 'Bearer ' + config.ACCESS_TOKEN,
        'content-type': 'application/json',
    }


def getStates():
    url = config.SERVER_URL + '/api/states'

    response = get(url, headers=getHeaders()).json()
    print(response)
    print(len(str(response)))


def toggleEntity(entity: Entity):
    url = config.SERVER_URL + '/api/services/' + \
        entity.device_type.service_type+'/toggle'

    print('Toggling {"entity_id":"'+entity.entity_id+'"}')
    response = post(url, headers=getHeaders(),
                    data='{"entity_id":"'+entity.entity_id+'"}')

    print(response)
