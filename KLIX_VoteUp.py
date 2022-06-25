from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-ekstensions")
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

driver = webdriver.Chrome(chrome_options=option, executable_path="chromedriver.exe")
driver.get("http://www.klix.ba")

time.sleep(10)

prijava_korisnika = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/a")
prijava_korisnika.click()

time.sleep(10)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("")
password.send_keys("")

time.sleep(2)

prijavi_se = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div/div[2]/div/form/div[4]/button")
prijavi_se.click()

time.sleep(15)

biznis = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div[2]/ul/li[2]/div/a")
biznis.click()

time.sleep(10)

sportske_vijesti = driver.find_elements(By.TAG_NAME, "h2")

for pojedinacna_vijest in sportske_vijesti:
    rijec = "lidl"
    v = pojedinacna_vijest.text.lower()
    if rijec in v:
        pojedinacna_vijest.click()
        break

time.sleep(10)

otvori_komentare = driver.find_element(By.XPATH, "/html/body/div[3]/article/div[3]/div/div/div[3]/div[2]/div[6]/a")
otvori_komentare.click()

time.sleep(5)


for x in svi_komentari:
    tekstKomentara = x.find_element(By.CLASS_NAME, "text-base")
    if trazena_rijec in tekstKomentara.text:
        dislike = x.find_elements(By.CLASS_NAME, "voteUp")
        dislike[1].click()
        time.sleep(3)
        odgovori = x.find_elements(By.TAG_NAME, "button")
        odgovori[3].click()
        time.sleep(3)
        unesi_komentar = x.find_element(By.XPATH, "./following-sibling::form")
        komentarisi = unesi_komentar.find_element(By.TAG_NAME, "textarea")
        komentarisi.send_keys("Test")
        time.sleep(2)
        postavi = unesi_komentar.find_element(By.TAG_NAME, "button")
        postavi.click()

lista = []

for x in svi_komentari:
    textKomentara = x.find_element(By.CLASS_NAME, "text-base").text.lower()
    if trazena_rijec in textKomentara:
        lista.append(trazena_rijec)
        autor = x.find_elements(By.TAG_NAME, "a")
        lista.append(autor[0].text)
        lista.append(autor[1].text)
        time.sleep(5)
        like = x.find_elements(By.CLASS_NAME, "voteUp")
        lista.append(like[0].text)
        lista.append(like[1].text)

