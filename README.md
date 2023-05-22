# sbs-master-list
The master list of starter templates for the Super Blockchain Scaffolder

<br/>

## Updating The List
Want to add your own awesoem project as a starter for the sbs cli tool? Well lucky for you, it's easy!

Just update the `sbs-master-list.yaml` file in this repository with the necessary information, and that's all there is to it!

## Validating The Yaml
We use specifically the [StrictYAML]() flavor of yaml. When you open a pull request CI jobs should automatically kick off to validate that the yaml file with your edits is still valid StrictYAML syntax.

You can run this validation locally by running the python file:
```bash
python3 validate-master-list-strict-yaml.py
```

## How to install?
Virtual environment is already setted up, just activate that by this command and you are good to go!
```
source sbs-master/bin/activate
```
Then you can just run this command:
```
python3 validate-master-list-strict-yaml.py
```

Note: you may also need to run this:
```bash
 python3 -m pip install strictyaml
 ```


 ### TODO

 - validate that git repo exists for new submissions

- validate that starters fit a schema