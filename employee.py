import random

class Employee:

    def __init__(self, emp_id, emp_name, work_time, wage_per_hour):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.work_time = work_time
        self.wage_per_hour = wage_per_hour

    def attendance_check(self):
        self.attendance = random.randint(0, 1)
        

    def calculate_dialywage(self):
        if self.attendance == 1:
            self.dialywages = self.work_time * self.wage_per_hour
            return f"employee id :{self.emp_id}\n{self.emp_name} is Present"
        else:
            self.dialywages = 0
            return f"employee id :{self.emp_id}\n{self.emp_name} is Absent ,No wage is generated"

    def part_time_full_time(self):
        if self.attendance != 1:
            return ""  
        match self.work_time:
            case hours if hours > 8:
                return f"{self.emp_name} is Full time \nFull time wage : {self.dialywages}"
            case hours if hours <= 8:
                return f"{self.emp_name} is Part time \nFull time wage : {self.dialywages}"