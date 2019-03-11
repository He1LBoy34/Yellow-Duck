from Person import *


class House:

    __address = 'n/a'
    __list_of_residents = ['n/a']

    def __init__(self, address):
        self.__address = address

    def set_address(self, address):
        self.__address = address

    def address(self):
        return self.__address

    def settle_person(self, settle):
        if isinstance(settle, Person):
            self.__list_of_residents.append(settle)
            settle.set_address(self.__address)

    def evict_person(self, evict):
        self.__list_of_residents.remove(evict)
        evict.set_address('n/a')

    def description_of_house(self):
        print('---------------------')
        print('Address of this house is', self.__address)
        print('# List of residents: ')
        for p in self.__list_of_residents:
            if isinstance(p, Person):
                print('# - ', p.name())