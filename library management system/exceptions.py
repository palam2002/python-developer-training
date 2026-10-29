
class LibraryError(Exception):
    pass


class NotFoundError(LibraryError):
    pass


class ValidationError(LibraryError):
    pass


class OperationError(LibraryError):
    pass
