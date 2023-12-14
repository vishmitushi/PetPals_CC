from PetPals.Entity.iadoptable import IAdoptable

class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def host_event(self):
        print("Hosting adoption event")

    def register_participant(self, participant):
        self.participants.append(participant)