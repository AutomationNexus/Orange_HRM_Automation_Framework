from selenium.webdriver.common.by import By


class Location:
    # driver.find_element(By.XPATH, "//a[normalize-space()='Locations']")

    hr_dashboard = (By.LINK_TEXT, 'HR Administration')

    location_dropdown = (By.XPATH, '//*[@id="top_level_menu_item_menu_item_108"]/a')
    location_button = (By.XPATH, "//a[normalize-space()='Locations']")
    location_add = (By.XPATH, '//*[@id="locationDiv"]/div/a/i')
    location_cancel = (By.XPATH,'//*[@id="locationAddModal"]/form/div[2]/a[2]')

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

    def location_popup_close(self):
        return self.driver.find_element(*Location.location_cancel)
