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
#driver.find_element(By.XPATH, "//li[@id='left_menu_item_10']//a[1]//span[1]").click()
#time.sleep(5)

#driver.find_element(By.XPATH, '//*[@id="top_level_menu_item_menu_item_108"]/a').click()
#time.sleep(10)
'''
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
'''
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

'''
driver.find_element(By.XPATH, '//*[@id="countryCode_inputfileddiv"]/div/input').click()
time.sleep(5)
driver.find_element(By.XPATH,"//li[100]//span[contains(text(),'India')][1]").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="time_zone_inputfileddiv"]/div/input').click()
time.sleep(5)
driver.find_element(By.XPATH,'//li[384]//span[contains(text(),"(GMT+05:30) India Standard Time - Kolkata")]').click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[@form-name='locationsModalForm' and contains(text(),'Save')]").click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="top_level_menu_item_menu_item_109"]/a').click()
time.sleep(10)
driver.quit()
time.sleep(10)
'''
# code for general information page
'''
driver.find_element(By.XPATH,'//*[@id="top_level_menu_item_menu_item_108"]/sub-menu-container/div/div[1]/a').click()
driver.find_element(By.XPATH,'//*[@id="top_level_menu_item_menu_item_109"]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="name"]').click()
driver.find_element(By.XPATH,'//*[@id="name"]').clear()
driver.find_element(By.XPATH,'//*[@id="name"]').send_keys("My Own Organization")

driver.find_element(By.XPATH,'//*[@id="taxId"]').click()
driver.find_element(By.XPATH,'//*[@id="taxId"]').clear()
driver.find_element(By.XPATH,'//*[@id="taxId"]').send_keys("123456")

driver.find_element(By.XPATH,'//*[@id="registraionNumber"]').click()
driver.find_element(By.XPATH,'//*[@id="registraionNumber"]').clear()
driver.find_element(By.XPATH,'//*[@id="registraionNumber"]').send_keys("789765")

driver.find_element(By.XPATH,'//*[@id="phone"]').click()
driver.find_element(By.XPATH,'//*[@id="phone"]').clear()
driver.find_element(By.XPATH,'//*[@id="phone"]').send_keys("123456")

driver.find_element(By.XPATH,'//*[@id="fax"]').click()
driver.find_element(By.XPATH,'//*[@id="fax"]').clear()
driver.find_element(By.XPATH,'//*[@id="fax"]').send_keys("123456")

driver.find_element(By.XPATH,'//*[@id="email"]').click()
driver.find_element(By.XPATH,'//*[@id="email"]').clear()
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("abc@xyz.com")

driver.find_element(By.XPATH,'//*[@id="street1"]').click()
driver.find_element(By.XPATH,'//*[@id="street1"]').clear()
driver.find_element(By.XPATH,'//*[@id="street1"]').send_keys("Palam Vihar")

driver.find_element(By.XPATH,'//*[@id="street2"]').click()
driver.find_element(By.XPATH,'//*[@id="street2"]').clear()
driver.find_element(By.XPATH,'//*[@id="street2"]').send_keys("Sector 23A")

driver.find_element(By.XPATH,'//*[@id="city"]').click()
driver.find_element(By.XPATH,'//*[@id="city"]').clear()
driver.find_element(By.XPATH,'//*[@id="city"]').send_keys("Gurgaon")

driver.find_element(By.XPATH,'//*[@id="province"]').click()
driver.find_element(By.XPATH,'//*[@id="province"]').clear()
driver.find_element(By.XPATH,'//*[@id="province"]').send_keys("Haryana")

driver.find_element(By.XPATH,'//*[@id="zipCode"]').click()
driver.find_element(By.XPATH,'//*[@id="zipCode"]').clear()
driver.find_element(By.XPATH,'//*[@id="zipCode"]').send_keys("98765")

driver.find_element(By.XPATH, '//*[@id="country_inputfileddiv"]/div/input').click()
time.sleep(5)
time.sleep(5)
driver.find_element(By.XPATH,"//li[100]//span[contains(text(),'India')][1]").click()

time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="note"]').click()
driver.find_element(By.XPATH,'//*[@id="note"]').clear()
driver.find_element(By.XPATH,'//*[@id="note"]').send_keys("This is sample note.")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="organizationGeneralInformationDiv"]/form/materializecss-decorator[4]/div/sf-decorator/div/button').click()
time.sleep(10)
'''
driver.find_element(By.ID, "menu_item_128").click()
time.sleep(5)
driver.find_element(By.ID, "addEmployeeButton").click()
time.sleep(8)
driver.find_element(By.ID, "first-name-box").click()
driver.find_element(By.ID, "first-name-box").clear()
driver.find_element(By.ID, "first-name-box").send_keys("Abc")

driver.find_element(By.ID, "middle-name-box").click()
driver.find_element(By.ID, "middle-name-box").clear()
driver.find_element(By.ID, "middle-name-box").send_keys("PQR")

driver.find_element(By.ID, "last-name-box").click()
driver.find_element(By.ID, "last-name-box").clear()
driver.find_element(By.ID, "last-name-box").send_keys("XYZ")

driver.find_element(By.ID, "joinedDate").click()
driver.find_element(By.ID, "joinedDate").clear()
driver.find_element(By.ID, "joinedDate").send_keys("2024-05-02")

driver.find_element(By.XPATH,
                    '//*[@id="modal-holder"]/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[3]/div/div[3]/div/div[1]/button/div/div/div').click()

# driver.find_elements(By.XPATH,'//*[@id="bs-select-3"]/ul/li[3]').click()
a = driver.find_elements(By.ID, 'bs-select-1-2')
for i in a:
    if i.text == "Gurgaon":
        i.click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="modal-holder"]/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[5]/div/div/span/div[2]').click()
time.sleep(5)

driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "username").send_keys("darkshadow2024")

time.sleep(3)
driver.find_element(By.XPATH,"//label[contains(text(),'Disabled')]").click()

driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("Studio@2023")

driver.find_element(By.ID, "confirmPassword").click()
driver.find_element(By.ID, "confirmPassword").clear()
driver.find_element(By.ID, "confirmPassword").send_keys("Studio@2023")

time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='modal-holder']/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[11]/div/div[1]/div/div[1]/button").click()

driver.find_element(By.XPATH,'//*[@id="modal-holder"]/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[11]/div/div[2]/div/div[1]/button').click()

driver.find_element(By.XPATH,"//*[@id='modal-holder']/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[11]/div/div[3]/div/div[1]/button").click()
time.sleep(3)
a = driver.find_elements(By.XPATH,'//*[@id="modal-holder"]/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[11]/div/div[3]/div/div[1]/div')
time.sleep(3)
driver.find_element(By.XPATH,"//li//a//span[contains(text(),'Global Admin')]").click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="modal-save-button"]').click()

time.sleep(30)
driver.quit()
