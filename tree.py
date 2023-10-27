import Persons as p
import family as f
import os
import json
import hashlib

programActive = False

filename = "persons_data.json"
old_data = {}
newPersons = []

old_family_data = {}
newFamalies = []



def activateProgram():
    global programActive
    if not os.path.exists(filename):
        print(f"{filename} file had to be create because it didn't exits!!!")
    with open(filename, "w") as file:
        file.close()

    os.chmod(filename, 0o644) 

    try:
        with open(filename, "r") as json_file:
            old_data = json.load(json_file)
            print("Json Data already existed: ", len(old_data), "people")
            
    except json.JSONDecodeError:
        old_data = {}
        print("No previous Json Data!!!")
    programActive = True

def turnOffProgram():
    programActive = False

def newPerson(name):
    if programActive == False:
        print("Error: progarm has not been loaded into memory")
        return False
    name = name.lower()
    hash = key(name)
    if hash in old_data:
        print('failed to make add person:' + name + " already exists")
        return False
    
    
    newPerson = p.Person(name,hash)
    old_data[hash] = newPerson.getJsonObj()

    print("Successfuly added new person: " + name)
    return newPerson

def key(str):
    return hashlib.sha256(str.encode('utf-8')).hexdigest()

def storePersons():
    with open("data.json","w") as file:
        json.dump(old_data,file, indent=4)
        file.close()

    os.chmod(filename, 0o444)
    print("end program.")

def newFamily(father, mother):
    """
    #check if family already exist and deal with it.
    if father+mother in old_family_data:
        print("Error: Familty already exist")
        return False
    
    newFamily = f.Family(father,mother)
    old_family_data[father+mother] = newFamily.getJsonObj()
    print("Successfully made new familty: " , father, '-', mother)
    """
    
    
def addChildToFamily(child,family):
    print("need to add child")
    
     
activateProgram()
dad = newPerson("Jose Munoz")
dadx = newPerson("jose munoz")
mom = newPerson("Alba blanca")
son = newPerson("Santi Gimenez")

family = newFamily(dad.name, mom.name)
