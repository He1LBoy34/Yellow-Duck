from Person import Person


class House:

    __address = 'n/a'
    __list_of_residents = ['n/a']

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
        print('')