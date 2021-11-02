import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

excel_credentials = r'C:\Users\crist\Downloads\selenium_practices\selenium_practices\ejemplo.xlsx'

df = pandas.read_excel(excel_credentials)

user = df['name'][0]
psw = df['password'][0]

url = 'http://www.linkedin.com'

#selectores

sig_in_button = 'body > nav > div > a.nav__button-secondary'
user_selector ='username'
password_selector = 'password'
login_button = '#organic-div > form > div.login__form_action_container > button'

# open browser

driver = webdriver.Chrome()

#maximimize screen

driver.maximize_window()

driver.get(url)

# Actions on the web page

driver.find_element_by_css_selector(sig_in_button).click()
driver.find_element_by_id(user_selector).send_keys(user)
driver.find_element_by_id(password_selector).send_keys(psw)
driver.find_element_by_css_selector(login_button).click()

#more actions on the web pages

time.sleep(5)

#close browser

driver.quit()