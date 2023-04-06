from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = ({'details': 'Invalid oe expired token'}, status.HTTP_403_FORBIDDEN)

    def __init__(self, msg, status_code=status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.status_code = status_code
