
class FileErrors(Exception):
    pass

class FileNotFound(FileErrors):
    def __init__(self, message = None, response_code = None):
        self.message = message if message else "File not Found."
        self.response_code = 404 if response_code is None else response_code
        self.type = 'FileNotFound'