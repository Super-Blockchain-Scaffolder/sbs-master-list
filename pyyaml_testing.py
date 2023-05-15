import yaml, json
from yaml import Loader
document = open("bss-master-list.yaml", "r").read()
print(json.dumps(yaml.load(document, Loader=Loader), indent=2))
