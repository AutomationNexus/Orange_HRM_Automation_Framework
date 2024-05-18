from selenium.webdriver.common.by import By


class Homepage:
    frame = (By.XPATH, '//*[@id="divInAppMarketing"]/iframe')
    link = (By.XPATH, '//*[@id="in-app-content"]')

    def __init__(self, driver):
        self.driver = driver

    def framee(self):
        self.driver.switch_to.frame(*Homepage.frame)
        return self.driver.find_elements(*Homepage.link)




#  driver.switch_to.frame(frame)
#  driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
