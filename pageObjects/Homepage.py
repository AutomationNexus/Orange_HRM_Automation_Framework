from selenium.webdriver.common.by import By

class Homepage:

    frame = ("packageListFrame")
    link = (By.LINK_TEXT, "org.openqa.selenium")
    def __init__(self, driver):
        self.driver = driver

    def framee(self):
        self.driver.find_element(*Homepage.frame)

    driver.switch_to.frame(frame)
    driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()


