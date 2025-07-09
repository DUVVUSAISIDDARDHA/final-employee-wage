from multiple_company import MultipleCompany

multi = MultipleCompany()

multi.add_company("TCS", 25, 20, 100)
multi.add_company("Infosys", 30, 20, 100)

tcs = multi.get_company_by_name("TCS")
tcs.add_employee("id_1", "Sai", 9)
tcs.add_employee("id_2", "Kiran", 8)

infosys = multi.get_company_by_name("Infosys")
infosys.add_employee("id_1", "Raj", 7)
infosys.add_employee("id_2", "Meena", 9)

multi.calculate_all_wages()
