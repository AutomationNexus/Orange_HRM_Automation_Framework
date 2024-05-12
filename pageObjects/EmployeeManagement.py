from selenium.webdriver.common.by import By


class EmployeeManagement:
    general_information_homepage = (By.ID, "menu_item_128")
    employee_add = (By.ID, 'addEmployeeButton')
    emp_name = (By.XPATH, '//*[@id="name"]')
    taxid = (By.XPATH, '//*[@id="taxId"]')
    regnum = (By.XPATH, '//*[@id="registraionNumber"]')
    phonenumber = (By.XPATH, '//*[@id="phone"]')
    fax = (By.XPATH, '//*[@id="fax"]')
    email = (By.XPATH, '//*[@id="email"]')
    street = (By.XPATH, '//*[@id="street1"]')
    street2 = (By.XPATH, '//*[@id="street2"]')
    city = (By.XPATH, '//*[@id="city"]')
    province = (By.XPATH, '//*[@id="province"]')
    zipcode = (By.XPATH, '//*[@id="zipCode"]')
    country = (By.XPATH, '//*[@id="country_inputfileddiv"]/div/input')
    country_select = (By.XPATH, "//li[100]//span[contains(text(),'India')][1]")
    notes = (By.XPATH, '//*[@id="note"]')

    def __init__(self, driver):
        self.driver = driver

    def general_info_homepage(self):
        return self.driver.find_element(*EmployeeManagement.general_information_homepage)

    def add_employee(self):
        return self.driver.find_element(*EmployeeManagement.employee_add)

    def add_name(self):
        return self.driver.find_element(*EmployeeManagement.emp_name)

    def add_taxid(self):
        return self.driver.find_element(*EmployeeManagement.taxid)

    def add_regnum(self):
        return self.driver.find_element(*EmployeeManagement.regnum)

    def add_phonenum(self):
        return self.driver.find_element(*EmployeeManagement.phonenumber)

    def add_fax(self):
        return self.driver.find_element(*EmployeeManagement.fax)

    def add_email(self):
        return self.driver.find_element(*EmployeeManagement.email)

    def add_street(self):
        return self.driver.find_element(*EmployeeManagement.street)

    def add_street2(self):
        return self.driver.find_element(*EmployeeManagement.street2)

    def add_city(self):
        return self.driver.find_element(*EmployeeManagement.city)

    def add_province(self):
        return self.driver.find_element(*EmployeeManagement.province)

    def add_zipcode(self):
        return self.driver.find_element(*EmployeeManagement.zipcode)

    def add_country(self):
        return self.driver.find_element(*EmployeeManagement.country)

    def country_selectt(self):
        return self.driver.find_element(*EmployeeManagement.country_select)

    def note(self):
        return self.driver.find_element(*EmployeeManagement.notes)
