class DatabaseConnectionError(Exception):
    def __init__(self,msg="Database Connection Error"):
        self.msg=msg