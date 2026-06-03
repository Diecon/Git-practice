class company:
    company_name = "GOOGLE"

    @staticmethod
    def change_company(new_company):
        company_name = new_company

company.change_company("HCL")
print(company.company_name)        #outputs GOOGLE since there is no self,cls for overriding the values on the classes