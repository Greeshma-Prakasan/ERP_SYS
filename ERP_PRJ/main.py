import employee as emp
import manage_teams as team
from search_emp import search_emp_fn
from change_emp import change_emp_data

def menu():
	print("enter 1 for Add Employee")
	print("enter 2 for Delete Employee")
	print("enter 3 for Search Employee")
	print("enter 4 for Change Employee Data")
	print("enter 5 for Display all Employees")
	print("enter 6 for Manage Teams")
	print("enter 7 for exit")
	


while True:
	
	menu()
	c = int(input("enter the choice : "))

	if c==1:	
		emp.add_employee()
	elif c==2:
		emp.delete_emp()
	elif c==3:
		search_emp_fn()
	elif c==4:
		change_emp_data()
	elif c==5:
		emp.display_emp()       
	elif c==6:
		team.manage_all_teams()
	elif c==7:
		break
	else:
		print("invalid choice")

