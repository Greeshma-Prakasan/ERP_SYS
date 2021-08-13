employees = {}
teams = {}
def menu():
	print("enter 1 for Add Employee")
	print("enter 2 for Delete Employee")
	print("enter 3 for Search Employee by name")
	print("enter 4 for Change Employee Data")
	print("enter 5 for Display all Employees")
	print("enter 6 for Manage Teams")
	print("enter 7 for exit")
	
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

def search_emp():
	n = input("Enter the name to search : ")
	f = False
	for i in employees.values():
		if i["Name"] == n:
			print(f"\t{i['Name']} is found")
			f = True
			break
	if f == False:
		print("\tNot Found")
		
def change_data_choice():
	
	print("\tpress 1 for change Name")
	print("\tpress 2 for change Age")
	print("\tpress 3 for change Salary")
	print("\tpress 4 for change Gender")
	print("\tpress 5 for exit")

		
def change_emp_data():
	while True:
		eid  = int(input("Enter the Eployee Id : "))
		if eid in employees.keys():
		
			change_data_choice()
			
			ch = int(input("Enter the choice : "))

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


def manage_all_teams_menu():
	print("\t1.Create Teams")
	print("\t2.Display Teams")
	print("\t3.Manage Team(Particular)")
	print("\t4.Delete Team")
	print("\t5.Exit")

def manage_all_teams():
	while True:
		manage_all_teams_menu()
		ch = int(input("\tEnter your choice : "))
		if ch == 1:
			create_team()
		elif ch == 2:
			display_teams()
		elif ch == 3:
			manage_teams()
		elif ch == 4:
			delete_team()
		elif ch == 5:
			#exit
			break
		else:
			print("\tInvalid choice")
			
			
def create_team():
	team_name = input("\tEnter team name : ")
	teams[team_name] = []
	print(teams)

def delete_team():
	team_name = input("\tEnter team name : ")
	if team_name in teams.keys():
		del teams[team_name]
		print("\tDeleted the team")
	else:
		print("\tWrong team name")

def display_teams():
	for i,j in teams.items():
		name = ""
		for n in j:
			name = name+employees[n]["Name"]+", "
		print(f"\t{i} => {name}")

def manage_team_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.Display Members")
	

def manage_teams():
	team_name = input("\t\tEnter team name ")
	manage_team_menu()
	ch = int(input("\t\t Enter your Choice "))
	if ch == 1:
		add_member(team_name)
	elif ch == 2:
		delete_member(team_name)
	elif ch == 3:
		display_member(team_name)
	elif ch == 4:
		rename_member(team_name)
	else:
		print("\tInvalid choice")	
	
def add_member(team_name):
	display_emp()
	eid = int(input("\t\tEnter the Employee Id : "))
	if eid in employees.keys():
		teams[team_name].append(eid)
	else:
		print("\t\tWrong Employee Id")
	print(teams)
def display_member(team_name):

	name=""
	for i in teams[team_name]:
		name = name +str(i)+"."+employees[i]["Name"]+"|"
	print(f"{name}")

def delete_member(team_name):
	display_member(team_name)
	eid = int(input("\t\tEnter Employee Id from from list"))
	if eid in teams[team_name]:
		teams[team_name].remove(eid)
	else:
		print("\t\tWrong Employee Id")

#def rename_member(team_name):
	
	


while True:
	
	menu()
	c = int(input("enter the choice : "))

	if c==1:	
		add_employee()
	elif c==2:
		delete_emp()
	elif c==3:
		search_emp()	 
	elif c==4:
		change_emp_data()
	elif c==5:
		display_emp()       
	elif c==6:
		manage_all_teams()
	elif c==7:
		break
	else:
		print("invalid choice")

