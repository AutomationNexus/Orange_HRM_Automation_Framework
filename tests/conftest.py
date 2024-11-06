import time

import pytest
# from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# as we have to run this code only once so defining the scope at class level
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_option = Options()
        chrome_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
        # driver.maximize_window()
        # driver.get("https://darkshaodow-trials712.orangehrmlive.com/auth/login")
    elif browser_name == "firefox":
        serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver33")
        driver = webdriver.Firefox(service=serv_obj)

    driver.maximize_window()
    driver.get("https://ujjwalsingh560-trials714.orangehrmlive.com/")
    driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("@io61xXFJH")

    time.sleep(1)
    driver.find_element(By.ID, "rememberMe").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)

    #return driver
    request.cls.driver = driver
    yield
    driver.find_element(By.XPATH,'//*[@id="navbar-logout"]/a').click()
    time.sleep(5)
    driver.close()

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)




