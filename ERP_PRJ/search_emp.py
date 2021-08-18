from employee import employees
def search_menu():
    print("\tpress 1 for Search by Name")
    print("\tpress 2 for Search by Age")
    print("\tpress 3 for Search by Salary")
    print("\tpress 4 for Search by Gender")
    print("\tpress 5 for exit")


def search_emp_fn():
    while True:
        search_menu()
        ch = int(input("\tEnter the choice : "))
        li = []
        if ch == 1:
            n = input("\tEnter the name to search : ")
            li = list(filter(lambda a: a.name == n, employees))
        elif ch == 2:
            age = int(input("\tEnter the age to search : "))
            li = list(filter(lambda a: a.age == age, employees))
        elif ch == 3:
            s = int(input("\tEnter the salary to search : "))
            li = list(filter(lambda a: a.salary == s, employees))
        elif ch == 4:
            g = input("\tEnter the gender to search : ")
            li = list(filter(lambda a: a.gender == g, employees))
        elif ch == 5:
            break
        else:
            print("Invalid choice")
        if li:
            print("\t\t______________Employee Details_______________")
            for i in li:
                print(f"\t\tName - {i.name}")
                print(f"\t\tAge - {i.age}")
                print(f"\t\tGender - {i.gender}")
                print(f"\t\tPlace - {i.place}")
                print(f"\t\tSalary - {i.salary}")
                print(f"\t\tPrevious Company - {i.previous_company}")
                print(f"\t\tJoining Date - {i.joining_date}")
                print("\t\t_________________________________________________")

