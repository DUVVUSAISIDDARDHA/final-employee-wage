from employee import Employee

employee1 = Employee("id_1","sai",7,25)
# USE CASE 1 - attendance checking
employee1.attendance_check()

# USE CASE 2 - Dialy wage
print(employee1.calculate_dialywage())

# USE CASE -3 Part time Full time
print(employee1.part_time_full_time())