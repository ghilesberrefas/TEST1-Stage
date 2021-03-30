import json
class MaClass :
    def upjson(self,bouton_ID) :
        jsonFile = open('test1/buttons.json', 'r') 
        data = json.load(jsonFile)
        jsonFile.close() 
        data[bouton_ID]['clicks']+=1
        ## Save our changes to JSON file
        jsonFile = open('test1/buttons.json', "w")
        jsonFile.write(json.dumps(data))
        jsonFile.close()
