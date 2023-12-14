class InvalidPetAge(Exception):
    def __init__(self, msg ="Age must be positive integer."):
        super().__init__(msg)
        # self.msg = msg