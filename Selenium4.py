import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
driver.get('https://www.klix.ba/')
time.sleep(3)
login = driver.find_element_by_xpath("/html/body/header/div/div[3]/a/div")
login.click()
time.sleep(1)
id_username = driver.find_element_by_id("username")
id_password = driver.find_element_by_id("password")
id_username.send_keys("")
id_password.send_keys("")
prijava = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div/div[2]/div/form/div[4]/button")
prijava.click()
time.sleep(3)

search=driver.find_element_by_id("search-open")
search.click()
trazi=driver.find_element_by_name("q")
trazi.send_keys("audi")
trazi.send_keys(Keys.ENTER)


biznis = driver.find_element_by_xpath("/html/body/header/div/div[2]/div[2]/ul/li[2]/div/a")
biznis.click()
biznisvjest = driver.find_elements_by_tag_name("h2")
time.sleep(5)
trazenarjec = "elon"
for pojedinacnavijest in biznisvjest:
    v = pojedinacnavijest.text.lower()
    if trazenarjec in v :
        pojedinacnavijest.click()
        break
time.sleep(5)
komentar = driver.find_element_by_xpath("/html/body/div[3]/article/div[3]/div/div/div[3]/div[2]/div[6]/a")
komentar.click()
time.sleep(2)
kupiiugasi = "ugasi"

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

time.sleep(2)
komentarisi=driver.find_element_by_id("komentarinput")
komentarisi.send_keys("MA BJAZIIIIII BA")
submit=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div/div/form/div/button")
submit.click()