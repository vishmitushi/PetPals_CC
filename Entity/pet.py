from PetPals.Util.DBConnUtil import dbConnection

class pet(dbConnection):
    def __init__(self):
        super().__init__(self)
        self.name = ''
        self.age = ''
        self.breed = ''
