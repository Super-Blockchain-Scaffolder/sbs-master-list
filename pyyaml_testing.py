import yaml, json
from yaml import Loader
# document = open("bss-master-list.yaml", "r").read()
# print(json.dumps(yaml.load(document, Loader=Loader), indent=2))

def typeChecker(value,typeExpected):
    if(type(value) is not typeExpected or value==None):
        return False
    return True

class myYAMLParser:
    def __init__(self):
        self.fileRawData = ""
        self.fileDictionary = {}
        pass

    def readYamlFile(self):
        fileDictionary = yaml.load(self.fileRawData, Loader=Loader)
        # print(json.dumps(fileDictionary, indent=2))
        self.fileDictionary = fileDictionary

    def __validateSchemaOfStarter(self,starterData):
        try:
            for key,value in starterData.items():
                
                match key:
                    case "name":
                        if(typeChecker(value,str)==False):
                            raise Exception("name is not a string")
                    case"repo-url":
                        if(typeChecker(value,str)==False):
                            raise Exception("repo-url is not a string")
                    case"live-url":
                        if(typeChecker(value,str)==False):
                            raise Exception("live-url is not a string")
                    case"description":
                        if(typeChecker(value,str)==False):
                            raise Exception("description is not a string")
                    case"maintainers":
                        if(typeChecker(value,list)==False):
                            raise Exception("maintainers is not a list")
                    case"tags":
                        if(typeChecker(value,list)==False):
                            raise Exception("tags is not a list")
            return True
        except Exception as error:
            Exception("Error ${error} for starter ${stateData}")
            return False
    
    def validateSchema(self):
        try:
            for key,value in self.fileDictionary.items():
                match key:
                    case "name":
                        if(typeChecker(value,str)==False):
                            raise Exception("name is not a string")
                    case "starter-templates":
                        if(typeChecker(value,list)==False):
                            raise Exception("starter templates is not a list")
                        else:
                            for starter in value:
                                if(self.__validateSchemaOfStarter(starter)==False):
                                    raise Exception("starter template is not valid for the starter: {starter}")
                    case other:
                        print(";",key,";")
                        raise Exception("Incorrect syntax for the starter template")
            return True
        except Exception as error:
            print(error)
            Exception("Error ${error}")
            return False

yamlParser = myYAMLParser()

fileRawData = open("bss-master-list.yaml", "r").read()
yamlParser.fileRawData = fileRawData
yamlParser.readYamlFile()

print()
print("-----File dictionary data:------")
print(yamlParser.fileDictionary)

print()
print("-----Checking the file:------")
results = yamlParser.validateSchema()
print(results)
