#!/usr/bin/env python

# Verifies that the the yaml file is valid StrictYAML syntax

# from strictyaml import load, Map, Str, Int, Seq, YAMLError, Optional
# # import yaml

# schema = Map({"a": Int() })

# f = open("bss-master-list.yaml", "r")
# try:
#     person = load(f.read(), schema)
#     # person = load(f.read())
#     print(person.as_yaml())
#     # print(person["name"])
# except YAMLError as error:
#     print(error)


# def readyaml():
#     with open("bss-master-list.yaml", "r") as stream:
#         try:
#             print(yaml.safe_load(stream))
#         except yaml.YAMLError as exc:
#             print(exc)

#import yaml reader
import yaml

# read a yaml file in python
def readYamlFile(filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)