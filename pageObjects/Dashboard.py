from selenium.webdriver.common.by import By


class Dashboard:

    def __init__(self, driver):
        self.driver = driver

    employee_list = (By.LINK_TEXT,"Employee List")

    def employees_details(self):
        return self.driver.find_element(*Dashboard.employee_list)
        # driver.find_element
