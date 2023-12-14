class NullException(Exception):
    def __init__(self,msg="An entity can't have null value"):
        self.msg=msg