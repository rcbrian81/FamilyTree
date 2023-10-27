class Family:
    def __init__(self,father,mother):
        self.hash = father+mother
        self.mother = mother
        self.father = father
        self.children = {}

        self.mother.lower = self.hash
        self.father.lower = self.hash
    
    def addChildren(self,child):
        if child.upper:
            print("ERROR: Child is already part of family:" + child.upper)
            return False
        
        self.children[child.hash] = child.hash
        child.upper = self.hash
    def getJsonObj(self):
        jsonObj = {
            'key':self.hash,
            'Father':self.father,
            'Mother':self.mother,
            'Children': self.children
        }




"""
family json
{
    hash:sdfasdcawef
    Father: father's hash
    Mother: mother's hash
    children: {child1'hash:child1'hash, child2'hash:child2'hash}
}

family_data.json 
family hash: {
    hash:sdfasdcawef
    Father: father's hash
    Mother: mother's hash
    children: {child1'hash:child1'hash, child2'hash:child2'hash}
}
"""