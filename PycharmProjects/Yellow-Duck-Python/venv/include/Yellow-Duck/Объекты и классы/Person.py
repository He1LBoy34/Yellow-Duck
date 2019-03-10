class Person:
    __name = 'n/a'
    __age = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def description_of_person(self):
        print('---------------')
        print('/ Hi my name is', self.__name)
        print('/ I am', self.__age,' years old')