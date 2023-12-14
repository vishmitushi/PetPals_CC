from PetPals.Util.DBConnUtil import dbConnection
from PetPals.Exception.DatabaseConnectionError import DatabaseConnectionError

class EventDAO:
    def __init__(self):
        self.connection = None

    def connect_to_database(self):
        try:
            # Connect to the database using DBConnUtil
            self.connection = dbConnection.open()
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to the database") from e

    def get_upcoming_events(self):
        try:
            # Assuming 'adoption_events' is the table name
            query="SELECT * FROM adoption_events WHERE event_date > CURRENT_DATE"
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()

            # Convert rows to adoption event objects
            upcoming_events=[self._create_event_object(row) for row in rows]
            return upcoming_events
        except Exception as e:
            raise DatabaseConnectionError("Error fetching upcoming events") from e
        finally:
            self.connection.close()

    def _create_event_object(self, row):
        event={
            'event_name': row[0],
            'event_date': row[1],
            'location': row[2]
        }
        return event