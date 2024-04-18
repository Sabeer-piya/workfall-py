from enum import Enum


class Role(str, Enum):
    ADMIN= "ADMIN"
    PARTNER= "PARTNER"
    CLIENT= "CLIENT"