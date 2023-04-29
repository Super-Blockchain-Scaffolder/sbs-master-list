# bss-master-list
The master list of starter templates for the Blockchain Super Scaffolder

<br/>

## Updating The List
Want to add your own awesoem project as a starter for the bss cli tool? Well lucky for you, it's easy!

Just update the `bss-master-list.yaml` file in this repository with the necessary information, and that's all there is to it!

## Validating The Yaml
We use specifically the [StrictYAML]() flavor of yaml. When you open a pull request CI jobs should automatically kick off to validate that the yaml file with your edits is still valid StrictYAML syntax.

You can run this validation locally by running the python file:
```bash
python3 validate-master-list-strict-yaml.py
```