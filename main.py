from employee import Employee

employee1 = Employee("id_1", "sai", 9, 25)

# UC1 - Attendance Check
# print(employee1.attendance_check())

# UC2 - Daily Wage Calculation
# print(employee1.calculate_dialywage())

# UC3 - Part Time / Full Time
# print(employee1.part_time_full_time())

# UC6 - Monthly Wage Calculation (Assume 20 working days and 100 hours)
print(employee1.calculate_monthly_wage())
