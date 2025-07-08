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
                return f"{self.emp_name} is Full time \nFull time wage : {self.dialywages}"
            case hours if hours <= 8:
                return f"{self.emp_name} is Part time \nFull time wage : {self.dialywages}"

    def calculate_monthly_wage(self):
        total_wage = 0
        total_present_days = 0
        result = f"Employee ID: {self.emp_id}, Name: {self.emp_name}\n\n"

        for day in range(1, 21):
            self.attendance_check()
            self.calculate_dialywage()

            if self.attendance == 1:
                status = "Present"
                total_present_days += 1
                type_ = ", Full time" if self.work_time > 8 else ", Part time"
            else:
                status = "Absent"
                type_ = ""

            result += f"Day {day} -> {status}{type_}, Work Time: {self.work_time}, Daily Wage: {self.dialywages}\n"
            total_wage += self.dialywages

        result += f"\nTotal Present Days: {total_present_days}\nTotal Monthly Wage: {total_wage}"
        return result
