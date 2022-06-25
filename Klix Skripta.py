from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
driver.get('https://www.klix.ba')
time.sleep(5)

driver.find_element_by_id("user").click()
time.sleep(2)
driver.find_element_by_id("username").send_keys("sevalsalaka1@gmail.com")
driver.find_element_by_id("password").send_keys("sevalsalak1")
prijavi_se = driver.find_element_by_xpath("// button[contains(text(),\
    'Prijavi se')]")
prijavi_se.click()