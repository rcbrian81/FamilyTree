import hashlib
import pickle

persons = {}
pckl_file_path = 'datafile.pkl'

try:
    with open(pckl_file_path, 'rb') as file:
        persons = pickle.load(file)
except EOFError:
    print("Pickle file is empty.")
except Exception as e:
    print(f"An error occurred: {e}")



def getHash(str):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(str.encode())
    return sha256_hash.hexdigest()

def person(name, DOB, father, mother):
	sha256_hash = hashlib.sha256()
	sha256_hash.update(name.encode())
	hash_result = sha256_hash.hexdigest()

	hash_result =getHash(name)

	if hash_result in persons:
		print(f"ERROR: Person already exist: {name}.")
		return "ERROR: Person already exist."

	newPerson = {
		'ID':hash_result,
		'name': name,
		'dob': DOB,
		'fatherID':father,
		'motherID':mother
	}


	print(f"New Person: {name}")
	persons[newPerson["ID"]] = newPerson
	return newPerson["ID"]

def getPerson(personID):
	if personID in persons:
		return persons[personID]
	else:
		print("ERORR: In getPersons().")
		return "ERORR: In getPersons()."
def getPersonID(name):
	key = getHash(name)
	print(key)
	if key in persons:
		return key
	print("ERROR: Person does NOT exist.")
	return "ERROR: Person does NOT exist."
def addFather(childID,fatherID):
	persons[childID].faher = fatherID

def getMotherID(childID):
	if childID in persons:
		return persons[childID]['motherID'] 
	else:
		return f"ERROR Person With {childID} NOT Found."
def getFatherID(childID):
	if childID in persons:
		return persons[childID]['fatherID'] 
	else:
		return f"ERROR Person With {childID} NOT Found."


def getChildren(parentID):
	print(parentID)
	children = []
	for key in persons:
		child = persons[key]
		if child["fatherID"] == parentID or child["motherID"] == parentID:
			children.append(child['ID'])

	return children

def printALL():
	print("ALL PEOPLE:")
	for key in persons:
		print(persons[key]['name'])






printALL()

with open('datafile.pkl', 'wb') as file:
    pickle.dump(persons, file)
