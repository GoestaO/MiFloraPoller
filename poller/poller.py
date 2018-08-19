import yaml
import json
import sys, os
from configuration import configuration
from btlewrap.base import BluetoothBackendException
from btlewrap.gatttool import GatttoolBackend
from miflora.miflora_poller import MiFloraPoller, MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
from models import SensorData
from db import persist


def get_miflora_data(poller):
    d = dict()
    try:
        d['firmware'] = poller.firmware_version()
        d['name'] = poller.name()
        d['temperature'] = poller.parameter_value(MI_TEMPERATURE)
        d['moisture'] = poller.parameter_value(MI_MOISTURE)
        d['light'] = poller.parameter_value(MI_LIGHT)
        d['conductivity'] = poller.parameter_value(MI_CONDUCTIVITY)
        d['battery'] = poller.parameter_value(MI_BATTERY)
    except BluetoothBackendException as e:
        d['data'] = 'no data'
    return d


def map_sensor_data_entity(sensor_data):
    if not 'data' in sensor_data:
        p = SensorData(temperature=sensor_data['temperature'], moisture=sensor_data['moisture'],
                       fertility=sensor_data['conductivity'], light=sensor_data['light'], battery=sensor_data['battery'])
        return p
    return None

if __name__ == "__main__":
    sensors = configuration.get("sensors")
    for sensor in sensors:
        bluetooth_mac_address = sensor.get('bluetooth_mac_address')
        poller = MiFloraPoller(bluetooth_mac_address, GatttoolBackend)
        sensordata_raw = get_miflora_data(poller)
        print(sensordata_raw)
        sensordata_entity = map_sensor_data_entity(sensordata_raw)
        # sensordata_entity.sensor_name = poller
        # persist(sensordata_entity)


