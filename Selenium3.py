from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
driver.get('https://www.klix.ba')

login=driver.find_element_by_xpath('/html/body/header/div/div[3]/a')
login.click()

driver.implicitly_wait(5)
tf_username=driver.find_element_by_id("username")
tf_password=driver.find_element_by_id("password")
tf_username.send_keys("")
tf_password.send_keys("")

driver.implicitly_wait(5)
logbutt=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div/div[2]/div/form/div[4]/button')
logbutt.click()

time.sleep(5)
biznis=driver.find_element_by_xpath('/html/body/header/div/div[2]/div[2]/ul/li[2]/div/a')
biznis.click()
time.sleep(2)
biznisVijesti = driver.find_elements_by_tag_name('h2')
trazenaRijec = "dolar"
for pojedinacnaVijest in biznisVijesti:
    v = pojedinacnaVijest.text.lower()
    if trazenaRijec in v:
        pojedinacnaVijest.click()
        break
globalnaVarijabla = driver.find_elements_by_class_name("bg-gray-400")
text="Prikazi sve komentare"
for x in globalnaVarijabla:
    if text in x.text:
        x.click()

trazenikomentar = "ugasi"
sviKomentari = driver.find_elements_by_class_name("komentar")

for x in sviKomentari:
    textKomentara = x.find_element_by_class_name("text-base")
    if trazenikomentar in textKomentara.text:
        buttonVoteUp = x.find_elements_by_class_name("voteUp")
        buttonVoteUp[1].click()
        buttonReply = x.find_elements_by_tag_name("button")
        buttonReply[3].click()
        unesiKomentar = x.find_element_by_xpath("./following-sibling::form")
        textForma = unesiKomentar.find_element_by_tag_name("textarea")
        textForma.send_keys("Ugasi ti")
        time.sleep(2)
        formaButton = unesiKomentar.find_element_by_tag_name("button")
        formaButton.click()
        break
