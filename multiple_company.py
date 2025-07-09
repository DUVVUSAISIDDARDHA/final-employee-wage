from company import Company

class MultipleCompany:
    def __init__(self):
        self.companies = []

    def add_company(self, company_name, wage_per_hour, max_days, max_hours):
        company = Company(company_name, wage_per_hour, max_days, max_hours)
        self.companies.append(company)
        print(f"Company {company_name} added")

    def get_company_by_name(self, company_name):
        for company in self.companies:
            if company.company_name == company_name:
                return company
        return None

    def calculate_all_wages(self):
        for company in self.companies:
            company.calculate_all_employee_monthly_wage()
