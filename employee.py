import random

class Employee:

    def __init__(self,emp_id,emp_name,work_time,wage_per_hour):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.work_time = work_time
        self.wage_per_hour = wage_per_hour

    def attendance_check(self):
        attendance = random.randint(0,1)
        if attendance == 0:
           return f"Absent"
        else:
           return f"Present"

    def calculate_dialywage(self):
        if self.attendance_check():
            dialywages = self.wage_per_hour * self.work_time
            return f"employee id :{self.emp_id}\n{self.emp_name} is Present\nDialywage for {self.emp_name} is {dialywages}"
        else:
            return f"employee id :{self.emp_id}\n{self.emp_name} is Absent ,No wage is generated "

         


        
