from enum import Enum


class RoleType(Enum):
    COMPANY_MEMBER = "Company Member"
    ADMIN = "Admins"
    
class WinnerType(Enum):
    WINNER = "Winner"
    PARTIAL_WINNER = "Partial Winner"
    NOT_WINNER = "Not Winner"