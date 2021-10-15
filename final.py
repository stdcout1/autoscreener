from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from json import *
import os, platform
with open('password.pw', 'r') as f:
    stuff = f.read().split('\n')
    EMAIL = stuff[0]
    PW = stuff[1]

print(EMAIL,'d', PW)
# support for macos TODO: add linux when i get raspie
if platform.system() == 'Darwin':
    # we need to promote chromedriver
    os.chmod('defen/chromedriver.exe', 0o755)
    drivger = r'defen/chromedriver'
else:
    drivger = r'defen/chromedriver.exe'

a = []
options = webdriver.ChromeOptions()
#options.add_argument('headless')


driver = webdriver.Chrome(executable_path=drivger,
                            options=options) # i like this. idc about depreciation
driver.get('https://mcteam.co/screening-hs')



#step 1: login! 
try:
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
finally:
    emil = driver.find_element('name','loginfmt')
    emil.send_keys(EMAIL)
    btn = driver.find_element('id','idSIButton9')
    btn.click()
try:
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "passwd"))
    )
finally:
    pw = driver.find_element('name', 'passwd')
    pw.send_keys(PW)
    sleep(1)
    btn2 = driver.find_element('id','idSIButton9')
    btn2.click()
driver.back()

#selection
try:
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "text-format-content"))
    )
finally:
    pass

qts = 'something'
d = 1
while qts:
    d += 1
    if d == 7:
        #answer yes for shorter screening + it applies to me
        qts = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[7]/div/div[2]/div/div[2]')
        qts.click()
    try:
        #rest answer no
        qts = driver.find_element(By.XPATH,f'/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[{d}]/div/div[2]/div/div[1]')
        qts.click()
    except:
        qts = ''
    
try:
    driver.find_element(By.CLASS_NAME,'button-content')
except:
    raise Exception("Something went wrong. Ensure your password is in password.pw")












