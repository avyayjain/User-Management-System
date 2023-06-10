

class DataBaseErrors(Exception):
    pass


class NoEntityFound(DataBaseErrors):
    def __init__(self, message = None, response_code = None):
        self.message = message if message else "No Entity associated to given data found."
        self.response_code = 404 if response_code is None else response_code
        self.type = 'NoEntityFound'

class UserErrors(Exception):
    def __init__(self, message=None, response_code=None):
        self.message = message if message else "Internal Server Error"
        self.response_code = response_code if response_code else 500
        self.type = "UserErrors"


class PermissionDeniedError(UserErrors):
    def __init__(self, message=None, response_code=None):
        self.message = message if message else "Could not validate credentials"
        self.response_code = response_code if response_code else 401
        self.type = "PermissionDeniedError"

class OpsUser(UserErrors):
    def __init__(self, message=None, response_code=None):
        self.message = message if message else "Ops User: Access Denied"
        self.response_code = response_code if response_code else 400
        self.type = "PermissionDeniedError"


class PayloadLargeError(UserErrors):
    def __init__(self, message=None, response_code=None):
        self.message = message if message else " Payload is too large to Process"
        self.response_code = response_code if response_code else 413
        self.type = "PayloadLargeError"


class PathError(UserErrors):
    def __init__(self, message=None, response_code=None):
        self.message = message if message else "S3 Path is incorrect"
        self.response_code = response_code if response_code else 400
        self.type = "PathError"


class S3ConnectionError(UserErrors):
    def __init__(self, message=None, response_code=None):
        self.message = message if message else "Try Again"
        self.response_code = response_code if response_code else 500
        self.type = "PathError"


class RoleNotFoundError(UserErrors):
    def __init__(self, message=None, response_code=None):
        self.message = message if message else "Try Again"
        self.response_code = response_code if response_code else 500
        self.type = "RoleNotFoundError"


class EditorAccessDeniedError(UserErrors):
    def __init__(self, message=None, response_code=None):
        self.message = message if message else "Access Denied"
        self.response_code = response_code if response_code else 400
        self.type = "Access denied"

#todo
# make error for no assignment
# fix for submit empty not allowed error (doubt)

