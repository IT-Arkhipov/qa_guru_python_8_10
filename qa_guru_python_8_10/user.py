from dataclasses import dataclass


@dataclass
class User:
    first_name: str = 'FirstName'
    last_name: str = 'LastName'
