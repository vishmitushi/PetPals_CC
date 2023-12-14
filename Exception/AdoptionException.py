class AdoptionException(Exception):
    def __init__(self,msg="No such pet available"):
        self.msg=msg