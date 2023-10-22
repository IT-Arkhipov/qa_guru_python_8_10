from dataclasses import dataclass


@dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


user = User(
    full_name='Elmo Lindgren',
    email='elmo@lindgren.us',
    current_address='314 W Vine St',
    permanent_address='4566 Lauren Drive'
)
