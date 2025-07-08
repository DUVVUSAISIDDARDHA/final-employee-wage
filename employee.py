import random

class Employee:
    def __init__(self,emp_name):
        self.emp_name = emp_name
    def attendance_check(self):
        attendance = random.randint(0,1)
        if attendance == 0:
           print(f"{self.emp_name} is present")
        else:
           print(f"{self.emp_name} is Absent")           