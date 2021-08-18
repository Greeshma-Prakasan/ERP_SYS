employees = {}
def add_employee():
	eid = int(input("\tEnter the Employee id : "))
	n = input("\tEnter the name : ")
	a = int(input("\tEnter the age : "))
	g = input("\tEnter the gender : ")
	p = input("\tEnter the place : ")
	s = int(input("\tEnter the salary : "))
	pre = input("\tEnter the previous company : ")
	j = input("\tEnter the joining date : ") 
	if eid not in employees.keys():
		employees[eid] = {"Name":n,"Age":a,"Gender":g,"Place":p,"Salary":s,"Previous Company":pre,"Joining Date":j}

	else:
		print("\tEmployee id is already present")

def delete_emp():
	eid = int(input("Enter the Employee id : "))
	if (eid in employees.keys()):
		del employees[eid]
		print("Deleted Successfully")
	else:
		print("Employee id is incorrect")
		
def display_emp():

	if employees != None:
		print("____________Employee Details___________")
		for i,j in employees.items():
			print(f"{i} :\tName - {j['Name']}")
			print(f"\tAge - {j['Age']}")
			print(f"\tGender - {j['Gender']}")
			print(f"\tPlace - {j['Place']}")
			print(f"\tSalary - {j['Salary']}")
			print(f"\tPrevious Company - {j['Previous Company']}")
			print(f"\tJoining Date - {j['Joining Date']}")	


def change_data_choice():
	
	print("\tpress 1 for change Name")
	print("\tpress 2 for change Age")
	print("\tpress 3 for change Salary")
	print("\tpress 4 for change Gender")
	print("\tpress 5 for exit")
		
def change_emp_data():
	while True:
		
		if eid in employees.keys():
		
			change_data_choice()
			
			ch = int(input("\tEnter the choice : "))
			eid  = int(input("\tEnter the Eployee Id : "))

			if ch==1:
				employees[eid]["Name"] = input("\tEnter the new Name : ")
			elif ch==2:
				employees[eid]["Age"] = input("\tEnter the new Age : ")
			elif ch==3:
				employees[eid]["Salary"] = input("\tEnter the new Salary : ")
			elif ch==4:
				employees[eid]["Gender"] = input("\tEnter the new Gender : ")
			elif ch==5:
				break;
			else:
				print("Invalid Choice")
		else:
			print("\tEmployee Not Found")


def search_menu():
	print("\tpress 1 for Search by Name")
	print("\tpress 2 for Search by Age")
	print("\tpress 3 for Search by Salary")
	print("\tpress 4 for Search by Gender")
	print("\tpress 5 for exit")

def search_emp():
	while True:
		search_menu()
		ch = int(input("\tEnter the choice : "))
		li = []
		if ch == 1:
			n = input("\tEnter the name to search : ")
			li = list(filter(lambda a:a["Name"]==n,employees.values()))
		elif ch == 2:
			age = int(input("\tEnter the age to search : "))
			li = list(filter(lambda a:a["Age"]==age,employees.values()))
		elif ch == 3:
			s = int(input("\tEnter the salary to search : "))
			li = list(filter(lambda a:a["Salary"]==s,employees.values()))
		elif ch == 4:
			g = input("\tEnter the gender to search : ")
			li = list(filter(lambda a:a["Gender"]==g,employees.values()))
		elif ch ==5:
			break
		else:
			print("Invalid choice")
		if li:
			for i in li:
				print("\t\t______________Employee Details_______________")
				print(f"\t\tName - {i['Name']}")
				print(f"\t\tAge - {i['Age']}")
				print(f"\t\tGender - {i['Gender']}")
				print(f"\t\tPlace - {i['Place']}")
				print(f"\t\tSalary - {i['Salary']}")
				print(f"\t\tPrevious Company - {i['Previous Company']}")
				print(f"\t\tJoining Date - {i['Joining Date']}")
				print("\t\t_________________________________________________")
				
