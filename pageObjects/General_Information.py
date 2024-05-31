from selenium.webdriver.common.by import By


class GeneralInformation:
    general_information_homepage = (By.XPATH, "//a[@class='top-level-menu-item active']")
    employee_add = (By.ID, 'addEmployeeButton')
    emp_name = (By.XPATH, "//input[@id='name']")
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
    submitt = (By.XPATH, "//button[@type='submit']")
    toast_msg = (By.XPATH, '//*[@id="toast-container"]/div/div')

    def __init__(self, driver):
        self.driver = driver

    def general_info_homepage(self):
        return self.driver.find_element(*GeneralInformation.general_information_homepage)

    def add_employee(self):
        return self.driver.find_element(*GeneralInformation.employee_add)

    def add_name(self):
        return self.driver.find_element(*GeneralInformation.emp_name)

    def add_taxid(self):
        return self.driver.find_element(*GeneralInformation.taxid)

    def add_regnum(self):
        return self.driver.find_element(*GeneralInformation.regnum)

    def add_phonenum(self):
        return self.driver.find_element(*GeneralInformation.phonenumber)

    def add_fax(self):
        return self.driver.find_element(*GeneralInformation.fax)

    def add_email(self):
        return self.driver.find_element(*GeneralInformation.email)

    def add_street(self):
        return self.driver.find_element(*GeneralInformation.street)

    def add_street2(self):
        return self.driver.find_element(*GeneralInformation.street2)

    def add_city(self):
        return self.driver.find_element(*GeneralInformation.city)

    def add_province(self):
        return self.driver.find_element(*GeneralInformation.province)

    def add_zipcode(self):
        return self.driver.find_element(*GeneralInformation.zipcode)

    def add_country(self):
        return self.driver.find_element(*GeneralInformation.country)

    def country_selectt(self):
        return self.driver.find_element(*GeneralInformation.country_select)

    def note(self):
        return self.driver.find_element(*GeneralInformation.notes)

    def submit(self):
        return self.driver.find_element(*GeneralInformation.submitt)

    #def msg(self):
     #   return self.driver.find_element(*GeneralInformation.toast_msg)

