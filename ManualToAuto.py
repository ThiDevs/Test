from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars");
chrome_options.add_argument("start-maximized");

path = "C:\\Users\\thiago.alves\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
driver.get("http://fluig.extrabom.com.br/portal/p/01/ecmnavigation#")
driver.find_element_by_xpath('//*[@id="username"]').send_keys('processo.fluig')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('TnCH1DN9WHes')
driver.find_element_by_xpath('//*[@id="submitLogin"]').click()

time.sleep(5)
try:
    driver.find_element_by_xpath('//*[@id="fluig-modal"]/div/div/div[1]/button/span[1]').click()
except Exception:
    pass
driver.find_element_by_xpath('//*[@id="document-description-2"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="document-description-182138"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="document-description-182161"]').click()
time.sleep(2)
driver.execute_script("scroll(0, -250);")
driver.find_element_by_xpath('//*[@id="next_ecm-navigation-page"]').click()
time.sleep(2)
elements = driver.find_elements_by_tag_name('tr')
print(len(elements))

for element in elements:
    id = element.get_attribute('id')

    if id != "":
        print(id)
        element.find_element_by_xpath('//*[@id="'+id+'"]/td[3]').click()
        name = element.find_element_by_xpath('//*[@id="document-description-'+id+'"]').text + '.old'
        element.find_element_by_xpath('// *[ @ id = "dropdown_navigation_'+id+'"] / span').click()
        e


        time.sleep(2)
       # driver.find_element_by_xpath('//*[@id="wcm-panel-wcmid9"]/div[2]/div[2]/div[1]/div[2]').click()
        break

   # element.find_elements_by_tag_name('tr').





#a = driver.find_element_by_xpath('//*[@id="236461"]/td[3]').text()
#print(a)


#




#

time.sleep(5)
driver.close()
