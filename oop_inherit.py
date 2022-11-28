"""
Inherit / keturunan adalah sebuah class yang mewarisi method dan properties parent class

"""
# Parent class

class Orang:
    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname
    
    def printName(self):
        print(self.firstname,self.lastname)

# Inheritance

class Murid(Orang):
    pass

Denny = Murid("Denny","Mario")
Denny.printName()
