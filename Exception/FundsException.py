class FundsException(Exception):
    def __init__(self,msg="Donations can't be less than $10"):
        self.msg=msg