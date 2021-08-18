from employee import employees
def change_data_choice():
    print("\tpress 1 for change Name")
    print("\tpress 2 for change Age")
    print("\tpress 3 for change Salary")
    print("\tpress 4 for change Gender")
    print("\tpress 5 for exit")


def change_emp_data():
    while True:

        change_data_choice()

        ch = int(input("\tEnter the choice : "))
        eid = int(input("\tEnter the Eployee Id : "))

        if ch == 1:
            for i in employees:
                if i.employee_id == eid:
                    i.set_name(input("\tEnter the new Name : "))
                    #employees[eid]["Name"] = input("\tEnter the new Name : ")
            # l = list(map(lambda a:a.employee_id ==))
        elif ch == 2:
            for i in employees:
                if i.employee_id == eid:
                    i.set_age(input("\tEnter the new Age : "))
                # employees[eid]["Age"] = input("\tEnter the new Age : ")
        elif ch == 3:
            for i in employees:
                if i.employee_id == eid:
                    i.set_salary(input("\tEnter the new Salary : "))
                # employees[eid]["Salary"] = input("\tEnter the new Salary : ")
        elif ch == 4:
            for i in employees:
                if i.employee_id == eid:
                    i.set_gender(input("\tEnter the new Gender : "))
                # employees[eid]["Gender"] = input("\tEnter the new Gender : ")
        elif ch == 5:
            break;
        else:
            print("Invalid Choice")

