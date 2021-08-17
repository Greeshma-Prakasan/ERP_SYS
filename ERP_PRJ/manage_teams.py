import employee as emp
teams = {}
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
			name = name+emp.employees[n]["Name"]+", "
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
	emp.display_emp()
	eid = int(input("\t\tEnter the Employee Id : "))
	if eid in emp.employees.keys():
		teams[team_name].append(eid)
	else:
		print("\t\tWrong Employee Id")
	print(teams)
def display_member(team_name):

	name=""
	for i in teams[team_name]:
		name = name +str(i)+"."+emp.employees[i]["Name"]+"|"
	print(f"{name}")

def delete_member(team_name):
	display_member(team_name)
	eid = int(input("\t\tEnter Employee Id from from list : "))
	if eid in teams[team_name]:
		teams[team_name].remove(eid)
	else:
		print("\t\tWrong Employee Id")

#def rename_member(team_name):
	
	
