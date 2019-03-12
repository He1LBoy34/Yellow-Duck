from Person import Person

class Driver(Person):

    __drive_exp = 0

    def set_drive_exp(self, dxp):
        self.__drive_exp = dxp

    def drive_exp(self):
        return self.__drive_exp

    def description_of_person(self):
        super().description_of_person()
        print('/ I am driver and my experience ', self.__drive_exp, 'years')