from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from json import *
import os, platform
with open('password.txt', r) as f:
    EMAIL = f.read()
    PW = f.read()


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
                            options=options)
driver.get('https://mcteam.co/screening-hs')
try:
    elem = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
finally:
    emil = driver.find_element_by_name('loginfmt')
    
    btn = driver.find_element_by_id('idSIButton9')
    emil.send_keys(EMAIL)
    sleep(0.5)
    pw = driver.find_element_by_name('passwd')
    pw.send_keys = PW
    btn.click()









