from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars");
chrome_options.add_argument("start-maximized");

path = "C:\\Users\\thiago.alves\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
driver.get("https://web.whatsapp.com/")
time.sleep(10)
driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[1]/div/div/div[2]').click()
time.sleep(2)
limit = 250
for i in range(100):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(str(i) +': Sou mt fdp')
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()

