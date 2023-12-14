class FileException(Exception):
    def __init__(self,msg="file is not found or cannot be read."):
        self.msg=msg