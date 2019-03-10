class Person:
    __name = 'n/a'
    __age = 0
    __address = 'n/a'

    def set_name(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def age(self):
        return self.__age

    def set_address(self, address):
        self.__address = address

    def address(self):
        return self.__address

    def description_of_person(self):
        print('---------------')
        print('/ Hi my name is', self.__name)
        print('/ I am', self.__age,' years old')
        print('/ My address is', self.__address)