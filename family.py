class Family:
    def __init__(self,father,mother):
        self.hash = father+mother
        self.mother = mother
        self.father = father
        self.children = []

        self.mother.addFamilly(self)
        self.father.addFamilly(self)

    def addChildren(self,child):
        self.children.append(child)
        child.mother = self.mother
        child.father = child.father
    
    def getSummary(self):
        summary = f"Father: {self.father.name}-------{self.mother.name} :Mother\nChildren: "

        for child in self.children:
            summary = summary + child.name + ", "

        return summary[0:len(summary)-2] + "\n"




