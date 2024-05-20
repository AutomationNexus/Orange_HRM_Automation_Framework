import time
# from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from pageObjects.Location import Location
from utilities.BaseClass import BaseClass

from pageObjects.Dashboard import Dashboard


# in this file we write test conditions
# all out test cases should be wrap under a class
# @pytest.mark.usefixtures("setup")
class Testone(BaseClass):
    def test_e2e(self):
        # Navigating to the employee list on the employee portal
        employee_list = Dashboard(self.driver)  # declaring an object for Dashboard class
        location = employee_list.employees_details()  # performing click operation to navigate to the Employee list portal
        time.sleep(5)
        # navigating to the HR Portal
        # location = Location(self.driver)  # declaring an object for Location class
        location.hr_homepage().click()  # performing the click operation to navigate to HR Portal
        time.sleep(5)
        location.hr_location_dropdown().click()  # performing the click operation to open the location dropdown
        time.sleep(5)

        location.location_click().click()  # performing the click operation to click on the location option
        time.sleep(3)
        location.location_new().click()  # performing the click operation to open new Add Location page
        time.sleep(3)
        # location.location_popup_close().click()  # performing the click operation to close the Add Location page

        location.location_city().click()  # entering the data on new location page
        location.location_city().clear()
        location.location_city().send_keys("Faridabad")  # entering city name

        location.location_province().click()
        location.location_province().clear()
        location.location_province().send_keys("Delhi NCR")  # entering province name

        location.location_area().click()
        location.location_area().clear()
        location.location_area().send_keys("Palam Vihar")  # entering area name

        location.location_zipcode().click()
        location.location_zipcode().clear()
        location.location_zipcode().send_keys("123456")  # entering zip code

        location.location_phone().click()
        location.location_phone().clear()
        location.location_phone().send_keys("1234567890")  # entering phone number

        location.location_fax().click()
        location.location_fax().clear()
        location.location_fax().send_keys("54321")  # entering fax number

        location.location_address().click()
        location.location_address().clear()  # entering the address
        location.location_address().send_keys("E-47/A, Q Block, Nayantra Road, Palam Vihar, Gurgaon,Haryana")

        location.location_notes().click()
        location.location_notes().clear()  # entering notes
        location.location_notes().send_keys("This is communication address.")

        # below loop content needs to be skipped
        '''
        driver.find_element(By.XPATH, '//*[@id="countryCode_inputfileddiv"]/div/input').click()

        time.sleep(3)
        countries = driver.find_elements(By.CLASS_NAME, 'select-dropdown')
        for i in range(len(countries)):
            print(countries[i].text)
            if countries[i].text == "Algeria":
                driver.execute_script(countries[i])
        '''

        location.location_country_code().click()  # clicking on country dropdown
        time.sleep(5)
        location.location_country().click()  # clicking on India
        time.sleep(3)
        location.location_timezone().click()  # clicking on timezone dropdown
        time.sleep(5)
        location.location_ist_timezone().click()  # clicking on kolkata timezone
        time.sleep(3)
        # location.location_save().click()

        # location.location_menu().click()
        # driver.quit()
        time.sleep(10)

        # code for general information page
        general_information = location.location_popup_close()

        general_information.general_info_homepage().click()
        time.sleep(5)

        general_information.add_employee().click()
        time.sleep(5)
        # general_information.add_name()
        general_information.add_name().click()
        general_information.add_name().clear()
        general_information.add_name().send_keys("My Own Organization")

        general_information.add_taxid().click()
        general_information.add_taxid().clear()
        general_information.add_taxid().send_keys("123456")

        general_information.add_regnum().click()
        general_information.add_regnum().clear()
        general_information.add_regnum().send_keys("789765")

        general_information.add_phonenum().click()
        general_information.add_phonenum().clear()
        general_information.add_phonenum().send_keys("123456")

        general_information.add_fax().click()
        general_information.add_fax().clear()
        general_information.add_fax().send_keys("123456")

        general_information.add_email().click()
        general_information.add_email().clear()
        general_information.add_email().send_keys("abc@xyz.com")

        general_information.add_street().click()
        general_information.add_street().clear()
        general_information.add_street().send_keys("Palam Vihar")

        general_information.add_street2().click()
        general_information.add_street2().clear()
        general_information.add_street2().send_keys("Sector 23A")

        general_information.add_city().click()
        general_information.add_city().clear()
        general_information.add_city().send_keys("Gurgaon")

        general_information.add_province().click()
        general_information.add_province().clear()
        general_information.add_province().send_keys("Haryana")

        general_information.add_zipcode().click()
        general_information.add_zipcode().clear()
        general_information.add_zipcode().send_keys("98765")

        general_information.add_country().click()
        time.sleep(5)
        general_information.country_selectt().click()

        time.sleep(3)
        general_information.note().click()
        general_information.note().clear()
        general_information.note().send_keys("This is sample note.")
        time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="organizationGeneralInformationDiv"]/form/materializecss-decorator[4]/div/sf-decorator/div/button').click()
        time.sleep(10)

