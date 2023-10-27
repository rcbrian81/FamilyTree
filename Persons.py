import json
import hashlib
import os

filename = "data.json"
old_data = {}
newPersons = []

if not os.path.exists(filename):
    print("data.json file had to be create because it didn't exits!!!")
    with open(filename, "w") as file:
        file.close()

os.chmod(filename, 0o644) 

try:
    with open(filename, "r") as json_file:
        old_data = json.load(json_file)
        print("Json Data already existed")
        print(old_data)
        
except json.JSONDecodeError:
    old_data = {}
    print("No previous Json Data!!!")

print(old_data)


class Person:
    def __init__(self,name):
        self.hash = hashlib.sha256(name.encode('utf-8')).hexdigest()

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
    

def newPerson(name):
    name = name.lower()
    hash = key(name)
    if hash in old_data:
        print('failed to make add person:' + name + " already exists")
        return False
    
    
    newPerson = Person(name)
    old_data[hash] = newPerson.getJsonObj()

    print("Successfuly added new person: " + name)
    return newPerson

def key(str):
    return hashlib.sha256(str.encode('utf-8')).hexdigest()

def endProgram():
    with open("data.json","w") as file:
        json.dump(old_data,file, indent=4)
        file.close()

    os.chmod(filename, 0o444)
    print("end program.")




dad = newPerson("Jose Munoz")
dadx = newPerson("jose munoz")
mom = newPerson("Alba blanca")
son = newPerson("Santi Gimenez")









endProgram()
#prevent other programs or users from editing json file.
