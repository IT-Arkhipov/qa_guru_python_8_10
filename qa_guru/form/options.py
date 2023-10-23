from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


gender = Gender
hobby = Hobby

