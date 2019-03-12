from Person import Person

class Programmer(Person):

    __prog_exp = 0

    def set_prog_exp(self, px):
        self.__prog_exp = px

    def prog_exp(self):
        return self.__prog_exp

    def description_of_person(self):
        super().description_of_person()
        print('/ I am programmer and my experience ', self.__prog_exp, 'years')