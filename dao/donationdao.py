from PetPals.Util.DBConnUtil import dbConnection
from PetPals.Exception.DatabaseConnectionError import DatabaseConnectionError

class donation_dao(dbConnection):
    def __init__(self):
        self.connection = None

    def connect_to_database(self):
        try:
            self.connection=dbConnection.open()
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to the database") from e

    def record_cash_donation(self, donor_name, amount, donation_date):
        try:
            query="INSERT INTO cash_donations (donor_name, amount, donation_date) VALUES (%s, %s, %s)"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (donor_name, amount, donation_date))
            self.connection.commit()
        except Exception as e:
            raise DatabaseConnectionError("Error recording cash donation") from e
        finally:
            self.connection.close()

    def record_item_donation(self, donor_name, amount, item_type):
        try:
            # Assuming 'item_donations' is the table name
            query="INSERT INTO item_donations (donor_name, amount, item_type) VALUES (%s, %s, %s)"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (donor_name, amount, item_type))
            self.connection.commit()
        except Exception as e:
            raise DatabaseConnectionError("Error recording item donation") from e
        finally:
            self.connection.close()