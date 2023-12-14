from PetPals.Util.DBConnUtil import dbConnection

class PetShelter(dbConnection):
    def __init__(self):
        self.availablePets = []

    def addPet(self, pet):
        self.availablePets.append(pet)

    def removePet(self, pet):
        self.availablePets.remove(pet)

    def ListAvailablePets(self):
            self.open()
            select_str = '''select * from Pet'''
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            print('')
            print('_________________Records In Pet Table________________________')
            for i in records:
                print(i)
            self.close()

