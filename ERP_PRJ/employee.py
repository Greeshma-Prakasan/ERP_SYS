from user import User
employees = []

class Employee(User):
	def __init__(self,eid,name,age,gender,place,salary,pre_com,j_date):
		self.employee_id = eid
		self.name = name
		self.age = age
		self.gender = gender
		self.place = place
		self.salary = salary
		self.previous_company = pre_com
		self.joining_date = j_date


	def set_name(self,name):
		self.name = name
	def set_age(self,age):
		self.age = age
	def set_gender(self,gender):
		self.gender = gender
	def set_salary(self,salary):
		self.salary = salary



def add_employee():
	eid = int(input("\tEnter the Employee id : "))
	n = input("\tEnter the name : ")
	a = int(input("\tEnter the age : "))
	g = input("\tEnter the gender : ")
	p = input("\tEnter the place : ")
	s = int(input("\tEnter the salary : "))
	pre = input("\tEnter the previous company : ")
	j = input("\tEnter the joining date : ")
	role = input("\tEnter the role : ")
	u = input("\tEnter the Username : ")
	pas = input("\tEnter the Password : ")
	# if eid not in employees.keys():
	# 	employees[eid] = {"Name":n,"Age":a,"Gender":g,"Place":p,"Salary":s,"Previous Company":pre,"Joining Date":j}
	#
	# else:
	# 	print("\tEmployee id is already present")
	if eid:
		e = Employee(eid,n,a,g,p,s,pre,j)
		e.role = role
		e.set_username(u)
		e.set_password(pas)
		employees.append(e)


def delete_emp():
	eid = int(input("Enter the Employee id : "))
	for i in employees:
		if i.employee_id == eid:
			employees.remove(i)
			print("Deleted Successfully")

	# if (eid in employees.keys()):
	# 	del employees[eid]
	# 	print("Deleted Successfully")
	# else:
	# 	print("Employee id is incorrect")
		
def display_emp():

	if employees != None:
		# for i,j in employees.items():
		# 	print(f"{i} :\tName - {j['Name']}")
		# 	print(f"\tAge - {j['Age']}")
		# 	print(f"\tGender - {j['Gender']}")
		# 	print(f"\tPlace - {j['Place']}")
		# 	print(f"\tSalary - {j['Salary']}")
		# 	print(f"\tPrevious Company - {j['Previous Company']}")
		# 	print(f"\tJoining Date - {j['Joining Date']}")
		print("\t__________Employee Details____________")
		for i in employees:
			print(f"\tEmployee Id - {i.employee_id}")
			print(f"\tName - {i.name}")
			print(f"\tAge - {i.age}")
			print(f"\tGender - {i.gender}")
			print(f"\tPlace - {i.place}")
			print(f"\tSalary - {i.salary}")
			print(f"\tPrevious Company - {i.previous_company}")
			print(f"\tJoining Date - {i.joining_date}")
			print(f"\tUsername - {i.get_username()}")
			print(f"\tRole - {i.role}")
			print("\t_________________________________________________")



