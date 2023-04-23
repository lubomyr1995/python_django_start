from datetime import timedelta
from enum import Enum


class ActionEnum(Enum):
    ACTIVATE = ('activate', timedelta(days=1))
    RECOVERY = ('recovery', timedelta(minutes=60))
    SOCKET = ('socket', timedelta(minutes=1))

    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime
