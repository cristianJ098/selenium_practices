import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

excel_credentials = r'C:\Users\crist\Downloads\selenium_practices\selenium_practices\ejemplo.xlsx'

df = pandas.read_excel(excel_credentials)

url = 'https://www.youtube.com'

# selectors

search_bar = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
search_button = 'search-icon-legacy'
song = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


for i in df.index:
	song2 = str(df['canciones'][i])
	driver.find_element_by_xpath(search_bar).send_keys(song2)
	driver.find_element_by_id(search_button).click()
	# waiting
	wait = WebDriverWait(driver,10)
	wait.until(ec.visibility_of_element_located((By.XPATH,song)))
	#click on song
	driver.find_element_by_xpath(song).click()
	#enjoy the song
	time.sleep(15)
	#clear search bar
	driver.find_element_by_xpath(search_bar).clear()

driver.quit()

