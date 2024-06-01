from selenium.webdriver.common.by import By

from pageObjects.Location import Location
# this is for dashboard

class Dashboard:

    def __init__(self, driver):
        self.driver = driver

    employee_list = (By.LINK_TEXT,"Employee List")

    def employees_details(self):
        self.driver.find_element(*Dashboard.employee_list).click()
        location = Location(self.driver)
        return location
        # driver.find_element
