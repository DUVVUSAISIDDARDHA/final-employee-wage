from employee import Employee

class Company:
    def __init__(self, company_name, wage_per_hour, max_days, max_hours):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.max_days = max_days
        self.max_hours = max_hours
        self.employees = []

    def add_employee(self, emp_id, emp_name, work_time):
        emp = Employee(emp_id, emp_name, work_time, self.wage_per_hour)
        self.employees.append(emp)
        print(f"Added employee {emp_id} with name {emp_name} to {self.company_name}.")
        return emp

    def get_employees(self):
        print(f"Employees in {self.company_name}:")
        for emp in self.employees:
            print(f"{emp.emp_id:<10} {emp.emp_name:<10}")
        return self.employees

    def calculate_all_employee_monthly_wage(self):
        print(f"\nCalculating monthly wages for all employees in {self.company_name}...\n")
        for emp in self.employees:
            print(emp.Calculate_Monthly_Wage())
            print("-" * 60)
