import json
class Person:
    def __init__(self,name,hash):
        self.hash = hash

        self.name = name
        self.upper = None
        self.lower = None
        self.dob = None

        
        jsonObj = {
            'key':self.hash,
            'name':self.name,
            'upper':self.upper,
            'lower':self.lower,
            'dob': self.dob
        }

    def addUpper(self, upper):
        self.upper = upper
    def addLower(self, lower):
        self.lower = lower
    def getJsonObj(self):
        jsonObj = {
            'key':self.hash,
            'name':self.name,
            'upper':self.upper,
            'lower':self.lower,
            'dob': self.dob
        }
        return jsonObj
    def getJson(self):
        return json.dumps(self.getJsonObj(),indent=4)
        
    



















#prevent other programs or users from editing json file.
