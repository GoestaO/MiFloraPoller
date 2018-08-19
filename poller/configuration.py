import os, yaml
from pprint import pprint
CURDIR = os.path.dirname(__file__)


def load_yaml(file):
    with open(file) as f:
        return yaml.load(f)

configuration = load_yaml("{}/{}".format(CURDIR, "config.yaml"))

if __name__ == "__main__":
    # sensors = configuration.get("sensors")
    # for sensor in sensors:
    #     pprint(sensor.get('bluetooth_mac_address'))
    db = configuration.get("database")
    pprint(db)

