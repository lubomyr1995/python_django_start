from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])[^\s]{8,20}$',
        [
            'password must contain 1 number (0-9)',
            'password must contain 1 uppercase letter',
            'password must contain 1 lowercase letter',
            'password must contain 1 non-alpha numeric',
            'password min 8 max 20 ch'
        ]
    )

    NAME = (
        r'^[a-zA-Z]{2,50}$',
        'only letters min 2 max 50 ch'
    )

    PHONE = (
        r'^0\d{9}$',
        'invalid phone number Ex. 0945123412'
    )
    BRAND = (
        r'^[a-zA-Z]{2,50}$',
        'min2 max 50'
    )

    def __init__(self, pattern: str, message: str | list[str]):
        self.pattern = pattern
        self.message = message
