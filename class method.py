class company:
    company_name = "GOOGLE"

    @classmethod              #no need to create an object like c = company() for the class
    def change_company(cls, new_company):
        cls.company_name = new_company

company.change_company("HCL")
print(company.company_name)