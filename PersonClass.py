import random


class Person:
    def __init__(self, name, address, number):
        self.__name = name
        self.__address = address
        self.__number = number

    def print_person(self):
        return self.__name, self.__address, self.__number


class Customer(Person):
    def __init__(self, name, address, number, custnum, maillist):
        Person.__init__(self, name, address, number)

        self.__custnum = custnum
        self.__maillist = maillist

    def print_person(self):
        return (
            self.__custnum,
            self.__maillist,
        )
