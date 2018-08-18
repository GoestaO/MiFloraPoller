import os, yaml

CURDIR = os.path.dirname(__file__)


def load_yaml(file):
    with open(file) as f:
        return yaml.load(f)

configuration = load_yaml("{}/{}".format(CURDIR, "config.yaml"))

