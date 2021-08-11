employees = []

while True:
	print("enter 1 for Add Employee")
	print("enter 2 for Delete Employee")
	print("enter 3 for Search Employee")
	print("enter 4 for Change Employee Data")
	print("enter 5 for Display all Employees")
	print("enter 6 for exit")

	c = int(input("enter the choice : "))

	if c==1:
		e = input("Enter the name : ")
		if e != None:
			employees.append(e)	

	elif c==2:
		e = input("Enter the name : ")
		if (e != None and e in employees ):
			employees.remove(e)
		else:
			print("name is incorrect")

	elif c==3:
		e = input("Enter the name to search : ")
		if e != None:
			if e in employees:
				print(e,"is present in the list")
			else:
				print(e,"is not present in the list") 
	elif c==4:
		e = input("Enter the name : ")
		if e != None :
			employees[employees.index(e)] = input("Enter the new name : ")

	elif c==5:
		if employees != None:
			print("____________Employee Details___________")
			for i in range(len(employees)):
				print(str(i+1)+". "+employees[i])
		else:
			print("There is no employee")                
	elif c==6:
		break
	else:
		print("invalid choice")

