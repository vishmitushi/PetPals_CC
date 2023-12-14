from PetPals.dao.petdao import Petdao
from PetPals.dao.donationdao import donation_dao
from PetPals.dao.eventdao import EventDAO
from PetPals.Exception.DatabaseConnectionError import DatabaseConnectionError

class MainModule:
    def __init__(self):
        self.pet_dao = Petdao()
        self.donation_dao = donation_dao()
        self.event_dao = EventDAO()

    def display_menu(self):
        print("PetPals - Main Menu")
        print("1. Display Available Pets")
        print("2. Record Cash Donation")
        print("3. Record Item Donation")
        print("4. Display Upcoming Adoption Events")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    self.pet_dao.open()
                    available_pets = self.pet_dao.get_available_pets()
                    for pet in available_pets:
                        print(pet)
                except DatabaseConnectionError as e:
                    print(f"Error: {e}")

            elif choice == "2":
                donor_name = input("Enter donor name: ")
                amount = float(input("Enter donation amount: "))
                donation_date = input("Enter donation date (YYYY-MM-DD): ")

                try:
                    self.donation_dao.connect_to_database()
                    self.donation_dao.record_cash_donation(donor_name, amount, donation_date)
                    print("Cash donation recorded successfully!")
                except DatabaseConnectionError as e:
                    print(f"Error: {e}")

            elif choice == "3":
                donor_name = input("Enter donor name: ")
                amount = float(input("Enter donation amount: "))
                item_type = input("Enter item type: ")

                try:
                    self.donation_dao.connect_to_database()
                    self.donation_dao.record_item_donation(donor_name, amount, item_type)
                    print("Item donation recorded successfully!")
                except DatabaseConnectionError as e:
                    print(f"Error: {e}")

            elif choice == "4":
                try:
                    self.event_dao.connect_to_database()
                    upcoming_events = self.event_dao.get_upcoming_events()
                    for event in upcoming_events:
                        print(event)
                except DatabaseConnectionError as e:
                    print(f"Error: {e}")

            elif choice == "5":
                print("Exiting PetPals. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()