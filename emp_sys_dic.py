employees = {}

while True:
	print("enter 1 for Add Employee")
	print("enter 2 for Delete Employee")
	print("enter 3 for Search Employee by name")
	print("enter 4 for Change Employee Data")
	print("enter 5 for Display all Employees")
	print("enter 6 for exit")

	c = int(input("enter the choice : "))

	if c==1:
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

	elif c==2:
		eid = int(input("Enter the Employee id : "))
		if (eid in employees.keys()):
			del employees[eid]
		else:
			print("Employee id is incorrect")

	elif c==3:
		n = input("Enter the name to search : ")
		f = False
		for i in employees.values():
			if i["Name"] == n:
				print(f"\t{i['Name']} is found")
				f = True
				break
		if f == False:
			print("\tNot Found")
			 
	elif c==4:
		eid  = int(input("Enter the Eployee Id : "))
		if eid in employees.keys():

			print("\tpress 1 for change Name")
			print("\tpress 2 for change Age")
			print("\tpress 3 for change Salary")
			print("\tpress 4 for change Gender")
			ch = int(input("Enter the choice : "))

			if ch==1:
				employees[eid]["Name"] = input("\tEnter the new Name : ")
			if ch==2:
				employees[eid]["Age"] = input("\tEnter the new Age : ")
			if ch==3:
				employees[eid]["Salary"] = input("\tEnter the new Salary : ")
			if ch==4:
				employees[eid]["Gender"] = input("\tEnter the new Gender : ")
		else:
			print("\tEmployee Not Found")

	elif c==5:
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
		
		else:
			print("There is no employee")                
	elif c==6:
		break
	else:
		print("invalid choice")

