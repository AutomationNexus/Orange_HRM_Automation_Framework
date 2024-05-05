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

url = "https://darkshaodow-trials712.orangehrmlive.com/auth/login"
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
driver.get(url)
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.XPATH,"txtUsername").click()
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("@V4c7DvMwT")

time.sleep(1)
driver.find_element(By.ID, "rememberMe").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//li[@id='left_menu_item_10']//a[1]//span[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="top_level_menu_item_menu_item_108"]/a').click()
time.sleep(10)
driver.find_element(By.XPATH, "//a[normalize-space()='Locations']").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="locationDiv"]/div/a/i').click()
time.sleep(3)
driver.find_element(By.ID, "name").click()
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Gurgaon")
driver.find_element(By.ID, "province").click()
driver.find_element(By.ID, "province").clear()
driver.find_element(By.ID, "province").send_keys("Haryana")
driver.find_element(By.ID, "city").click()
driver.find_element(By.ID, "city").clear()
driver.find_element(By.ID, "city").send_keys("Palam Vihar")
driver.find_element(By.ID, "zipCode").click()
driver.find_element(By.ID, "zipCode").clear()
driver.find_element(By.ID, "zipCode").send_keys("123456")
driver.find_element(By.ID, "phone").click()
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys("1234567890")
driver.find_element(By.ID, "fax").click()
driver.find_element(By.ID, "fax").clear()
driver.find_element(By.ID, "fax").send_keys("54321")
driver.find_element(By.ID, "address").click()
driver.find_element(By.ID, "address").clear()
driver.find_element(By.ID, "address").send_keys("E-47/A, Q Block, Nayantra Road, Palam Vihar, Gurgaon,Haryana")
driver.find_element(By.ID, "notes").click()
driver.find_element(By.ID, "notes").clear()
driver.find_element(By.ID, "notes").send_keys("This is communication address.")
driver.find_element(By.XPATH, '//*[@id="countryCode_inputfileddiv"]/div/input').click()

time.sleep(3)
countries = driver.find_elements(By.CLASS_NAME, 'select-dropdown')
for i in range(len(countries)):
    print(countries[i].text)
    if countries[i].text == "Algeria":
        driver.execute_script(countries[i])


time.sleep(10)
driver.quit()
