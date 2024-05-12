from selenium.webdriver.common.by import By
from pageObjects.EmployeeManagement import *



class Location:
    # driver.find_element(By.XPATH, "//a[normalize-space()='Locations']")

    hr_dashboard = (By.LINK_TEXT, 'HR Administration')

    location_dropdown = (By.XPATH, '//*[@id="top_level_menu_item_menu_item_108"]/a')
    location_button = (By.XPATH, "//a[normalize-space()='Locations']")
    location_add = (By.XPATH, '//*[@id="locationDiv"]/div/a/i')
    location_cancel = (By.XPATH,'//*[@id="locationAddModal"]/form/div[2]/a[2]')

    city = (By.ID, "name")
    province = (By.ID, "province")
    area = (By.ID, "city")
    zipcode = (By.ID, "zipCode")
    phone = (By.ID, "phone")
    fax = (By.ID, "fax")
    address = (By.ID, "address")
    notes = (By.ID, "notes")
    country_code = (By.XPATH, '//*[@id="countryCode_inputfileddiv"]/div/input')
    country = (By.XPATH, "//li[100]//span[contains(text(),'India')][1]")
    time_zone = (By.XPATH, '//*[@id="time_zone_inputfileddiv"]/div/input')
    ist_timezone = (By.XPATH,'//li[384]//span[contains(text(),"(GMT+05:30) India Standard Time - Kolkata")]')
    save = (By.XPATH, "//a[@form-name='locationsModalForm' and contains(text(),'Save')]")
    menu = (By.XPATH, '//*[@id="top_level_menu_item_menu_item_109"]/a')


    def __init__(self, driver):
        self.driver = driver

    def hr_homepage(self):
        return self.driver.find_element(*Location.hr_dashboard)

    def hr_location_dropdown(self):
        return self.driver.find_element(*Location.location_dropdown)

    def location_click(self):
        return self.driver.find_element(*Location.location_button)

    def location_new(self):
        return self.driver.find_element(*Location.location_add)

    def location_city(self):
        return self.driver.find_element(*Location.city)

    def location_province(self):
        return self.driver.find_element(*Location.province)

    def location_area(self):
        return self.driver.find_element(*Location.area)

    def location_zipcode(self):
        return self.driver.find_element(*Location.zipcode)

    def location_phone(self):
        return self.driver.find_element(*Location.phone)

    def location_fax(self):
        return self.driver.find_element(*Location.fax)

    def location_address(self):
        return self.driver.find_element(*Location.address)

    def location_notes(self):
        return self.driver.find_element(*Location.notes)

    def location_country_code(self):
        return self.driver.find_element(*Location.country_code)

    def location_country(self):
        return self.driver.find_element(*Location.country)

    def location_timezone(self):
        return self.driver.find_element(*Location.time_zone)

    def location_ist_timezone(self):
        return self.driver.find_element(*Location.ist_timezone)

    def location_save(self):
        return self.driver.find_element(*Location.save)

    def location_menu(self):
        return self.driver.find_element(*Location.menu)

    def location_popup_close(self):
        self.driver.find_element(*Location.location_cancel).click()
        general_information = EmployeeManagement(self.driver)
        return general_information







