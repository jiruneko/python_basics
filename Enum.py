from enum import Enum, auto


class Gender(Enum):
    male = auto()
    female = auto()
    others = auto()


print([Gender.male, Gender.female, Gender.others])

x = Gender.male
print(type(x))
