from PetPals.Entity.pet import pet
from PetPals.Exception import InvalidPetAge
from PetPals.Util.DBConnUtil import dbConnection
from PetPals.Exception.DatabaseConnectionError import DatabaseConnectionError

class Petdao(dbConnection):
    def __init__(self):
        self.name = ''
        self.age = ''
        self.breed = ''

    def connect_to_database(self):
        try:
            # Connect to the database using DBConnUtil
            self.connection = dbConnection.open()
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to the database") from e

    def get_available_pets(self):
        try:
            # Assuming 'pets' is the table name
            query = "SELECT * FROM pets"
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()

            # Convert rows to Pet objects
            available_pets = [pet(*row) for row in rows]
            return available_pets
        except Exception as e:
            raise DatabaseConnectionError("Error fetching available pets") from e
        finally:
            self.connection.close()

    def create(self):
        create_str='''create table if not exists Pet(
        pet_id int primary key auto_increment,
        name varchar(50),
        age int,
        breed varchar(50))'''
        self.open()
        self.stmt.execute(create_str)
        self.stmt.close()
        print('-----Table created successfully------:')

    def addPet(self):
        self.name = input('Enter Name :')
        self.age= int(input('Enter Age:'))
        if (self.age<0):
            try:
                raise InvalidPetAge()
            except InvalidPetAge as e:
                print(f'Error : {e}')
        self.breed = input('Enter Breed :')
        data=[(self.name,self.age, self.breed)]
        insert_str='''insert into Pet(name,age,breed) values(%s,%s,%s)'''
        self.open()
        self.stmt.executemany(insert_str,data)
        self.conn.commit()
        print('Records Inserted Successfully..')
        lastest_record = '''select pet_id from Pet ORDER BY pet_id DESC LIMIT 1'''
        self.stmt.execute(lastest_record)
        self.pet_id = self.stmt.fetchone()
        print(f'Pet ID : {self.pet_id } Name : {self.name} Age:{self.age} Breed:{self.breed}')
        self.close()

    def select(self):
        self.open()
        select_str='''select * from Pet'''
        self.stmt.execute(select_str)
        records=self.stmt.fetchall()
        print('')
        print('_________________Records In Pet Table________________________')
        for i in records:
            print(i)
        self.close()


    def delete(self):
        ID=input('Enter the Pet ID to be deleted:')
        delete_str=f'delete from Pet where pet_id={ID}'
        self.open()
        self.stmt.execute(delete_str)
        self.conn.commit()
        print('Records Deleted Successfully..')

    def __str__(self):
        return f'Name: {self.name} Age: {self.age} Breed: {self.breed}'