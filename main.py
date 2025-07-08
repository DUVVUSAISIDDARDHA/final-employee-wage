from company import Company

# USE CASE 7 -
my_company = Company("TCS", wage_per_hour=25, max_days=20, max_hours=100)


my_company.add_employee("id_1", "sai", work_time=9)
my_company.add_employee("id_2", "ram", work_time=8)


my_company.calculate_all_employee_monthly_wage()
