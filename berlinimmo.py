from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
# Initiate the browser

def scann_wbm():

# closes cookie modal
    def closeCookie():

            buttonsCookies = driver.find_elements(by=By.CLASS_NAME, value="cookie-settings-submit")
            
            if len(buttonsCookies) > 0:
                buttonsCookies[0].click()

 # 1. go to website
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.wbm.de/wohnungen-berlin/angebote/")

    closeCookie()

# 2. get list of offers
    listElements = driver.find_elements(by=By.CLASS_NAME, value="openimmo-search-list-item")
    print(len(listElements))

    if len(listElements) > 0:
    
# 3. if list longer then 0 go to one offer
        linkToElement = listElements[0].find_element(By.TAG_NAME, 'a').get_attribute('href')
        print(linkToElement)
        driver.get(linkToElement)
        closeCookie()

# 4. get a form
        form = driver.find_element(By.CLASS_NAME, 'textWrap')

        form.find_element(By.ID, 'powermail_field_wbsvorhanden_1').click()

        selectDate = form.find_element(By.ID, 'powermail_field_wbsgueltigbis')
        selectDate.click()
        selectDate.send_keys('15082023')
        
        selectZimmer = Select(form.find_element(By.ID, 'powermail_field_wbszimmeranzahl')) 
        selectZimmer.select_by_value('2')

        selectWbs = Select(form.find_element(By.ID, 'powermail_field_einkommensgrenzenacheinkommensbescheinigung9'))
        selectWbs.select_by_value('100')

        form.find_element(By.ID, 'powermail_field_name').send_keys('Pawlak')

        form.find_element(By.ID, 'powermail_field_vorname').send_keys('Gregor')

        form.find_element(By.ID, 'powermail_field_strasse').send_keys('Storkower Str. 177')

        form.find_element(By.ID, 'powermail_field_plz').send_keys('10369')

        form.find_element(By.ID, 'powermail_field_ort').send_keys('Berlin')

        form.find_element(By.ID, 'powermail_field_e_mail').send_keys('greqorian@gmail.com')

        form.find_element(By.ID, 'powermail_field_datenschutzhinweis_1').click()

        form.find_element(By.TAG_NAME, 'button').click()

        # driver.save_screenshot('screenie.png')
        time.sleep(10) # Let the user actually see something!
        
    driver.quit()



def scann_howoge():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get('https://www.howoge.de/wohnungen-gewerbe/wohnungssuche.html')

    buttonsCookies = driver.find_elements(by=By.CLASS_NAME, value="cookie-settings-submit")
    
    if len(buttonsCookies) > 0:
        buttonsCookies[0].click()

    listElements = driver.find_elements(by=By.CLASS_NAME, value="openimmo-search-list-item")
    print(len(listElements))

    if len(listElements) > 0:
       
        linkToElement = listElements[0].find_element(By.TAG_NAME, 'a').get_attribute('href')
        driver.get(linkToElement)
        driver.save_screenshot('screenie.png')
        driver.implicitly_wait(0.5)
        
    # time.sleep(5) # Let the user actually see something!
    driver.quit()

def scann_gewobag():
    
    # 1 open search results
    gewobagSearch = 'https://www.gewobag.de/fuer-mieter-und-mietinteressenten/mietangebote/?bezirke%5B%5D=friedrichshain-kreuzberg&bezirke%5B%5D=friedrichshain-kreuzberg-friedrichshain&bezirke%5B%5D=friedrichshain-kreuzberg-kreuzberg&bezirke%5B%5D=pankow&bezirke%5B%5D=pankow-prenzlauer-berg&bezirke%5B%5D=tempelhof-schoeneberg-schoeneberg&nutzungsarten%5B%5D=wohnung&gesamtmiete_von=&gesamtmiete_bis=&gesamtflaeche_von=&gesamtflaeche_bis=&zimmer_von=2&zimmer_bis=3&sort-by=recent'

    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get(gewobagSearch)
    time.sleep(200) # Let the user actually see something!
    # 2 submit cookie policy
    linkCookies = driver.find_elements(by=By.ID, value='CookieBoxSaveButton')
    
    if len(linkCookies) > 0:
        linkCookies[0].get_attribute('href')

    # 3 search for list of flats
    listContainer = driver.find_elements(by=By.CLASS_NAME, value='filtered-elements filtered-mietangebote')
    listElements = listContainer[0].find_elements(By.TAG_NAME, 'article')
    print(len(listElements))

    # 4. if any offers exist select one
    if len(listElements) > 0:
       
        linkToElement = listElements[0].get_attribute('href')
        driver.get(linkToElement)
        # driver.save_screenshot('screenie.png')
        driver.implicitly_wait(0.5)
        
    # time.sleep(5) # Let the user actually see something!
    driver.quit()

#  run search
scann_wbm()

# scann_gewobag()
