import time
from pkg_resources import to_filename 
from selenium import webdriver  
driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://www.it-akademija.com")
print(driver.title)
dlsbutton = driver.find_element_by_xpath("/html/body/header/div[1]/ul/li[2]/a")
dlsbutton.click()
ime_username = driver.find_element_by_id("username")
ime_password = driver.find_element_by_id("password")
ime_username.send_keys("")
ime_password.send_keys("")
loginbuton = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[1]/div/div[1]/form/div[3]/div[1]/input")
loginbuton.click()
dropdown = driver.find_element_by_xpath("/html/body/div[2]/div/nav/ul/li[8]/a")
dropdown.click()
time.sleep(2)
video = driver.find_element_by_xpath("/html/body/div[2]/div/nav/ul/li[8]/ul/li[7]/a")
video.click()
time.sleep(2)
snimak = driver.find_element_by_xpath("/html/body/div[2]/main/div/div/div/div/div/div[2]/div[2]/form/div[3]/div/div[1]/div[1]/div/a[1]")
snimak.click()
time.sleep(10)
play = driver.find_element_by_xpath("/html/body")
play.click()
brojac = 0
while True:
    driver.get_screenshot_as_png()
    driver.save_screenshot(f"screenshot{brojac}.png")
    time.sleep(5)
    brojac += 1
    if brojac==10:
        break
play.click()
time.sleep(3)
drag=driver.find_element_by_aria_value_text("2:47:20")
drag.click()
