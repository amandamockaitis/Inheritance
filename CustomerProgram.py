import PersonClass as pc


def main():
    person = pc.Person("Amanda", "4830 Nolan Ridge", "832-341-0311")

    customer = pc.Customer("Amanda", "4830 Nolan Ridge", "832-341-0311", 458693, "True")

    print(person.print_person())

    print(customer.print_person())


main()
