#!/usr/bin/env python

# Verifies that the the yaml file is valid StrictYAML syntax

from strictyaml import load, Map, Str, Int, Seq, YAMLError, Optional
# import yaml

schema = Map({"a": Int() })

f = open("bss-master-list.yaml", "r")
try:
    person = load(f.read(), schema)
    # person = load(f.read())
    print(person.as_yaml())
except YAMLError as error:
    print(error)

