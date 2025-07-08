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
        else:
            self.dialywages = 0

    def part_time_full_time(self):
        if self.attendance != 1:
            return ""
        match self.work_time:
            case hours if hours > 8:
                return f"{self.emp_name} is Full time \nFull time wage is: {self.dialywages}"
            case hours if hours <= 8:
                return f"{self.emp_name} is Part time \nFull time wage is: {self.dialywages}"

    def Calculate_Monthly_Wage(self):
        total_wage = 0
        total_present_days = 0
        total_hours = 0
        total_days = 0
        result = f"Employee ID: {self.emp_id}, Name: {self.emp_name}\n\n"

        while total_days < 20 and total_hours + self.work_time <= 100:
            total_days += 1
            self.attendance_check()
            self.calculate_dialywage()

            if self.attendance == 1:
                status = "Present"
                total_present_days += 1
                total_hours += self.work_time
                type_ = ", Full time" if self.work_time > 8 else ", Part time"
            else:
                status = "Absent"
                type_ = ""

            total_wage += self.dialywages
            result += f"Day {total_days} -> {status}{type_}, Work Time: {self.work_time}, Daily Wage: {self.dialywages}\n"

        result += f"\nTotal Present Days: {total_present_days}\nTotal Hours Worked: {total_hours}\nTotal Wage Till Limit: {total_wage}"
        return result
