from Person import Person
from House import House

person1 = Person('Mike', 34)
person2 = Person('John', 24)
person3 = Person('Den', 27)
house = House('1street')


house.settle_person(person1)
house.settle_person(person2)

person1.description_of_person()
person2.description_of_person()

house.description_of_house()

person1.test_class()
person2.test_static()