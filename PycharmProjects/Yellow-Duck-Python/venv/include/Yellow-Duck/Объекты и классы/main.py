from Person import Person
from House import House
from Programmer import *
from Driver import *

person1 = Driver('Mike', 34)
person2 = Programmer('John', 24)

house = House('1street')

person1.set_drive_exp(3)
person2.set_prog_exp(2)
house.settle_person(person1)
house.settle_person(person2)

person1.description_of_person()
person2.description_of_person()


house.description_of_house()

person1.test_class()
person2.test_static()